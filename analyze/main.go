package main

import (
	"fmt"
	"os"
	"path/filepath"
	"sort"
	"strings"
	"time"

	"gopkg.in/yaml.v3"
)

type Breach struct {
	SourceName               string   `yaml:"source_name"`
	SourceURL                string   `yaml:"source_url"`
	DateOfBreach             string   `yaml:"date_of_breach"`
	DateOfDisclosure         string   `yaml:"date_of_disclosure"`
	DateOfCustomerNotif      string   `yaml:"date_of_customer_notification"`
	Category                 string   `yaml:"category"`
	InitialAttackVector      string   `yaml:"initial_attack_vector"`
	CVE                      []string `yaml:"cve"`
	VendorProduct            string   `yaml:"vendor_product"`
	SoftwarePackage          string   `yaml:"software_package"`
	Malware                  string   `yaml:"malware"`
	SupplyChainClaimed       bool     `yaml:"supply_chain_claimed"`
	Notes                    string   `yaml:"notes"`
	FilePath                 string
}

func main() {
	root := "."
	if len(os.Args) > 1 {
		root = os.Args[1]
	}

	breaches, err := loadBreaches(root)
	if err != nil {
		fmt.Fprintf(os.Stderr, "error loading breaches: %v\n", err)
		os.Exit(1)
	}

	readme := generateREADME(breaches)

	outPath := filepath.Join(root, "README.md")
	if err := os.WriteFile(outPath, []byte(readme), 0644); err != nil {
		fmt.Fprintf(os.Stderr, "error writing README: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("Updated %s with stats for %d breaches\n", outPath, len(breaches))
}

func loadBreaches(root string) ([]Breach, error) {
	var breaches []Breach
	categories := []string{"ransomware", "data-leak", "supply-chain", "credential-theft", "other"}
	for _, cat := range categories {
		dir := filepath.Join(root, cat)
		entries, err := os.ReadDir(dir)
		if err != nil {
			continue
		}
		for _, e := range entries {
			if e.IsDir() || !strings.HasSuffix(e.Name(), ".yaml") {
				continue
			}
			path := filepath.Join(dir, e.Name())
			data, err := os.ReadFile(path)
			if err != nil {
				continue
			}
			var b Breach
			if err := yaml.Unmarshal(data, &b); err != nil {
				fmt.Fprintf(os.Stderr, "warning: parse error in %s: %v\n", path, err)
				continue
			}
			b.FilePath = path
			if b.Category == "" {
				b.Category = cat
			}
			// Skip editorial stubs (DataBreachToday/ISMG article titles, not breach records)
			if strings.Contains(b.SourceName, "(DataBreachToday)") ||
				strings.Contains(b.SourceName, "(ISMG") {
				continue
			}
			breaches = append(breaches, b)
		}
	}
	return breaches, nil
}

func generateREADME(breaches []Breach) string {
	total := len(breaches)
	now := time.Now().UTC().Format("2006-01-02")

	// Category counts
	catCount := map[string]int{}
	for _, b := range breaches {
		catCount[b.Category]++
	}

	// CVE coverage
	withCVE, totalCVEs := 0, 0
	cveSet := map[string]bool{}
	for _, b := range breaches {
		if len(b.CVE) > 0 {
			withCVE++
			for _, c := range b.CVE {
				c = strings.TrimSpace(c)
				if c != "" {
					cveSet[c] = true
					totalCVEs++
				}
			}
		}
	}

	// Malware coverage
	malwareCount := map[string]int{}
	withMalware := 0
	for _, b := range breaches {
		if b.Malware != "" {
			withMalware++
			name := normalizeMalware(b.Malware)
			malwareCount[name]++
		}
	}

	// Supply chain
	supplyChain := 0
	for _, b := range breaches {
		if b.SupplyChainClaimed {
			supplyChain++
		}
	}

	// Vendor products
	vendorSet := map[string]int{}
	for _, b := range breaches {
		if b.VendorProduct != "" {
			vendorSet[b.VendorProduct]++
		}
	}

	// Attack vectors (CWE)
	vectorCount := map[string]int{}
	for _, b := range breaches {
		if b.InitialAttackVector != "" && b.InitialAttackVector != "unknown" {
			v := b.InitialAttackVector
			vectorCount[v]++
		}
	}

	// Year distribution
	yearCount := map[string]int{}
	for _, b := range breaches {
		y := extractYear(b.DateOfBreach)
		if y != "" {
			yearCount[y]++
		}
	}

	// Disclosure lag stats
	var lags []int
	for _, b := range breaches {
		lag := disclosureLagDays(b.DateOfBreach, b.DateOfDisclosure)
		if lag >= 0 {
			lags = append(lags, lag)
		}
	}

	var sb strings.Builder

	sb.WriteString("# breach-notes\n\n")
	sb.WriteString("Structured YAML records of breach reports, advisories, and cyber incidents.\n\n")
	sb.WriteString(fmt.Sprintf("**Last updated:** %s  **Total records:** %d\n\n", now, total))
	sb.WriteString("---\n\n")

	sb.WriteString("## Summary Statistics\n\n")
	sb.WriteString(fmt.Sprintf("| Metric | Value |\n|--------|-------|\n"))
	sb.WriteString(fmt.Sprintf("| Total incidents | %d |\n", total))
	sb.WriteString(fmt.Sprintf("| With CVE/GHSA references | %d (%.0f%%) |\n", withCVE, pct(withCVE, total)))
	sb.WriteString(fmt.Sprintf("| Unique CVEs/GHSAs | %d |\n", len(cveSet)))
	sb.WriteString(fmt.Sprintf("| With malware identified | %d (%.0f%%) |\n", withMalware, pct(withMalware, total)))
	sb.WriteString(fmt.Sprintf("| Supply chain claimed | %d (%.0f%%) |\n", supplyChain, pct(supplyChain, total)))
	sb.WriteString(fmt.Sprintf("| Unique vendor products | %d |\n", len(vendorSet)))
	if len(lags) > 0 {
		sb.WriteString(fmt.Sprintf("| Median disclosure lag (days) | %d |\n", median(lags)))
		sb.WriteString(fmt.Sprintf("| Max disclosure lag (days) | %d |\n", max(lags)))
	}
	sb.WriteString("\n")

	sb.WriteString("## Incidents by Category\n\n")
	sb.WriteString("| Category | Count | % |\n|----------|-------|---|\n")
	cats := []string{"ransomware", "data-leak", "supply-chain", "credential-theft", "other"}
	for _, cat := range cats {
		n := catCount[cat]
		sb.WriteString(fmt.Sprintf("| %s | %d | %.0f%% |\n", cat, n, pct(n, total)))
	}
	sb.WriteString("\n")

	sb.WriteString("## Incidents by Year\n\n")
	sb.WriteString("| Year | Count |\n|------|-------|\n")
	years := sortedKeys(yearCount)
	for _, y := range years {
		sb.WriteString(fmt.Sprintf("| %s | %d |\n", y, yearCount[y]))
	}
	sb.WriteString("\n")

	sb.WriteString("## Top Malware Families\n\n")
	sb.WriteString("| Malware | Incidents |\n|---------|----------|\n")
	for _, name := range topN(malwareCount, 15) {
		sb.WriteString(fmt.Sprintf("| %s | %d |\n", name, malwareCount[name]))
	}
	sb.WriteString("\n")

	sb.WriteString("## CVE / GHSA References\n\n")
	cves := sortedSet(cveSet)
	if len(cves) > 0 {
		sb.WriteString("```\n")
		for _, c := range cves {
			sb.WriteString(c + "\n")
		}
		sb.WriteString("```\n\n")
	}

	sb.WriteString("## Top Attack Vectors\n\n")
	sb.WriteString("| Attack Vector | Incidents |\n|--------------|----------|\n")
	for _, v := range topN(vectorCount, 15) {
		sb.WriteString(fmt.Sprintf("| %s | %d |\n", v, vectorCount[v]))
	}
	sb.WriteString("\n")

	sb.WriteString("## Incident Index\n\n")
	sb.WriteString("| File | Category | Breach Date | Malware | CVEs |\n")
	sb.WriteString("|------|----------|-------------|---------|------|\n")
	sorted := make([]Breach, len(breaches))
	copy(sorted, breaches)
	sort.Slice(sorted, func(i, j int) bool {
		return sorted[i].DateOfBreach > sorted[j].DateOfBreach
	})
	for _, b := range sorted {
		fname := filepath.Base(b.FilePath)
		dir := filepath.Base(filepath.Dir(b.FilePath))
		relPath := dir + "/" + fname
		cves := strings.Join(b.CVE, ", ")
		sb.WriteString(fmt.Sprintf("| [%s](%s) | %s | %s | %s | %s |\n",
			fname, relPath, b.Category, b.DateOfBreach, truncate(b.Malware, 30), truncate(cves, 40)))
	}
	sb.WriteString("\n")

	sb.WriteString("## Schema\n\n")
	sb.WriteString("Each YAML file captures:\n\n")
	sb.WriteString("```yaml\n")
	sb.WriteString("source_name: \"publication or organization name\"\n")
	sb.WriteString("source_url: \"direct URL to the report\"\n")
	sb.WriteString("date_of_breach: \"YYYY-MM-DD or YYYY-MM or YYYY\"\n")
	sb.WriteString("date_of_disclosure: \"YYYY-MM-DD or unknown\"\n")
	sb.WriteString("date_of_customer_notification: \"YYYY-MM-DD or unknown\"\n")
	sb.WriteString("category: \"ransomware | data-leak | supply-chain | credential-theft | other\"\n")
	sb.WriteString("initial_attack_vector: \"CWE-NNN: Description or free text\"\n")
	sb.WriteString("cve: [\"CVE-2021-44228\"]  # list, empty if none\n")
	sb.WriteString("vendor_product: \"Vendor Product Name\"\n")
	sb.WriteString("software_package: \"package-name\"\n")
	sb.WriteString("malware: \"MalwareName\"\n")
	sb.WriteString("supply_chain_claimed: false\n")
	sb.WriteString("notes: \"Additional context\"\n")
	sb.WriteString("```\n\n")

	sb.WriteString("## Folders\n\n")
	sb.WriteString("- `ransomware/` — ransomware incidents\n")
	sb.WriteString("- `data-leak/` — customer data exposure\n")
	sb.WriteString("- `supply-chain/` — supply chain attacks\n")
	sb.WriteString("- `credential-theft/` — credential compromise\n")
	sb.WriteString("- `other/` — uncategorized or multi-category\n")

	return sb.String()
}

func pct(n, total int) float64 {
	if total == 0 {
		return 0
	}
	return float64(n) / float64(total) * 100
}

func extractYear(date string) string {
	if len(date) >= 4 {
		y := date[:4]
		if y >= "2000" && y <= "2030" {
			return y
		}
	}
	return ""
}

func disclosureLagDays(breach, disclosure string) int {
	b := parseDate(breach)
	d := parseDate(disclosure)
	if b.IsZero() || d.IsZero() {
		return -1
	}
	lag := int(d.Sub(b).Hours() / 24)
	if lag < 0 {
		return -1
	}
	return lag
}

func parseDate(s string) time.Time {
	for _, layout := range []string{"2006-01-02", "2006-01", "2006"} {
		t, err := time.Parse(layout, s)
		if err == nil {
			return t
		}
	}
	return time.Time{}
}

func median(vals []int) int {
	if len(vals) == 0 {
		return 0
	}
	sorted := make([]int, len(vals))
	copy(sorted, vals)
	sort.Ints(sorted)
	return sorted[len(sorted)/2]
}

func max(vals []int) int {
	m := 0
	for _, v := range vals {
		if v > m {
			m = v
		}
	}
	return m
}

func topN(m map[string]int, n int) []string {
	type kv struct{ k string; v int }
	var pairs []kv
	for k, v := range m {
		pairs = append(pairs, kv{k, v})
	}
	sort.Slice(pairs, func(i, j int) bool {
		if pairs[i].v != pairs[j].v {
			return pairs[i].v > pairs[j].v
		}
		return pairs[i].k < pairs[j].k
	})
	var keys []string
	for i, p := range pairs {
		if i >= n {
			break
		}
		keys = append(keys, p.k)
	}
	return keys
}

func sortedKeys(m map[string]int) []string {
	var keys []string
	for k := range m {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	return keys
}

func sortedSet(m map[string]bool) []string {
	var keys []string
	for k := range m {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	return keys
}

func normalizeMalware(s string) string {
	s = strings.TrimSpace(s)
	// Strip trailing descriptors like "ransomware", "malware", "group", "gang"
	for _, suffix := range []string{" ransomware", " malware", " group", " gang", " RAT"} {
		s = strings.TrimSuffix(s, suffix)
	}
	return s
}

func truncate(s string, n int) string {
	if len(s) <= n {
		return s
	}
	return s[:n-1] + "…"
}
