#!/bin/bash

# Script to download Google Docs as HTML and PDF
# Usage: ./download_docs.sh

set -e

DOCS_DIR="docs"
PDF_DIR="pdf"

mkdir -p "$DOCS_DIR"
mkdir -p "$PDF_DIR"

# Function to extract document ID from Google Docs URL
extract_doc_id() {
    local url="$1"
    echo "$url" | grep -oP '(?<=document/d/)[^/]+' | head -1
}

# Function to download document as HTML
download_html() {
    local doc_id="$1"
    local filename="$2"
    local url="https://docs.google.com/document/d/${doc_id}/export?format=html"

    echo "Downloading HTML: $filename"
    curl -L -o "${DOCS_DIR}/${filename}.html" "$url"

    # Clean up the HTML (remove Google-specific scripts and styles)
    sed -i 's/<script[^>]*>.*<\/script>//g' "${DOCS_DIR}/${filename}.html"
}

# Function to download document as PDF
download_pdf() {
    local doc_id="$1"
    local filename="$2"
    local url="https://docs.google.com/document/d/${doc_id}/export?format=pdf"

    echo "Downloading PDF: $filename"
    curl -L -o "${PDF_DIR}/${filename}.pdf" "$url"
}

# Privacy Policy
echo "=== Privacy Policy ==="
download_html "1GGJ9W-foJm-M34FCkiTUCEgB7gSZMy41-_xIEBNPMpM" "privacy-policy-en"
download_pdf "1GGJ9W-foJm-M34FCkiTUCEgB7gSZMy41-_xIEBNPMpM" "privacy-policy-en"

download_html "1FlVaYgbtxkjr-AvAIrLbxbJnY2xX0N9of1jbCZGdImA" "privacy-policy-es"
download_pdf "1FlVaYgbtxkjr-AvAIrLbxbJnY2xX0N9of1jbCZGdImA" "privacy-policy-es"

download_html "1j1nkgARliQ6HTiWUF9fIaTQJbbUfmXot" "privacy-policy-it"
download_pdf "1j1nkgARliQ6HTiWUF9fIaTQJbbUfmXot" "privacy-policy-it"

# Cookies Policy
echo "=== Cookies Policy ==="
download_html "1hUzURCQbGq2Ohjpmo8cdRWxnPwt8QPfn" "cookies-policy-en"
download_pdf "1hUzURCQbGq2Ohjpmo8cdRWxnPwt8QPfn" "cookies-policy-en"

download_html "1Q3acAq1FgvfIAc7oF1N6J9hHsvIKHXXC" "cookies-policy-es"
download_pdf "1Q3acAq1FgvfIAc7oF1N6J9hHsvIKHXXC" "cookies-policy-es"

download_html "1jjctXQ1qstIQQUbGuNL_Ee21k1s60cPd" "cookies-policy-it"
download_pdf "1jjctXQ1qstIQQUbGuNL_Ee21k1s60cPd" "cookies-policy-it"

# Contracting and Purchase Process
echo "=== Contracting and Purchase Process ==="
download_html "1sA5n66yVxyHEERZiSYBuwE7riLtNbImm" "contracting-purchase-en"
download_pdf "1sA5n66yVxyHEERZiSYBuwE7riLtNbImm" "contracting-purchase-en"

download_html "19iL5o4aUpynDhjfffj20J2pYJZ4gLEBp" "contracting-purchase-es"
download_pdf "19iL5o4aUpynDhjfffj20J2pYJZ4gLEBp" "contracting-purchase-es"

download_html "1d2zGEOIVDpjoNchfpioyMvzUgPgNTrmi" "contracting-purchase-it"
download_pdf "1d2zGEOIVDpjoNchfpioyMvzUgPgNTrmi" "contracting-purchase-it"

# Subscription and Refund Policy
echo "=== Subscription and Refund Policy ==="
download_html "1qpPQqzJXu0qKFsNMZRjh4_1bmIpxcOF2" "subscription-refund-en"
download_pdf "1qpPQqzJXu0qKFsNMZRjh4_1bmIpxcOF2" "subscription-refund-en"

download_html "1e_XSvA5fZVAwGefLOLp-C5J1Nl0RcI67" "subscription-refund-es"
download_pdf "1e_XSvA5fZVAwGefLOLp-C5J1Nl0RcI67" "subscription-refund-es"

download_html "1b5MkRflwURRb6yhS1GaN875FK6l4645m" "subscription-refund-it"
download_pdf "1b5MkRflwURRb6yhS1GaN875FK6l4645m" "subscription-refund-it"

# Licence Agreement
echo "=== Licence Agreement ==="
download_html "1ac0BRftDuqAPW_7wu4izzMYs-IXYPIWb" "licence-agreement-en"
download_pdf "1ac0BRftDuqAPW_7wu4izzMYs-IXYPIWb" "licence-agreement-en"

download_html "1SBKrwdQ8gQhg1tV8tJhmBa8BQYhRHD28" "licence-agreement-es"
download_pdf "1SBKrwdQ8gQhg1tV8tJhmBa8BQYhRHD28" "licence-agreement-es"

download_html "1B4qym5BdqkAg3bc7ESp3WfItfqca_4Gj" "licence-agreement-it"
download_pdf "1B4qym5BdqkAg3bc7ESp3WfItfqca_4Gj" "licence-agreement-it"

# Terms of Use
echo "=== Terms of Use ==="
download_html "18odYkurzVgI0xyptBESp1lhtulyG0Ohc" "terms-of-use-en"
download_pdf "18odYkurzVgI0xyptBESp1lhtulyG0Ohc" "terms-of-use-en"

download_html "17eIMPyP8t4r46IDmwY_djnj1rdCYjkEm" "terms-of-use-es"
download_pdf "17eIMPyP8t4r46IDmwY_djnj1rdCYjkEm" "terms-of-use-es"

download_html "1KQd6zeRCPc0wPQR84ILArYnlcoF6gpsZ" "terms-of-use-it"
download_pdf "1KQd6zeRCPc0wPQR84ILArYnlcoF6gpsZ" "terms-of-use-it"

echo "=== Download complete ==="
