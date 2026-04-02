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

Documents are hosted at: https://auditaiadmin.github.io/legal/

**Note:** Each document is isolated and accessible only via direct URL. There is no public index page listing all documents. Users with a link to one document cannot navigate to discover other documents.

## 🔄 Updating Documents

To update the documents:

1. Update the Google Docs source documents
2. Run the download script:
   ```bash
   cd /home/pllanos/entropy/legal_docs/repo
   ./download_docs.sh
   ```
3. Regenerate the HTML pages:
   ```bash
   python3 generate_pages.py
   ```
4. Commit and push changes to gh-pages:
   ```bash
   git checkout gh-pages
   git add -A
   git commit -m "Update legal documents"
   git push origin gh-pages
   ```

## 🔗 Document URLs

Each document is accessible via direct URL:

**Privacy Policy:**
- English: `https://auditaiadmin.github.io/legal/privacy-policy-en.html`
- Español: `https://auditaiadmin.github.io/legal/privacy-policy-es.html`
- Italiano: `https://auditaiadmin.github.io/legal/privacy-policy-it.html`

**Cookies Policy:**
- English: `https://auditaiadmin.github.io/legal/cookies-policy-en.html`
- Español: `https://auditaiadmin.github.io/legal/cookies-policy-es.html`
- Italiano: `https://auditaiadmin.github.io/legal/cookies-policy-it.html`

**Contracting and Purchase Process:**
- English: `https://auditaiadmin.github.io/legal/contracting-purchase-en.html`
- Español: `https://auditaiadmin.github.io/legal/contracting-purchase-es.html`
- Italiano: `https://auditaiadmin.github.io/legal/contracting-purchase-it.html`

**Subscription and Refund Policy:**
- English: `https://auditaiadmin.github.io/legal/subscription-refund-en.html`
- Español: `https://auditaiadmin.github.io/legal/subscription-refund-es.html`
- Italiano: `https://auditaiadmin.github.io/legal/subscription-refund-it.html`

**Licence Agreement:**
- English: `https://auditaiadmin.github.io/legal/licence-agreement-en.html`
- Español: `https://auditaiadmin.github.io/legal/licence-agreement-es.html`
- Italiano: `https://auditaiadmin.github.io/legal/licence-agreement-it.html`

**Terms of Use:**
- English: `https://auditaiadmin.github.io/legal/terms-of-use-en.html`
- Español: `https://auditaiadmin.github.io/legal/terms-of-use-es.html`
- Italiano: `https://auditaiadmin.github.io/legal/terms-of-use-it.html`

## 📁 Repository Structure

```
.
├── index.html              # Redirects to 404 (no public index)
├── 404.html                # Custom 404 page
├── robots.txt              # Prevents search engine indexing
├── docs/                   # Raw HTML documents from Google Docs
├── pdf/                    # PDF versions of documents
├── *-en.html               # Individual document pages (English)
├── *-es.html               # Individual document pages (Español)
├── *-it.html               # Individual document pages (Italiano)
├── assets/
│   └── css/                # Stylesheets
├── download_docs.sh        # Script to download documents from Google Docs
├── generate_pages.py       # Script to generate HTML pages
├── check-deployment.sh     # Script to verify deployment status
└── .github/
    └── workflows/
        └── deploy.yml      # GitHub Actions deployment workflow
```

## 🚀 Deployment

The site is deployed to GitHub Pages from the `gh-pages` branch. Changes pushed to `gh-pages` are automatically published.

## 🔒 Security Features

- **Document Isolation:** Each document page has no links to other documents
- **No Public Index:** The root URL redirects to a 404 page
- **No Search Engine Indexing:** All pages include `noindex` meta tags
- **robots.txt:** Discourages crawler access
- **Language Switching Only:** Users can only switch languages within the same document type

## 📝 License

Copyright © 2026 AuditAI. All rights reserved.

Last updated: December 16, 2025
