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

## 🌐 Published Website

The documents are published at: **https://auditaiadmin.github.io/legal/**

Each document is accessible only via its direct URL (no public index page).

---

## 🔧 How to Update Documents

This guide is written for people with **NO technical experience**. Follow every step carefully.

### Step 1: Install GitHub Desktop

GitHub Desktop is a free application that makes it easy to work with this repository.

#### For Windows:
1. Go to https://desktop.github.com/download/
2. Click the **Download for Windows** button
3. Once downloaded, double-click the file `GitHubDesktopSetup-x64.exe`
4. Follow the installation wizard (just click "Next" on everything)
5. When it asks you to sign in, use your GitHub account credentials

#### For Mac:
1. Go to https://desktop.github.com/download/
2. Click the **Download for macOS** button
3. Once downloaded, open the file `GitHubDesktop-arm64.dmg` (or `GitHubDesktop-x64.dmg` for Intel Macs)
4. Drag the GitHub Desktop icon to your Applications folder
5. Open GitHub Desktop from Applications
6. When it asks you to sign in, use your GitHub account credentials

#### For Linux (Ubuntu/Debian):
1. Open Terminal (press Ctrl+Alt+T)
2. Copy and paste this command, then press Enter:
   ```bash
   wget https://github.com/shiftkey/desktop/releases/download/release-3.3.12-linux1/GitHubDesktop-linux-amd64-3.3.12-linux1.deb
   ```
3. Wait for the download to complete
4. Install it with this command:
   ```bash
   sudo dpkg -i GitHubDesktop-linux-amd64-3.3.12-linux1.deb
   ```
5. If you get errors, run:
   ```bash
   sudo apt-get install -f
   ```
6. Open GitHub Desktop from your applications menu
7. Sign in with your GitHub account

### Step 2: Clone (Download) the Repository

1. Open **GitHub Desktop**
2. Click **File** → **Clone Repository**
3. Click the **URL** tab
4. In the "Repository URL" field, paste: `https://github.com/Auditaiadmin/legal.git`
5. In "Local Path", choose where you want to save the files (e.g., `Documents/legal`)
6. Click **Clone**
7. Wait for the download to complete

**IMPORTANT:** Make sure you're on the **gh-pages** branch:
- In GitHub Desktop, look at the top of the window
- You should see "Current Branch: gh-pages"
- If it says "main", click on it and select **gh-pages** from the list

### Step 3: Edit the HTML Documents

The HTML files you need to edit are in the `docs/` folder.

#### To modify document content:

1. Navigate to the `docs/` folder in the cloned repository
2. Find the document you want to edit, for example:
   - `privacy-policy-en.html` (Privacy Policy in English)
   - `cookies-policy-es.html` (Cookies Policy in Spanish)
   - `licence-agreement-it.html` (Licence Agreement in Italian)
