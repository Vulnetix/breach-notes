package main

import (
	"fmt"
	"os"
	"path/filepath"
	"sort"
	"time"

	"gopkg.in/yaml.v3"
)

type Breach struct {
	SourceName        string   `yaml:"source_name"`
	SourceURL         string   `yaml:"source_url"`
	DateOfBreach      string   `yaml:"date_of_breach"`
	DateOfDisclosure  string   `yaml:"date_of_disclosure"`
	DateOfCustomerNotification string `yaml:"date_of_customer_notification"`
	Category          string   `yaml:"category"`
	InitialAttackVector string  `yaml:"initial_attack_vector"`
	CVE               []string `yaml:"cve"`
	VendorProduct     string   `yaml:"vendor_product"`
	SoftwarePackage   string   `yaml:"software_package"`
	Malware           string   `yaml:"malware"`
	SupplyChainClaimed bool    `yaml:"supply_chain_claimed"`
	Notes             string   `yaml:"notes"`
}

type BreachWithDate struct {
	Breach Breach
	Date   time.Time
}

func main() {
	// Directories to scan
	dirs := []string{
		"ransomware",
		"data-leak",
		"supply-chain",
		"credential-theft",
		"other",
	}

	var breaches []BreachWithDate

	// Scan each directory
	for _, dir := range dirs {
		files, err := filepath.Glob(filepath.Join(dir, "*.yaml"))
		if err != nil {
			fmt.Printf("Error globbing in %s: %v\n", dir, err)
			continue
		}

		for _, file := range files {
			data, err := os.ReadFile(file)
			if err != nil {
				fmt.Printf("Error reading %s: %v\n", file, err)
				continue
			}

			var breach Breach
			err = yaml.Unmarshal(data, &breach)
			if err != nil {
				fmt.Printf("Error parsing YAML in %s: %v\n", file, err)
				continue
			}

			// Parse date
			date, err := time.Parse("2006-01-02", breach.DateOfBreach)
			if err != nil {
				// Try with just year-month if day is missing
				date, err = time.Parse("2006-01", breach.DateOfBreach)
				if err != nil {
					// Try with just year
					date, err = time.Parse("2006", breach.DateOfBreach)
					if err != nil {
						fmt.Printf("Error parsing date in %s: %v\n", file, err)
						continue
					}
				}
			}

			breaches = append(breaches, BreachWithDate{Breach: breach, Date: date})
		}
	}

	// Sort by date (newest first)
	sort.Slice(breaches, func(i, j int) bool {
		return breaches[i].Date.After(breaches[j].Date)
	})

	// Take top 10
	if len(breaches) > 10 {
		breaches = breaches[:10]
	}

	// Create output data
	recentBreaches := make([]map[string]interface{}, len(breaches))
	for i, b := range breaches {
		recentBreaches[i] = map[string]interface{}{
			"source_name":        b.Breach.SourceName,
			"source_url":         b.Breach.SourceURL,
			"date_of_breach":     b.Breach.DateOfBreach,
			"date_of_disclosure": b.Breach.DateOfDisclosure,
			"category":           b.Breach.Category,
			"malware":            b.Breach.Malware,
			"cve":                b.Breach.CVE,
			"notes":              b.Breach.Notes,
		}
	}

	// Write to data file
	outputData := map[string]interface{}{
		"recent_breaches": recentBreaches,
		"updated_at":      time.Now().Format("2006-01-02 15:04:05"),
	}

	output, err := yaml.Marshal(outputData)
	if err != nil {
		fmt.Printf("Error marshaling YAML: %v\n", err)
		os.Exit(1)
	}

	// Ensure data directory exists
	os.MkdirAll("data", 0755)

	err = os.WriteFile("data/recent-breaches.yaml", output, 0644)
	if err != nil {
		fmt.Printf("Error writing file: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("Updated data/recent-breaches.yaml with %d recent breaches\n", len(breaches))
}