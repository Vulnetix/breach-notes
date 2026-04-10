package main

import (
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"strings"
	"time"

	"gopkg.in/yaml.v3"
)

// yaml.v3 automatically parses unquoted YYYY-MM-DD values as time.Time.
// rawString coerces such values back to their canonical string form.
func rawString(v interface{}) (string, bool) {
	switch s := v.(type) {
	case string:
		return s, true
	case time.Time:
		return s.Format("2006-01-02"), true
	}
	return "", false
}

// ── Schema types ──────────────────────────────────────────────────────────────

type SchemaItems struct {
	Pattern string `yaml:"pattern"`
}

type SchemaField struct {
	Group       string      `yaml:"group"`
	Type        string      `yaml:"type"`   // string | bool | number | integer | list
	Required    bool        `yaml:"required"`
	Format      string      `yaml:"format"` // date_flexible | date_flexible_or_empty | ""
	Enum        []string    `yaml:"enum"`
	Items       SchemaItems `yaml:"items"`
	Minimum     *float64    `yaml:"minimum"`
	Description string      `yaml:"description"`
}

type Schema struct {
	Version string                 `yaml:"version"`
	Fields  map[string]SchemaField `yaml:"fields"`
}

// ── Validation state ──────────────────────────────────────────────────────────

type result struct {
	errors   int
	warnings int
}

func (r *result) errorf(format string, args ...interface{}) {
	fmt.Printf("ERROR: "+format+"\n", args...)
	r.errors++
}

func (r *result) warnf(format string, args ...interface{}) {
	fmt.Printf("WARN:  "+format+"\n", args...)
	r.warnings++
}

// ── Entry point ───────────────────────────────────────────────────────────────

func main() {
	base := "."
	if len(os.Args) > 1 {
		base = os.Args[1]
	}

	schema, err := loadSchema(filepath.Join(base, "schema.yaml"))
	if err != nil {
		fmt.Printf("ERROR: cannot load schema: %v\n", err)
		os.Exit(1)
	}

	dirs := []string{"ransomware", "data-leak", "supply-chain", "credential-theft", "other"}
	res := &result{}
	total := 0

	for _, dir := range dirs {
		files, err := filepath.Glob(filepath.Join(base, dir, "*.yaml"))
		if err != nil {
			res.errorf("globbing %s: %v", dir, err)
			continue
		}
		for _, file := range files {
			total++
			validateFile(file, dir, schema, res)
		}
	}

	fmt.Printf("\nValidated %d files — %d error(s), %d warning(s)\n", total, res.errors, res.warnings)
	if res.errors > 0 {
		os.Exit(1)
	}
}

// ── Schema loading ────────────────────────────────────────────────────────────

func loadSchema(path string) (*Schema, error) {
	data, err := os.ReadFile(path)
	if err != nil {
		return nil, err
	}
	var s Schema
	if err := yaml.Unmarshal(data, &s); err != nil {
		return nil, fmt.Errorf("parsing %s: %w", path, err)
	}
	if len(s.Fields) == 0 {
		return nil, fmt.Errorf("%s defines no fields", path)
	}
	return &s, nil
}

// ── File validation ───────────────────────────────────────────────────────────

func validateFile(file, expectedDir string, schema *Schema, res *result) {
	data, err := os.ReadFile(file)
	if err != nil {
		res.errorf("reading %s: %v", file, err)
		return
	}

	// Unmarshal to a generic map so we can inspect every key.
	var doc map[string]interface{}
	if err := yaml.Unmarshal(data, &doc); err != nil {
		res.errorf("invalid YAML in %s: %v", file, err)
		return
	}
	if doc == nil {
		res.errorf("%s is empty", file)
		return
	}

	// 1. Schema checks: required fields, types, enum, format, minimum.
	for fieldName, spec := range schema.Fields {
		raw, present := doc[fieldName]
		validateField(file, fieldName, raw, present, spec, res)
	}

	// 2. Unknown field check — warn about keys not in the schema.
	for key := range doc {
		if _, known := schema.Fields[key]; !known {
			res.warnf("%s: unknown field %q (not in schema.yaml)", file, key)
		}
	}

	// 3. Category must place file in the correct directory.
	if cat, ok := doc["category"].(string); ok && cat != "" {
		if !strings.Contains(file, string(filepath.Separator)+cat+string(filepath.Separator)) &&
			!strings.HasPrefix(file, cat+string(filepath.Separator)) {
			res.warnf("%s: category %q but file is not in %s/", file, cat, cat)
		}
	}
}

