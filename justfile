# Breach Notes — task runner

# Default: show available recipes
default:
    @just --list

# Start Hugo dev server with drafts
dev:
    hugo server -D --bind 0.0.0.0

# Build the production site
build: sync-data generate-recent
    hugo --minify

# Sync YAML breach data into Hugo data directory
sync-data:
    mkdir -p data
    for cat in ransomware data-leak supply-chain credential-theft other; do \
        rm -rf "data/$cat"; \
        cp -r "$cat" "data/$cat"; \
    done

# Generate recent-breaches.yaml (top 10 latest)
generate-recent:
    go build -o update-breaches ./scripts/update-breaches.go
    ./update-breaches
    rm -f update-breaches

# Validate all YAML breach files
validate:
    cd scripts/validate && go run . ../../

# Run the Go analyzer to regenerate README stats
analyze:
    cd analyze && go run .

# Run full CI checks locally
check: validate build
    @echo "All checks passed"

# --- Terraform ---

# Initialize Terraform
tf-init:
    cd terraform && terraform init

# Plan Terraform changes (Cloudflare DNS)
tf-plan:
    cd terraform && terraform plan

# Apply Terraform changes
tf-apply:
    cd terraform && terraform apply

# Show current Terraform state
tf-show:
    cd terraform && terraform show

# --- Deployment ---

# Deploy: build and push (GHA handles actual deploy)
deploy: check
    @echo "Push to main to trigger GitHub Actions deploy"

# Clean build artifacts
clean:
    rm -rf public/ resources/_gen/ update-breaches
