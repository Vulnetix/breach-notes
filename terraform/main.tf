terraform {
  required_version = ">= 1.0.0"
  required_providers {
    cloudflare = {
      source  = "cloudflare/cloudflare"
      version = "~> 4.0"
    }
  }
}

provider "cloudflare" {
  api_token = var.cloudflare_api_token
}

# DNS CNAME for GitHub Pages — must NOT be proxied for GH Pages custom domain verification
resource "cloudflare_record" "breachnotes" {
  zone_id = var.cloudflare_zone_id
  name    = "breachnotes"
  content = "vulnetix.github.io"
  type    = "CNAME"
  ttl     = 1 # auto when not proxied
  proxied = false
}

# Redirect www → apex
resource "cloudflare_record" "breachnotes_www" {
  zone_id = var.cloudflare_zone_id
  name    = "www.breachnotes"
  content = "vulnetix.github.io"
  type    = "CNAME"
  ttl     = 1
  proxied = false
}

output "breachnotes_fqdn" {
  value = cloudflare_record.breachnotes.hostname
}
