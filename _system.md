# Breach Notes System Documentation

## Overview

Breach Notes is a comprehensive system for documenting, organizing, and presenting cybersecurity breach incidents. It combines structured YAML data storage with a modern Hugo-powered static site featuring a hacker-inspired theme, automated updates, and custom domain configuration via Cloudflare.

## System Components

### 1. Data Layer

#### Structure
- **Format**: YAML files organized by incident category
- **Categories**: 
  - `ransomware/` - Ransomware attacks
  - `data-leak/` - Data exposure incidents
  - `supply-chain/` - Supply chain compromises
  - `credential-theft/` - Credential theft incidents
  - `other/` - Miscellaneous or multi-category incidents

#### Schema
Each incident file follows this structure:
```yaml
source_name: "Publication or organization name"
source_url: "Direct URL to the report"
date_of_breach: "YYYY-MM-DD or YYYY-MM or YYYY"
date_of_disclosure: "YYYY-MM-DD or unknown"
date_of_customer_notification: "YYYY-MM-DD or unknown"
category: "ransomware | data-leak | supply-chain | credential-theft | other"
initial_attack_vector: "CWE-NNN: Description or free text"
cve: ["CVE-2021-44228"]  # list, empty if none
vendor_product: "Vendor Product Name"
software_package: "package-name"
malware: "MalwareName"
supply_chain_claimed: false
notes: "Additional context"
```

#### Storage
- Original YAML files maintained in category directories for version control
- Symlinked copies in `data/` directory for Hugo processing
- Auto-generated `data/recent-breaches.yaml` containing the 10 most recent incidents

### 2. Presentation Layer (Hugo Site)

#### Technology Stack
- **Static Site Generator**: Hugo v0.160.0+
- **Theme**: Custom hacker-themed design
- **Icons**: Iconfy CSS library
- **Styling**: Custom CSS with terminal/green-on-black aesthetic
- **Interactivity**: JavaScript for animated effects

#### Templates
- **Base Layout** (`layouts/_default/baseof.html`): Core HTML structure with asset loading
- **Homepage** (`layouts/index.html`): Shows 10 most recent breaches + statistics
- **Section Pages** (`layouts/_default/section.html`): Lists breaches by category
- **Single Pages** (`layouts/_default/single.html`): Displays full breach details
- **Partials** (`layouts/partials/`): Reusable components (page headers, etc.)

#### Features
- **Hacker Theme Elements**:
  - Matrix-style code rain background
  - Binary rain animations
  - Circuit board patterns
  - Terminal cursor blinking effects
  - Glitch text effects on headings
  - Hover effects on links
- **Icon Integration**: Iconfy icons throughout the interface
- **Responsive Design**: Mobile-friendly layouts
- **Accessibility**: Proper semantic HTML and ARIA considerations
- **Performance**: Optimized CSS and minimal JavaScript

### 3. Automation Layer

#### GitHub Actions Workflow
- **File**: `.github/workflows/update-homepage.yml`
- **Trigger**: Hourly schedule (`0 * * * *`) + manual dispatch
- **Job**: `update-homepage`
- **Steps**:
  1. Checkout repository
  2. Setup Go environment
  3. Build Go update program
  4. Run update script to find recent breaches
  5. Commit and push changes (if any)

#### Update Mechanism
- **Go Program**: `scripts/update-breaches.go`
- **Function**: 
  - Scans all YAML files in category directories
  - Parses breach dates (handles YYYY-MM-DD, YYYY-MM, YYYY formats)
  - Sorts incidents by date (newest first)
  - Selects top 10 most recent breaches
  - Generates `data/recent-breaches.yaml` with structured data
- **Output**: YAML file consumed by Hugo homepage template

### 4. Infrastructure Layer

#### GitHub Pages
- **Hosting**: GitHub Pages via GitHub Actions build
- **Build Process**: Hugo static site generation
- **Output**: Static HTML/CSS/JS files served from `gh-pages` branch or `docs/` folder

