package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"

	"gopkg.in/yaml.v3"
)

type Breach struct {
	SourceName   string   `yaml:"source_name"`
	SourceURL    string   `yaml:"source_url"`
	DateOfBreach string   `yaml:"date_of_breach"`
	Category     string   `yaml:"category"`
	CVE          []string `yaml:"cve"`
	Notes        string   `yaml:"notes"`
}

var validCategories = map[string]bool{
	"ransomware":       true,
	"data-leak":        true,
	"supply-chain":     true,
	"credential-theft": true,
	"other":            true,
}

func main() {
	base := "."
	if len(os.Args) > 1 {
		base = os.Args[1]
	}
	dirs := []string{"ransomware", "data-leak", "supply-chain", "credential-theft", "other"}
	errors := 0
	total := 0

	for _, dir := range dirs {
		files, err := filepath.Glob(filepath.Join(base, dir, "*.yaml"))
		if err != nil {
			fmt.Printf("ERROR: globbing %s: %v\n", dir, err)
			errors++
			continue
		}

		for _, file := range files {
			total++
			data, err := os.ReadFile(file)
			if err != nil {
				fmt.Printf("ERROR: reading %s: %v\n", file, err)
				errors++
				continue
			}

			var breach Breach
			if err := yaml.Unmarshal(data, &breach); err != nil {
				fmt.Printf("ERROR: invalid YAML in %s: %v\n", file, err)
				errors++
				continue
			}

			if breach.SourceName == "" {
				fmt.Printf("ERROR: %s missing source_name\n", file)
				errors++
			}
			if breach.DateOfBreach == "" {
				fmt.Printf("ERROR: %s missing date_of_breach\n", file)
				errors++
			}
			if breach.Category == "" {
				fmt.Printf("ERROR: %s missing category\n", file)
				errors++
			} else if !validCategories[breach.Category] {
				fmt.Printf("ERROR: %s invalid category: %s\n", file, breach.Category)
				errors++
			}
			// Verify file is in correct category directory
			expectedDir := breach.Category
			if expectedDir != "" && !strings.Contains(file, "/"+expectedDir+"/") && !strings.HasPrefix(file, expectedDir+"/") {
				fmt.Printf("WARN: %s has category '%s' but is in wrong directory\n", file, breach.Category)
			}
		}
	}

	fmt.Printf("\nValidated %d breach files\n", total)
	if errors > 0 {
		fmt.Printf("Found %d errors\n", errors)
		os.Exit(1)
	}
	fmt.Println("All files valid")
}
