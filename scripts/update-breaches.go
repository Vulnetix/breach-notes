package main

import (
	"fmt"
	"math"
	"os"
	"path/filepath"
	"sort"
	"strconv"
	"strings"
	"time"

	"gopkg.in/yaml.v3"
)

// Breach holds every field supported by schema.yaml.
type Breach struct {
	// Core
	SourceName       string `yaml:"source_name"`
	SourceURL        string `yaml:"source_url"`
	DateOfBreach     string `yaml:"date_of_breach"`
	DateOfDisclosure string `yaml:"date_of_disclosure"`
	Category         string `yaml:"category"`
	Notes            string `yaml:"notes"`

	// Traditional breach
	DateOfCustomerNotification string   `yaml:"date_of_customer_notification"`
	InitialAttackVector        string   `yaml:"initial_attack_vector"`
	CVE                        []string `yaml:"cve"`
	VendorProduct              string   `yaml:"vendor_product"`
	SoftwarePackage            string   `yaml:"software_package"`
	Malware                    string   `yaml:"malware"`
	SupplyChainClaimed         bool     `yaml:"supply_chain_claimed"`

	// Crypto / Web3
	Blockchain           string  `yaml:"blockchain"`
	FinancialLossUSD     float64 `yaml:"financial_loss_usd"`
	FinancialRecoveredUSD float64 `yaml:"financial_recovered_usd"`
	AffectedCount        int64   `yaml:"affected_count"`

	// AI
	AIModelName     string `yaml:"ai_model_name"`
	AIModelProvider string `yaml:"ai_model_provider"`
	AIAttackVector  string `yaml:"ai_attack_vector"`
}

type record struct {
	breach Breach
	file   string // relative path, e.g. "ransomware/2024-02_change-healthcare.yaml"
	date   time.Time
}

var dirs = []string{"ransomware", "data-leak", "supply-chain", "credential-theft", "ai", "cryptocurrency", "other"}

func main() {
	records, err := loadAll()
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	// Sort newest-first for the incident index and recent-breaches output.
	sort.Slice(records, func(i, j int) bool {
		return records[i].date.After(records[j].date)
	})

	if err := writeRecentBreaches(records); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	if err := updateREADME(records); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	fmt.Printf("Done. Processed %d breach records.\n", len(records))
}

// ── I/O helpers ───────────────────────────────────────────────────────────────

func loadAll() ([]record, error) {
	var records []record
	for _, dir := range dirs {
		files, err := filepath.Glob(filepath.Join(dir, "*.yaml"))
		if err != nil {
			return nil, fmt.Errorf("glob %s: %w", dir, err)
		}
		for _, file := range files {
			data, err := os.ReadFile(file)
			if err != nil {
				fmt.Printf("WARN: reading %s: %v\n", file, err)
				continue
			}
			var b Breach
			if err := yaml.Unmarshal(data, &b); err != nil {
				fmt.Printf("WARN: parsing %s: %v\n", file, err)
				continue
			}
			d, err := parseDate(b.DateOfBreach)
			if err != nil {
				fmt.Printf("WARN: date in %s: %v\n", file, err)
				continue
			}
			records = append(records, record{breach: b, file: file, date: d})
		}
	}
	return records, nil
}

func parseDate(s string) (time.Time, error) {
	for _, layout := range []string{"2006-01-02", "2006-01", "2006"} {
		if t, err := time.Parse(layout, s); err == nil {
			return t, nil
		}
	}
	return time.Time{}, fmt.Errorf("cannot parse %q as date", s)
}

// ── recent-breaches.yaml ──────────────────────────────────────────────────────