#### Cloudflare Configuration (Terraform)
- **Provider**: Cloudflare
- **Resources**:
  - DNS CNAME record: `breachnotes.vulnetix.com` → GitHub Pages domain
  - Optional: Page rule for www redirect
  - SSL/TLS: Managed by Cloudflare proxy
- **Files**:
  - `terraform/main.tf`: Core configuration
  - `terraform/variables.tf`: Configurable parameters
- **Usage**:
  ```bash
  cd terraform
  terraform init
  terraform apply
  ```

### 5. Development Setup

#### Prerequisites
- Hugo Extended version (for Sass/SCSS support)
- Go 1.21+ (for update script)
- Git
- Optional: Terraform for Cloudflare management

#### Local Development
```bash
# Clone repository
git clone https://github.com/chris/breach-notes.git
cd breach-notes

# Install dependencies (if using package manager)
# hugo, go, etc.

# Start development server
hugo server --buildDrafts

# Visit http://localhost:1313
```

#### Building for Production
```bash
hugo --minify
# Output generated in ./public/ directory
```

## Data Flow

1. **Data Entry**: Contributors add YAML files to appropriate category directories
2. **Version Control**: Changes tracked via Git
3. **Automated Updates**: 
   - Hourly GitHub Actions workflow runs
   - Go script processes all YAML files
   - Updates `data/recent-breaches.yaml`
   - Commits changes back to repository
4. **Site Generation**: 
   - Hugo reads YAML data from `data/` directory
   - Generates static HTML pages
   - Deploys to GitHub Pages
5. **Presentation**: 
   - Users access site via `breachnotes.vulnetix.com`
   - Hacker-themed interface displays breach information
   - Navigation by category, search via browser, detailed views

## Security & Maintenance

### Data Integrity
- YAML format ensures structured, parseable data
- Symlink approach preserves original files while enabling Hugo processing
- Automated validation through Hugo build process

### Update Reliability
- GitHub Actions workflow includes error handling
- Go script validates YAML parsing and date formats
- Failed updates don't break existing site (uses last good data)
- Manual workflow dispatch available for immediate updates

### Infrastructure
- Cloudflare provides DDoS protection, SSL/TLS, and caching
- GitHub Pages offers reliable static site hosting
- Terraform enables infrastructure-as-code for DNS management

## Metrics & Statistics

The system automatically calculates and displays:
- Total incidents by category and year
- Malware family distribution
- CVE/GHSA reference counts
- Attack vector analysis
- Median/maximum disclosure lag times

These statistics are compiled from the README.md file which is maintained separately from the incident data.

## Extensibility

### Adding New Features
1. **New Data Fields**: Extend YAML schema and update templates
2. **Additional Views**: Create new layout files in `layouts/`
3. **Enhanced Styling**: Modify CSS files in `assets/css/`
4. **New Automation**: Add scripts and update GitHub workflow
5. **Alternative Deployments**: Modify `config.toml` for different hosts

### Categories
New categories can be added by:
1. Creating directory in root
2. Adding symlink in `data/` directory
3. Creating `_index.md` in `content/` for section page
4. Adding menu item in `hugo.toml`
5. Updating templates to handle new category if needed

## Contribution Guidelines

### Adding Breach Incidents
1. Determine appropriate category based on incident type
2. Create YAML file named: `YYYY-MM-DD_descriptive-name.yaml`
3. Populate all relevant fields using the schema above
4. Ensure `source_url` points to authoritative source
5. Submit pull request with clear description

### Code Contributions
1. Fork repository
2. Create feature branch
3. Make changes
4. Ensure local site builds correctly: `hugo server`
5. Test updates with: `go run scripts/update-breaches.go`
6. Submit pull request

## License

- **Data**: Factual information from public reports (no copyright claimed)
- **Site Design & Code**: MIT License
- **Documentation**: CC BY 4.0
- **Iconfy Icons**: Used per their licensing terms

## Contact & Support

For questions, issues, or contributions:
- GitHub Issues: https://github.com/chris/breach-notes/issues
- Pull Requests: Standard GitHub PR process
- Documentation: This file and README.md

---
*System generated and maintained as part of the Breach Notes project.*
*Last updated: $(date)*