// validateField checks a single field value against its schema spec.
func validateField(file, name string, raw interface{}, present bool, spec SchemaField, res *result) {
	// Missing field.
	if !present || raw == nil {
		if spec.Required {
			res.errorf("%s: required field %q is missing", file, name)
		}
		return
	}

	// Empty string for a required field.
	if s, ok := rawString(raw); ok && spec.Required && strings.TrimSpace(s) == "" {
		res.errorf("%s: required field %q is empty", file, name)
		return
	}

	// Type check.
	switch spec.Type {
	case "string":
		if _, ok := rawString(raw); !ok {
			res.errorf("%s: field %q must be a string, got %T", file, name, raw)
			return
		}
	case "bool":
		if _, ok := raw.(bool); !ok {
			res.errorf("%s: field %q must be a bool, got %T", file, name, raw)
			return
		}
	case "number":
		if !isNumber(raw) {
			res.errorf("%s: field %q must be a number, got %T", file, name, raw)
			return
		}
	case "integer":
		if !isInteger(raw) {
			res.errorf("%s: field %q must be an integer, got %T", file, name, raw)
			return
		}
	case "list":
		items, ok := raw.([]interface{})
		if !ok {
			res.errorf("%s: field %q must be a list, got %T", file, name, raw)
			return
		}
		if spec.Items.Pattern != "" {
			re, err := regexp.Compile(spec.Items.Pattern)
			if err == nil {
				for _, item := range items {
					s, ok := item.(string)
					if !ok {
						res.errorf("%s: field %q list item must be a string, got %T", file, name, item)
						continue
					}
					if !re.MatchString(s) {
						res.errorf("%s: field %q item %q does not match pattern %s", file, name, s, spec.Items.Pattern)
					}
				}
			}
		}
		return // no further checks for lists
	}

	// Enum check.
	if len(spec.Enum) > 0 {
		s, _ := rawString(raw)
		if !contains(spec.Enum, s) {
			res.errorf("%s: field %q value %q not in allowed set %v", file, name, s, spec.Enum)
		}
	}

	// Format check (dates).
	if spec.Format != "" {
		// time.Time values were already parsed as valid dates by yaml.v3.
		if _, isTime := raw.(time.Time); isTime {
			return
		}
		s, _ := rawString(raw)
		checkDateFormat(file, name, s, spec.Format, res)
	}

	// Minimum check (number / integer).
	if spec.Minimum != nil {
		v := toFloat(raw)
		if v < *spec.Minimum {
			res.errorf("%s: field %q value %v is below minimum %v", file, name, v, *spec.Minimum)
		}
	}
}

// ── Helper functions ──────────────────────────────────────────────────────────

func isNumber(v interface{}) bool {
	switch v.(type) {
	case int, int64, float64:
		return true
	}
	return false
}

func isInteger(v interface{}) bool {
	switch v.(type) {
	case int, int64:
		return true
	case float64:
		f := v.(float64)
		return f == float64(int64(f))
	}
	return false
}

func toFloat(v interface{}) float64 {
	switch n := v.(type) {
	case int:
		return float64(n)
	case int64:
		return float64(n)
	case float64:
		return n
	}
	return 0
}

func contains(list []string, s string) bool {
	for _, v := range list {
		if v == s {
			return true
		}
	}
	return false
}

var dateLayouts = []string{"2006-01-02", "2006-01", "2006"}

func checkDateFormat(file, field, value, format string, res *result) {
	if format == "date_flexible_or_empty" && (value == "" || strings.ToLower(value) == "unknown") {
		return
	}
	for _, layout := range dateLayouts {
		if _, err := time.Parse(layout, value); err == nil {
			return
		}
	}
	res.errorf("%s: field %q value %q is not a valid date (expected YYYY-MM-DD, YYYY-MM, or YYYY)", file, field, value)
}