func writeRecentBreaches(records []record) error {
	top := records
	if len(top) > 10 {
		top = top[:10]
	}

	recent := make([]map[string]interface{}, len(top))
	for i, r := range top {
		b := r.breach
		recent[i] = map[string]interface{}{
			"source_name":            b.SourceName,
			"source_url":             b.SourceURL,
			"date_of_breach":         b.DateOfBreach,
			"date_of_disclosure":     b.DateOfDisclosure,
			"category":               b.Category,
			"initial_attack_vector":  b.InitialAttackVector,
			"cve":                    b.CVE,
			"vendor_product":         b.VendorProduct,
			"software_package":       b.SoftwarePackage,
			"malware":                b.Malware,
			"supply_chain_claimed":   b.SupplyChainClaimed,
			"blockchain":             b.Blockchain,
			"financial_loss_usd":     b.FinancialLossUSD,
			"financial_recovered_usd": b.FinancialRecoveredUSD,
			"affected_count":         b.AffectedCount,
			"ai_model_name":          b.AIModelName,
			"ai_model_provider":      b.AIModelProvider,
			"ai_attack_vector":       b.AIAttackVector,
			"notes":                  b.Notes,
		}
	}

	out := map[string]interface{}{
		"recent_breaches": recent,
		"updated_at":      time.Now().Format("2006-01-02 15:04:05"),
	}

	raw, err := yaml.Marshal(out)
	if err != nil {
		return fmt.Errorf("marshal recent-breaches: %w", err)
	}

	os.MkdirAll("data", 0o755)
	if err := os.WriteFile("data/recent-breaches.yaml", raw, 0o644); err != nil {
		return fmt.Errorf("write recent-breaches: %w", err)
	}
	fmt.Printf("Wrote data/recent-breaches.yaml (%d entries)\n", len(top))
	return nil
}

// ── README generation ─────────────────────────────────────────────────────────

const beginMarker = "<!-- BEGIN GENERATED -->"
const endMarker = "<!-- END GENERATED -->"

func updateREADME(records []record) error {
	path := "README.md"
	raw, err := os.ReadFile(path)
	if err != nil {
		return fmt.Errorf("read README: %w", err)
	}
	content := string(raw)

	start := strings.Index(content, beginMarker)
	end := strings.Index(content, endMarker)
	if start == -1 || end == -1 {
		return fmt.Errorf("README missing %s / %s markers", beginMarker, endMarker)
	}
	end += len(endMarker)

	generated := beginMarker + "\n" + buildREADMEBody(records) + "\n" + endMarker
	updated := content[:start] + generated + content[end:]

	if err := os.WriteFile(path, []byte(updated), 0o644); err != nil {
		return fmt.Errorf("write README: %w", err)
	}
	fmt.Println("Updated README.md")
	return nil
}

