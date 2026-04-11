#!/usr/bin/env bash
# Validate that every generated RSS/XML feed is well-formed XML.
# Used by both the pre-commit hook and the GitHub Action.
#
# Requirements: hugo, xmllint (libxml2-utils)
set -euo pipefail

# ── Check prerequisites ──────────────────────────────────────────────────────

for cmd in hugo xmllint; do
  if ! command -v "$cmd" &>/dev/null; then
    echo "SKIP: $cmd not found — install it to enable RSS validation" >&2
    exit 0
  fi
done

# ── Build site ────────────────────────────────────────────────────────────────

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
BUILD_DIR="$(mktemp -d)"
trap 'rm -rf "$BUILD_DIR"' EXIT

echo "Building Hugo site into $BUILD_DIR ..."
hugo --source "$REPO_ROOT" --destination "$BUILD_DIR" --quiet 2>&1

# ── Validate every XML file ──────────────────────────────────────────────────

errors=0
checked=0
while IFS= read -r -d '' xml_file; do
  checked=$((checked + 1))
  if ! xmllint --noout "$xml_file" 2>/tmp/rss-lint-err; then
    echo "FAIL: $xml_file"
    cat /tmp/rss-lint-err
    errors=$((errors + 1))
  fi
done < <(find "$BUILD_DIR" -name '*.xml' -print0)

echo "Checked $checked XML file(s) — $errors error(s)"
if [ "$errors" -gt 0 ]; then
  exit 1
fi
