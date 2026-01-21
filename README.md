# AuditAI Legal Documents

Official legal documentation repository for AuditAI platform.

## 📄 Available Documents

- **Privacy Policy** (PRP-01/2026-V1)
- **Cookies Policy** (CKP-01/2026-V1)
- **Contracting and Purchase Process** (CPP-01/2026-V1)
- **Subscription and Refund Policy** (SRP-01/2026-V1)
- **Licence Agreement** (LIC-01/2026-V1)
- **Terms of Use** (TCC-01/2026-V1)

All documents are available in three languages:
- 🇬🇧 English
- 🇪🇸 Español
- 🇮🇹 Italiano

## 🌐 Website

Visit the documentation site at: https://auditaiadmin.github.io/legal/

## 🔄 Updating Documents

To update the documents:

1. Update the Google Docs source documents
2. Run the download script:
   ```bash
   ./download_docs.sh
   ```
3. Regenerate the HTML pages:
   ```bash
   python3 generate_pages.py
   ```
4. Commit and push changes

## 📁 Repository Structure

```
.
├── index.html              # Main landing page
├── docs/                   # Raw HTML documents from Google Docs
├── pdf/                    # PDF versions of documents
├── assets/
│   ├── css/                # Stylesheets
│   ├── js/                 # JavaScript files
│   └── images/             # Images and logos
├── download_docs.sh        # Script to download documents from Google Docs
├── generate_pages.py       # Script to generate HTML pages
└── .github/
    └── workflows/
        └── deploy.yml      # GitHub Actions deployment workflow
```

## 🚀 Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the main branch.

## 📝 License

Copyright © 2026 AuditAI. All rights reserved.

Last updated: December 16, 2025
