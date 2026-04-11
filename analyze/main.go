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
	Blockchain               string   `yaml:"blockchain"`
	FinancialLossUSD         float64  `yaml:"financial_loss_usd"`
	FinancialRecoveredUSD    float64  `yaml:"financial_recovered_usd"`
	AffectedCount            int64    `yaml:"affected_count"`
	AIModelName              string   `yaml:"ai_model_name"`
	AIModelProvider          string   `yaml:"ai_model_provider"`
	AIAttackVector           string   `yaml:"ai_attack_vector"`
	CloudProvider            string   `yaml:"cloud_provider"`
	CloudSharedResponsibility string  `yaml:"cloud_shared_responsibility"`
	CloudResourceCRIT        string   `yaml:"cloud_resource_crit"`
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
	categories := []string{"ransomware", "data-leak", "supply-chain", "credential-theft", "ai", "cloud", "cryptocurrency", "other"}
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
	cats := []string{"ransomware", "data-leak", "supply-chain", "credential-theft", "ai", "cloud", "cryptocurrency", "other"}
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

	sb.WriteString("## Schema\n\n")
	sb.WriteString("Each YAML file captures (see [`schema.yaml`](schema.yaml) for the canonical definition):\n\n")
	sb.WriteString("```yaml\n")
	sb.WriteString("# ── Core fields (always present) ───────────────────────────────────────────────\n")
	sb.WriteString("source_name: \"Publication or organization reporting the breach\"\n")
	sb.WriteString("source_url: \"https://example.com/direct-link-to-report\"\n")
	sb.WriteString("date_of_breach: \"YYYY-MM-DD\"          # also accepts YYYY-MM or YYYY\n")
	sb.WriteString("date_of_disclosure: \"YYYY-MM-DD\"      # empty string \"\" if unknown\n")
	sb.WriteString("category: \"ransomware | data-leak | supply-chain | credential-theft | ai | cloud | cryptocurrency | other\"\n")
	sb.WriteString("notes: \"Narrative summary of the incident including timeline, scope, threat actor attribution, and any known impact.\"\n")
	sb.WriteString("\n")
	sb.WriteString("# ── Traditional breach fields ───────────────────────────────────────────────────\n")
	sb.WriteString("date_of_customer_notification: \"\"     # YYYY-MM-DD or \"\" if unknown\n")
	sb.WriteString("initial_attack_vector: \"CWE-NNN: Short description, or free-text description of the attack method\"\n")
	sb.WriteString("cve: []                               # list of CVE/GHSA IDs, e.g. [\"CVE-2024-3094\"], empty if none\n")
	sb.WriteString("vendor_product: \"Vendor Product Name\" # affected vendor or product\n")
	sb.WriteString("software_package: \"\"                  # package name for software supply chain incidents, \"\" otherwise\n")
	sb.WriteString("malware: \"\"                           # malware family name if identified, \"\" otherwise\n")
	sb.WriteString("supply_chain_claimed: false           # true if a third-party vendor relationship was the attack vector\n")
	sb.WriteString("\n")
	sb.WriteString("# ── Crypto / Web3 fields ───────────────────────────────────────────────────────\n")
	sb.WriteString("blockchain: \"ethereum\"                # blockchain(s) involved, e.g. \"ethereum, solana\"; omit if not applicable\n")
	sb.WriteString("financial_loss_usd: 0                 # numeric USD value of funds lost; omit if not applicable\n")
	sb.WriteString("financial_recovered_usd: 0           # numeric USD value recovered after the incident; omit if not applicable\n")
	sb.WriteString("affected_count: 0                    # number of affected wallets, users, or individuals; omit if not applicable\n")
	sb.WriteString("\n")
	sb.WriteString("# ── AI fields ─────────────────────────────────────────────────────────────────\n")
	sb.WriteString("ai_model_name: \"\"                    # AI model involved, e.g. \"ChatGPT\", \"Claude\", \"Gemini\"; omit if not applicable\n")
	sb.WriteString("ai_model_provider: \"\"                # organization behind the model, e.g. \"OpenAI\", \"Anthropic\"; omit if not applicable\n")
	sb.WriteString("ai_attack_vector: \"\"                 # AI-specific attack method, e.g. \"prompt injection\", \"deepfake\"; omit if not applicable\n")
	sb.WriteString("\n")
	sb.WriteString("# ── Cloud / SaaS fields ───────────────────────────────────────────────────────\n")
	sb.WriteString("cloud_provider: \"\"                   # cloud provider, e.g. \"AWS\", \"Azure\", \"GCP\", \"Snowflake\"; omit if not applicable\n")
	sb.WriteString("cloud_shared_responsibility: \"\"      # \"vendor\" | \"customer\" | \"shared\" | \"unknown\"\n")
	sb.WriteString("cloud_resource_crit: \"\"              # CRIT identifier, e.g. \"arn:aws:s3:::{bucket}\"; omit if not applicable\n")
	sb.WriteString("```\n\n")

	sb.WriteString("## Folders\n\n")
	sb.WriteString("- `ransomware/` — ransomware incidents\n")
	sb.WriteString("- `data-leak/` — customer data exposure\n")
	sb.WriteString("- `supply-chain/` — supply chain attacks\n")
	sb.WriteString("- `credential-theft/` — credential compromise\n")
	sb.WriteString("- `ai/` — AI-related cybersecurity incidents\n")
	sb.WriteString("- `cloud/` — cloud and SaaS security incidents\n")
	sb.WriteString("- `cryptocurrency/` — cryptocurrency, DeFi, and Web3 incidents\n")
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