3. **Right-click** on the file → **Open With** → Choose a text editor:
   - **Windows**: Notepad (simple) or Notepad++ (better)
   - **Mac**: TextEdit (make sure it's in Plain Text mode: Format → Make Plain Text)
   - **Linux**: gedit, nano, or any text editor
4. Find the text you want to change
5. Make your changes (be careful not to delete HTML tags like `<p>`, `</span>`, etc.)
6. **Save the file** (Ctrl+S on Windows/Linux, Cmd+S on Mac)

**WARNING:** Only edit the text content. Do NOT delete or modify:
- Anything inside `< >` brackets (these are HTML tags)
- The `<style>` section at the beginning
- Class names like `class="c4"`

#### To modify links:

Links look like this: `<a class="c7" href="https://example.com">Link Text</a>`

To change a link:
1. Find the `href="..."` part
2. Replace the URL between the quotes
3. Save the file

### Step 4: Replace PDF Files

1. Navigate to the `pdf/` folder in the cloned repository
2. Find the PDF you want to replace, for example: `privacy-policy-en.pdf`
3. **Delete** the old PDF file
4. **Copy** your new PDF file into this folder
5. **Rename** it to match the exact same name as the old one (e.g., `privacy-policy-en.pdf`)

**IMPORTANT:** The file name must be EXACTLY:
- `privacy-policy-en.pdf`, `privacy-policy-es.pdf`, `privacy-policy-it.pdf`
- `cookies-policy-en.pdf`, `cookies-policy-es.pdf`, `cookies-policy-it.pdf`
- `contracting-purchase-en.pdf`, `contracting-purchase-es.pdf`, `contracting-purchase-it.pdf`
- `subscription-refund-en.pdf`, `subscription-refund-es.pdf`, `subscription-refund-it.pdf`
- `licence-agreement-en.pdf`, `licence-agreement-es.pdf`, `licence-agreement-it.pdf`
- `terms-of-use-en.pdf`, `terms-of-use-es.pdf`, `terms-of-use-it.pdf`

### Step 5: Regenerate the Final Pages

After editing the HTML files in `docs/`, you need to regenerate the final web pages.

#### On Windows:
1. Press **Windows Key + R**
2. Type `cmd` and press Enter
3. Type this command and press Enter:
   ```
   cd Documents\legal
   ```
   (Replace `Documents\legal` with wherever you cloned the repository)
4. Type this command and press Enter:
   ```
   python generate_pages.py
   ```
5. You should see "✓ Successfully generated 18 pages"

#### On Mac:
1. Open **Terminal** (press Cmd+Space, type "Terminal", press Enter)
2. Type this command and press Enter:
   ```
   cd ~/Documents/legal
   ```
   (Replace with wherever you cloned the repository)
3. Type this command and press Enter:
   ```
   python3 generate_pages.py
   ```
4. You should see "✓ Successfully generated 18 pages"

#### On Linux:
1. Open **Terminal** (press Ctrl+Alt+T)
2. Type this command and press Enter:
   ```
   cd ~/Documents/legal
   ```
   (Replace with wherever you cloned the repository)
3. Type this command and press Enter:
   ```
   python3 generate_pages.py
   ```
4. You should see "✓ Successfully generated 18 pages"

**If you get an error** saying "python is not recognized" or "command not found":
- **Windows**: Install Python from https://www.python.org/downloads/ (check "Add Python to PATH" during installation)
- **Mac/Linux**: Python should be pre-installed. Try `python3` instead of `python`

### Step 6: Commit Your Changes

A "commit" is like saving a checkpoint of your work with a description of what you changed.

1. Go back to **GitHub Desktop**
2. You'll see a list of all the files you changed on the left side
3. At the bottom left, there are two text boxes:
   - **Summary (required)**: Write a short description, for example:
     - "Update Privacy Policy English version"
     - "Fix typo in Cookies Policy"
     - "Update all PDF files to latest version"
   - **Description (optional)**: You can add more details here if needed
4. Click the blue **Commit to gh-pages** button

**That's it!** Your changes are now saved locally on your computer.

### Step 7: Push (Publish) Your Changes

"Pushing" uploads your changes to GitHub and publishes them to the website.

1. After committing, you'll see a button at the top that says **Push origin**
2. Click the **Push origin** button
3. Wait for it to finish (you'll see a loading indicator)
4. **Done!** Your changes are now uploaded to GitHub

### Step 8: Wait for Publication

1. Go to https://github.com/Auditaiadmin/legal/actions
2. You'll see a yellow dot 🟡 next to your commit (this means it's building)
3. Wait 1-2 minutes
4. The yellow dot will turn into a green checkmark ✅ when it's done
5. Your changes are now live at https://auditaiadmin.github.io/legal/

**If you see a red X ❌:**
- Something went wrong
- Check the error by clicking on the failed action
- Contact technical support for help

---

## 🆘 Troubleshooting

### "I can't find the docs/ folder"
- Make sure you cloned the repository (Step 2)
- Make sure you're on the **gh-pages** branch (see Step 2)
- Look in the folder where you cloned the repository

### "The generate_pages.py script doesn't work"
- Make sure Python is installed
- Make sure you're in the correct folder (the `legal` repository folder)
- Try `python3 generate_pages.py` instead of `python generate_pages.py`

### "GitHub Desktop says 'No changes'"
- Make sure you saved your file after editing
- Make sure you're editing files in the cloned repository, not somewhere else
- Try closing and reopening GitHub Desktop

### "My changes aren't showing on the website"
- Wait 2-3 minutes after pushing
- Clear your browser cache (Ctrl+Shift+R on most browsers)
- Check https://github.com/Auditaiadmin/legal/actions to see if the build succeeded

### "I messed up and want to undo everything"
1. In GitHub Desktop, click **Repository** → **Discard All Changes**
2. This will undo everything back to the last commit
3. **WARNING:** This cannot be undone, all your changes will be lost

---

## 📁 Repository Structure

```
legal/
├── index.html                    # Redirects to 404 (no public index)
├── 404.html                      # Custom 404 page
├── robots.txt                    # Prevents search engine indexing
├── docs/                         # SOURCE FILES - Edit these!
│   ├── privacy-policy-en.html    # Privacy Policy source (English)
│   ├── privacy-policy-es.html    # Privacy Policy source (Spanish)
│   ├── privacy-policy-it.html    # Privacy Policy source (Italian)
│   ├── cookies-policy-*.html     # Cookies Policy sources
│   ├── contracting-purchase-*.html
│   ├── subscription-refund-*.html
│   ├── licence-agreement-*.html
│   └── terms-of-use-*.html
├── pdf/                          # PDF FILES - Replace these!
│   ├── privacy-policy-en.pdf
│   ├── privacy-policy-es.pdf
│   └── ... (all PDFs)
├── privacy-policy-en.html        # GENERATED - Don't edit directly!
├── cookies-policy-en.html        # GENERATED - Don't edit directly!
├── ... (all final HTML pages)    # GENERATED by generate_pages.py
├── assets/
│   ├── css/
│   │   └── document.css          # Website styling
│   └── images/
│       └── favicon.svg           # AuditAI logo
├── generate_pages.py             # Script to create final HTML pages
└── .github/
    └── workflows/
        └── deploy.yml            # Auto-deployment configuration
```

**KEY POINT:**
- **Edit files in `docs/` folder** (source files)
- **Run `generate_pages.py`** to create the final pages
- **Never edit the HTML files in the root folder** (they get overwritten)

---

## 🔗 Document URLs

Each document is accessible only via direct URL:

**Privacy Policy:**
- 🇬🇧 https://auditaiadmin.github.io/legal/privacy-policy-en.html
- 🇪🇸 https://auditaiadmin.github.io/legal/privacy-policy-es.html
- 🇮🇹 https://auditaiadmin.github.io/legal/privacy-policy-it.html

**Cookies Policy:**
- 🇬🇧 https://auditaiadmin.github.io/legal/cookies-policy-en.html
- 🇪🇸 https://auditaiadmin.github.io/legal/cookies-policy-es.html
- 🇮🇹 https://auditaiadmin.github.io/legal/cookies-policy-it.html

**Contracting and Purchase Process:**
- 🇬🇧 https://auditaiadmin.github.io/legal/contracting-purchase-en.html
- 🇪🇸 https://auditaiadmin.github.io/legal/contracting-purchase-es.html
- 🇮🇹 https://auditaiadmin.github.io/legal/contracting-purchase-it.html

**Subscription and Refund Policy:**
- 🇬🇧 https://auditaiadmin.github.io/legal/subscription-refund-en.html
- 🇪🇸 https://auditaiadmin.github.io/legal/subscription-refund-es.html
- 🇮🇹 https://auditaiadmin.github.io/legal/subscription-refund-it.html

**Licence Agreement:**
- 🇬🇧 https://auditaiadmin.github.io/legal/licence-agreement-en.html
- 🇪🇸 https://auditaiadmin.github.io/legal/licence-agreement-es.html
- 🇮🇹 https://auditaiadmin.github.io/legal/licence-agreement-it.html

**Terms of Use:**
- 🇬🇧 https://auditaiadmin.github.io/legal/terms-of-use-en.html
- 🇪🇸 https://auditaiadmin.github.io/legal/terms-of-use-es.html
- 🇮🇹 https://auditaiadmin.github.io/legal/terms-of-use-it.html

---

## 🔒 Security Features

- **Document Isolation:** Each document has no links to discover other documents
- **No Public Index:** The root URL redirects to a 404 page
- **No Search Engine Indexing:** All pages include `noindex` meta tags
- **Language Switching Only:** Users can only switch languages within the same document type

---

## 📝 Quick Reference Card

**What do I edit?** → Files in the `docs/` folder

**How do I update PDFs?** → Replace files in the `pdf/` folder with the same names

**What do I run after editing?** → `python3 generate_pages.py` (or `python generate_pages.py` on Windows)

**How do I publish?** → Commit in GitHub Desktop, then click "Push origin"

**Where is the website?** → https://auditaiadmin.github.io/legal/

**How long until changes appear?** → 1-2 minutes after pushing

---

## 📞 Need Help?

If you get stuck:
1. Read the error message carefully
2. Check the Troubleshooting section above
3. Contact the technical team with:
   - What you were trying to do
   - What error message you got (take a screenshot)
   - Which file you were editing

---

## 📝 License

Copyright © 2026 AuditAI. All rights reserved.

Last updated: December 16, 2025

