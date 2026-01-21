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
        "icon": "📄",
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
        "icon": "🍪",
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
        "icon": "🛒",
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
        "icon": "💳",
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
        "icon": "📜",
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
        "icon": "📋",
        "languages": {
            "en": {"name": "English", "flag": "🇬🇧"},
            "es": {"name": "Español", "flag": "🇪🇸"},
            "it": {"name": "Italiano", "flag": "🇮🇹"}
        }
    }
]

def generate_language_switcher(doc, current_lang):
    """Generate language switcher HTML"""
    switcher = '<div class="language-links">'
    for lang_code, lang_info in doc["languages"].items():
        is_current = lang_code == current_lang
        css_class = "lang-link active" if is_current else "lang-link"
        switcher += f'''
            <a href="{doc['id']}-{lang_code}.html" class="{css_class}">
                <div style="display: flex; align-items: center;">
                    <span class="lang-flag">{lang_info["flag"]}</span>
                    <div class="lang-info">
                        <span class="lang-name">{lang_info["name"]}</span>
                    </div>
                </div>
            </a>
        '''
    switcher += '</div>'
    return switcher

def read_document_content(doc_id, lang):
    """Read the HTML content of a document"""
    html_path = f"docs/{doc_id}-{lang}.html"
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract body content (remove html, head, body tags)
            import re
            body_match = re.search(r'<body[^>]*>(.*)</body>', content, re.DOTALL | re.IGNORECASE)
            if body_match:
                return body_match.group(1)
            return content
    return f"<p>Document content not found.</p>"

def generate_page(doc, lang):
    """Generate an HTML page for a specific document and language"""
    lang_info = doc["languages"][lang]
    content = read_document_content(doc["id"], lang)

    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{doc['title']} - AuditAI Legal Documents">
    <title>{doc['icon']} {doc['title']} - AuditAI</title>
    <link rel="stylesheet" href="assets/css/styles.css">
    <style>
        .language-switcher {{
            background: var(--card-bg);
            padding: 1.5rem;
            border-radius: 0.75rem;
            box-shadow: var(--shadow);
            margin-bottom: 2rem;
        }}
        .language-switcher h3 {{
            font-size: 1rem;
            margin-bottom: 1rem;
            color: var(--secondary-color);
        }}
        .lang-link.active {{
            background: var(--primary-color);
            color: white;
        }}
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <div class="header-content">
                <h1>{doc['icon']} {doc['title']}</h1>
                <p>AuditAI Legal Documents</p>
            </div>
        </div>
    </header>

    <main class="main-content">
        <div class="container">
            <div class="document-viewer">
                <div class="document-header">
                    <div class="document-title">
                        <div class="breadcrumb">
                            <a href="index.html">← Back to all documents</a>
                        </div>
                        <h2>{doc['title']}</h2>
                        <div class="document-meta">
                            <span><strong>Version:</strong> {doc['version']}</span> |
                            <span><strong>Language:</strong> {lang_info["flag"]} {lang_info["name"]}</span>
                        </div>
                    </div>
                    <div class="document-actions">
                        <a href="pdf/{doc['id']}-{lang}.pdf" class="btn btn-primary" download>
                            📥 Download PDF
                        </a>
                    </div>
                </div>

                <div class="language-switcher">
                    <h3>🌐 Available Languages</h3>
                    {generate_language_switcher(doc, lang)}
                </div>

                <div class="document-content">
                    {content}
                </div>
            </div>
        </div>
    </main>

    <footer class="footer">
        <div class="container">
            <p>&copy; 2026 AuditAI. All rights reserved.</p>
            <p><a href="index.html">Back to all documents</a></p>
        </div>
    </footer>
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
