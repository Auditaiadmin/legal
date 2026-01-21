#!/bin/bash

# Script to enable GitHub Pages for the repository

set -e

GITHUB_TOKEN=$(cat /home/pllanos/entropy/legal_docs/.secret | cut -d= -f2)
REPO_OWNER="Auditaiadmin"
REPO_NAME="legal"

echo "Enabling GitHub Pages for ${REPO_OWNER}/${REPO_NAME}..."

# Enable GitHub Pages with GitHub Actions as source
curl -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer ${GITHUB_TOKEN}" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  "https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/pages" \
  -d '{
    "source": {
      "branch": "main",
      "path": "/"
    },
    "build_type": "workflow"
  }'

echo ""
echo "GitHub Pages configuration:"
echo "- URL: https://${REPO_OWNER,,}.github.io/${REPO_NAME}/"
echo "- Source: GitHub Actions workflow"
echo ""
echo "The site should be available in a few minutes at:"
echo "https://auditaiadmin.github.io/legal/"