func buildREADMEBody(records []record) string {
	var sb strings.Builder
	total := len(records)
	now := time.Now().Format("2006-01-02")

	// ── header ────────────────────────────────────────────────────────────────
	sb.WriteString(fmt.Sprintf("**Last updated:** %s  **Total records:** %d\n\n", now, total))
	sb.WriteString("---\n\n")

	// ── Summary Statistics ────────────────────────────────────────────────────
	sb.WriteString("## Summary Statistics\n\n")
	sb.WriteString("| Metric | Value |\n|--------|-------|\n")

	sb.WriteString(fmt.Sprintf("| Total incidents | %d |\n", total))

	// CVE stats
	withCVE, uniqueCVEs := cveStats(records)
	pct := pctOf(withCVE, total)
	sb.WriteString(fmt.Sprintf("| With CVE/GHSA references | %d (%s) |\n", withCVE, pct))
	sb.WriteString(fmt.Sprintf("| Unique CVEs/GHSAs | %d |\n", uniqueCVEs))

	// Malware
	withMalware := countWhere(records, func(r record) bool { return r.breach.Malware != "" })
	sb.WriteString(fmt.Sprintf("| With malware identified | %d (%s) |\n", withMalware, pctOf(withMalware, total)))

	// Supply chain
	supplyChain := countWhere(records, func(r record) bool { return r.breach.SupplyChainClaimed })
	sb.WriteString(fmt.Sprintf("| Supply chain claimed | %d (%s) |\n", supplyChain, pctOf(supplyChain, total)))

	// Unique vendor products
	uniqueVendors := uniqueNonEmpty(records, func(r record) string { return r.breach.VendorProduct })
	sb.WriteString(fmt.Sprintf("| Unique vendor products | %d |\n", uniqueVendors))

	// Disclosure lag
	medLag, maxLag := disclosureLag(records)
	sb.WriteString(fmt.Sprintf("| Median disclosure lag (days) | %d |\n", medLag))
	sb.WriteString(fmt.Sprintf("| Max disclosure lag (days) | %d |\n", maxLag))

	// Financial loss
	withLoss := countWhere(records, func(r record) bool { return r.breach.FinancialLossUSD > 0 })
	sb.WriteString(fmt.Sprintf("| Incidents with financial loss data | %d (%s) |\n", withLoss, pctOf(withLoss, total)))

	totalLoss := sumFloat(records, func(r record) float64 { return r.breach.FinancialLossUSD })
	sb.WriteString(fmt.Sprintf("| Total financial loss (USD) | %s |\n", formatUSD(totalLoss)))

	totalRecovered := sumFloat(records, func(r record) float64 { return r.breach.FinancialRecoveredUSD })
	sb.WriteString(fmt.Sprintf("| Total financial recovered (USD) | %s |\n", formatUSD(totalRecovered)))

	// Blockchain / crypto
	withBlockchain := countWhere(records, func(r record) bool { return r.breach.Blockchain != "" })
	sb.WriteString(fmt.Sprintf("| Crypto / Web3 incidents | %d (%s) |\n", withBlockchain, pctOf(withBlockchain, total)))

	// Affected count
	withAffected := countWhere(records, func(r record) bool { return r.breach.AffectedCount > 0 })
	totalAffected := int64(0)
	for _, r := range records {
		totalAffected += r.breach.AffectedCount
	}
	sb.WriteString(fmt.Sprintf("| Incidents with affected-count data | %d (%s) |\n", withAffected, pctOf(withAffected, total)))
	if totalAffected > 0 {
		sb.WriteString(fmt.Sprintf("| Total affected (wallets / users) | %s |\n", formatCount(totalAffected)))
	}

	sb.WriteString("\n")

	// ── Incidents by Category ─────────────────────────────────────────────────
	sb.WriteString("## Incidents by Category\n\n")
	sb.WriteString("| Category | Count | % |\n|----------|-------|---|\n")
	catCounts := groupBy(records, func(r record) string { return r.breach.Category })
	catOrder := []string{"ransomware", "data-leak", "supply-chain", "credential-theft", "ai", "cryptocurrency", "other"}
	for _, cat := range catOrder {
		n := catCounts[cat]
		sb.WriteString(fmt.Sprintf("| %s | %d | %s |\n", cat, n, pctOf(n, total)))
	}
	sb.WriteString("\n")

	// ── Incidents by Year ─────────────────────────────────────────────────────
	sb.WriteString("## Incidents by Year\n\n")
	sb.WriteString("| Year | Count |\n|------|-------|\n")
	yearCounts := map[int]int{}
	for _, r := range records {
		yearCounts[r.date.Year()]++
	}
	years := make([]int, 0, len(yearCounts))
	for y := range yearCounts {
		years = append(years, y)
	}
	sort.Ints(years)
	for _, y := range years {
		sb.WriteString(fmt.Sprintf("| %d | %d |\n", y, yearCounts[y]))
	}
	sb.WriteString("\n")

	// ── Top Malware Families ──────────────────────────────────────────────────
	sb.WriteString("## Top Malware Families\n\n")
	sb.WriteString("| Malware | Incidents |\n|---------|----------|\n")
	malwareCounts := map[string]int{}
	for _, r := range records {
		if r.breach.Malware != "" {
			malwareCounts[r.breach.Malware]++
		}
	}
	for _, row := range topN(malwareCounts, 15) {
		sb.WriteString(fmt.Sprintf("| %s | %d |\n", row.key, row.count))
	}
	sb.WriteString("\n")

	// ── CVE / GHSA References ─────────────────────────────────────────────────
	sb.WriteString("## CVE / GHSA References\n\n```\n")
	allCVEs := map[string]bool{}
	for _, r := range records {
		for _, cve := range r.breach.CVE {
			allCVEs[cve] = true
		}
	}
	sortedCVEs := make([]string, 0, len(allCVEs))
	for cve := range allCVEs {
		sortedCVEs = append(sortedCVEs, cve)
	}
	sort.Strings(sortedCVEs)
	for _, cve := range sortedCVEs {
		sb.WriteString(cve + "\n")
	}
	sb.WriteString("```\n\n")

	// ── Top Attack Vectors ────────────────────────────────────────────────────
	sb.WriteString("## Top Attack Vectors\n\n")
	sb.WriteString("| Attack Vector | Incidents |\n|--------------|----------|\n")
	vectorCounts := map[string]int{}
	for _, r := range records {
		v := r.breach.InitialAttackVector
		if v == "" || strings.ToLower(v) == "unknown" {
			continue
		}
		// Normalise: strip CWE prefix label variations, keep key phrase
		vectorCounts[v]++
	}
	for _, row := range topN(vectorCounts, 15) {
		sb.WriteString(fmt.Sprintf("| %s | %d |\n", row.key, row.count))
	}
	sb.WriteString("\n")

	// ── Top Blockchains ───────────────────────────────────────────────────────
	if withBlockchain > 0 {
		sb.WriteString("## Top Blockchains\n\n")
		sb.WriteString("| Blockchain | Incidents | Financial Loss |\n|------------|-----------|----------------|\n")
		chainCounts := map[string]int{}
		chainLoss := map[string]float64{}
		for _, r := range records {
			if r.breach.Blockchain == "" {
				continue
			}
			for _, chain := range splitChains(r.breach.Blockchain) {
				chainCounts[chain]++
				chainLoss[chain] += r.breach.FinancialLossUSD
			}
		}
		for _, row := range topN(chainCounts, 15) {
			loss := chainLoss[row.key]
			lossStr := ""
			if loss > 0 {
				lossStr = formatUSD(loss)
			}
			sb.WriteString(fmt.Sprintf("| %s | %d | %s |\n", row.key, row.count, lossStr))
		}
		sb.WriteString("\n")
	}

	return sb.String()
}

