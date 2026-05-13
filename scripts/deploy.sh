#!/usr/bin/env bash
# Run from project root: bash scripts/deploy.sh
set -e
cd "$(dirname "$0")/.."

echo "→ processing CSVs..."
python scripts/process.py

echo "→ committing..."
git add public/
git commit -m "feed update $(date -u +%Y-%m-%dT%H:%M:%SZ)" || echo "  nothing to commit"

echo "→ pushing..."
git push

echo "✓ done. Vercel/Cloudflare will redeploy in ~30s."
