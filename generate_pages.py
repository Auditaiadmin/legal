#!/usr/bin/env python3
"""
Script to generate HTML pages for each legal document
"""

import os
from pathlib import Path

# Document configuration
documents = [
    {
        "id": "privacy-policy",
        "title": "Privacy Policy",
        "version": "PRP-01/2026-V1",
        "languages": {
            "en": {"name": "English", "flag": "🇬🇧"},
            "es": {"name": "Español", "flag": "🇪🇸"},
            "it": {"name": "Italiano", "flag": "🇮🇹"}
        }
    },
    {
        "id": "cookies-policy",
        "title": "Cookies Policy",
        "version": "CKP-01/2026-V1",
        "languages": {
            "en": {"name": "English", "flag": "🇬🇧"},
            "es": {"name": "Español", "flag": "🇪🇸"},
            "it": {"name": "Italiano", "flag": "🇮🇹"}
        }
    },
    {
        "id": "contracting-purchase",
        "title": "Contracting and Purchase Process",
        "version": "CPP-01/2026-V1",
        "languages": {
            "en": {"name": "English", "flag": "🇬🇧"},
            "es": {"name": "Español", "flag": "🇪🇸"},
            "it": {"name": "Italiano", "flag": "🇮🇹"}
        }
    },
    {
        "id": "subscription-refund",
        "title": "Subscription and Refund Policy",
        "version": "SRP-01/2026-V1",
        "languages": {
            "en": {"name": "English", "flag": "🇬🇧"},
            "es": {"name": "Español", "flag": "🇪🇸"},
            "it": {"name": "Italiano", "flag": "🇮🇹"}
        }
    },
    {
        "id": "licence-agreement",
        "title": "Licence Agreement",
        "version": "LIC-01/2026-V1",
        "languages": {
            "en": {"name": "English", "flag": "🇬🇧"},
            "es": {"name": "Español", "flag": "🇪🇸"},
            "it": {"name": "Italiano", "flag": "🇮🇹"}
        }
    },
    {
        "id": "terms-of-use",
        "title": "Terms of Use (Disclaimer)",
        "version": "TCC-01/2026-V1",
        "languages": {
            "en": {"name": "English", "flag": "🇬🇧"},
            "es": {"name": "Español", "flag": "🇪🇸"},
            "it": {"name": "Italiano", "flag": "🇮🇹"}
        }
    }
]

def generate_language_selector(doc, current_lang):
    """Generate compact language selector dropdown"""
    lang_info = doc["languages"][current_lang]

    options = ""
    for lang_code, info in doc["languages"].items():
        is_active = lang_code == current_lang
        active_class = " active" if is_active else ""
        options += f'''
        <a href="{doc['id']}-{lang_code}.html" class="language-option{active_class}">
            <span class="language-flag">{info["flag"]}</span>
            <span>{info["name"]}</span>
        </a>'''

    return f'''
    <div class="language-selector">
        <div class="language-dropdown">
            <button class="language-button" type="button">
                <span class="language-flag">{lang_info["flag"]}</span>
                <span>{lang_info["name"]}</span>
                <span class="language-arrow">▼</span>
            </button>
            <div class="language-menu">{options}
            </div>
        </div>
    </div>'''

def read_document_content(doc_id, lang):
    """Read the full HTML content including styles from Google Docs"""
    html_path = f"docs/{doc_id}-{lang}.html"
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return content
    return f"<p>Document content not found.</p>"

def generate_page(doc, lang):
    """Generate an HTML page for a specific document and language"""
    lang_info = doc["languages"][lang]
    google_doc_html = read_document_content(doc["id"], lang)

    # Extract head content (styles) and body content separately
    import re
    head_match = re.search(r'<head[^>]*>(.*?)</head>', google_doc_html, re.DOTALL | re.IGNORECASE)
    body_match = re.search(r'<body[^>]*>(.*)</body>', google_doc_html, re.DOTALL | re.IGNORECASE)

    google_styles = head_match.group(1) if head_match else ""
    document_content = body_match.group(1) if body_match else google_doc_html

    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{doc['title']} - AuditAI">
    <meta name="robots" content="noindex, nofollow">
    <title>{doc['title']} - AuditAI</title>
    <link rel="icon" type="image/svg+xml" href="assets/images/favicon.svg">
    <link rel="stylesheet" href="assets/css/document.css">
    {google_styles}
</head>
<body>
    <!-- Fixed Toolbar -->
    <div class="document-toolbar">
        <div class="toolbar-content">
            <a href="pdf/{doc['id']}-{lang}.pdf" class="pdf-download" download>
                <svg class="pdf-icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                <span>PDF</span>
            </a>

            {generate_language_selector(doc, lang)}
        </div>
    </div>

    <!-- Document Content -->
    <div class="document-container">
        <div class="document-content">
            {document_content}
        </div>
    </div>

    <!-- JavaScript for language dropdown -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const dropdown = document.querySelector('.language-dropdown');
            const button = dropdown.querySelector('.language-button');

            // Toggle dropdown on button click
            button.addEventListener('click', function(e) {{
                e.stopPropagation();
                dropdown.classList.toggle('open');
            }});

            // Close dropdown when clicking outside
            document.addEventListener('click', function(e) {{
                if (!dropdown.contains(e.target)) {{
                    dropdown.classList.remove('open');
                }}
            }});

            // Prevent dropdown from closing when clicking inside the menu
            const menu = dropdown.querySelector('.language-menu');
            menu.addEventListener('click', function(e) {{
                e.stopPropagation();
            }});
        }});
    </script>
</body>
</html>'''

    return html

def main():
    """Generate all document pages"""
    print("Generating document pages...")

    for doc in documents:
        for lang_code in doc["languages"].keys():
            filename = f"{doc['id']}-{lang_code}.html"
            html_content = generate_page(doc, lang_code)

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)

            print(f"✓ Generated: {filename}")

    print(f"\n✓ Successfully generated {len(documents) * len(documents[0]['languages'])} pages")

if __name__ == "__main__":
    main()
