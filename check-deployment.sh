#!/bin/bash

# Script to check GitHub Pages deployment status

set -e

GITHUB_TOKEN=$(cat /home/pllanos/entropy/legal_docs/.secret | cut -d= -f2)
REPO_OWNER="Auditaiadmin"
REPO_NAME="legal"

echo "Checking GitHub Pages deployment status..."
echo ""

# Get latest build status
BUILD_INFO=$(curl -s -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer ${GITHUB_TOKEN}" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  "https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/pages/builds/latest")

STATUS=$(echo "$BUILD_INFO" | grep -o '"status":"[^"]*"' | cut -d'"' -f4)
ERROR=$(echo "$BUILD_INFO" | grep -o '"message":[^,}]*' | cut -d':' -f2)

if [ "$STATUS" = "built" ]; then
    echo "✓ Deployment Status: SUCCESS"
    echo ""
    echo "Your site is live at:"
    echo "https://auditaiadmin.github.io/legal/"
    echo ""
elif [ "$STATUS" = "building" ]; then
    echo "⏳ Deployment Status: IN PROGRESS"
    echo ""
    echo "The site is currently being built. Please wait a few moments and check again."
    echo ""
elif [ "$STATUS" = "errored" ]; then
    echo "✗ Deployment Status: FAILED"
    echo "Error: $ERROR"
    echo ""
else
    echo "Status: $STATUS"
    echo ""
fi

# Get pages info
PAGES_INFO=$(curl -s -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer ${GITHUB_TOKEN}" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  "https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/pages")

BUILD_TYPE=$(echo "$PAGES_INFO" | grep -o '"build_type":"[^"]*"' | cut -d'"' -f4)
SOURCE_BRANCH=$(echo "$PAGES_INFO" | grep -o '"branch":"[^"]*"' | cut -d'"' -f4)

echo "Configuration:"
echo "- Build Type: $BUILD_TYPE"
echo "- Source Branch: $SOURCE_BRANCH"
echo "- URL: https://auditaiadmin.github.io/legal/"