// ── Statistics helpers ────────────────────────────────────────────────────────

func cveStats(records []record) (withCVE, uniqueCVEs int) {
	seen := map[string]bool{}
	for _, r := range records {
		if len(r.breach.CVE) > 0 {
			withCVE++
		}
		for _, c := range r.breach.CVE {
			seen[c] = true
		}
	}
	return withCVE, len(seen)
}

func countWhere(records []record, fn func(record) bool) int {
	n := 0
	for _, r := range records {
		if fn(r) {
			n++
		}
	}
	return n
}

func uniqueNonEmpty(records []record, fn func(record) string) int {
	seen := map[string]bool{}
	for _, r := range records {
		if v := fn(r); v != "" {
			seen[v] = true
		}
	}
	return len(seen)
}

func sumFloat(records []record, fn func(record) float64) float64 {
	total := 0.0
	for _, r := range records {
		total += fn(r)
	}
	return total
}

func disclosureLag(records []record) (median, max int) {
	var lags []int
	for _, r := range records {
		disc := r.breach.DateOfDisclosure
		if disc == "" || strings.ToLower(disc) == "unknown" {
			continue
		}
		dt, err := parseDate(disc)
		if err != nil {
			continue
		}
		lag := int(dt.Sub(r.date).Hours() / 24)
		if lag < 0 {
			lag = 0
		}
		lags = append(lags, lag)
		if lag > max {
			max = lag
		}
	}
	if len(lags) == 0 {
		return 0, 0
	}
	sort.Ints(lags)
	return lags[len(lags)/2], max
}

func groupBy(records []record, fn func(record) string) map[string]int {
	m := map[string]int{}
	for _, r := range records {
		m[fn(r)]++
	}
	return m
}

type kv struct {
	key   string
	count int
}

func topN(m map[string]int, n int) []kv {
	all := make([]kv, 0, len(m))
	for k, v := range m {
		all = append(all, kv{k, v})
	}
	sort.Slice(all, func(i, j int) bool {
		if all[i].count != all[j].count {
			return all[i].count > all[j].count
		}
		return all[i].key < all[j].key
	})
	if n > len(all) {
		n = len(all)
	}
	return all[:n]
}

func splitChains(s string) []string {
	parts := strings.Split(s, ",")
	out := make([]string, 0, len(parts))
	for _, p := range parts {
		p = strings.TrimSpace(p)
		if p != "" {
			out = append(out, p)
		}
	}
	return out
}

// ── Formatting helpers ────────────────────────────────────────────────────────

func pctOf(n, total int) string {
	if total == 0 {
		return "0%"
	}
	return strconv.Itoa(int(math.Round(float64(n)/float64(total)*100))) + "%"
}

func formatUSD(v float64) string {
	if v == 0 {
		return ""
	}
	switch {
	case v >= 1e12:
		return fmt.Sprintf("$%.1fT", v/1e12)
	case v >= 1e9:
		return fmt.Sprintf("$%.1fB", v/1e9)
	case v >= 1e6:
		return fmt.Sprintf("$%.1fM", v/1e6)
	case v >= 1e3:
		return fmt.Sprintf("$%.0fK", v/1e3)
	default:
		return fmt.Sprintf("$%.0f", v)
	}
}

func formatCount(n int64) string {
	switch {
	case n >= 1_000_000_000:
		return fmt.Sprintf("%.1fB", float64(n)/1e9)
	case n >= 1_000_000:
		return fmt.Sprintf("%.1fM", float64(n)/1e6)
	case n >= 1_000:
		return fmt.Sprintf("%.0fK", float64(n)/1e3)
	default:
		return strconv.FormatInt(n, 10)
	}
}

