#!/bin/bash

# GitHub Pages Deployment Helper Script
# Quick setup for Python Practice Questions platform

echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║                                                                  ║"
echo "║   GitHub Pages - Python Practice Platform Deployment            ║"
echo "║                                                                  ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Error: Not a git repository"
    echo "   Run: git init"
    exit 1
fi

echo "📦 Checking files..."
if [ ! -d "docs" ]; then
    echo "❌ Error: docs folder not found"
    exit 1
fi

echo "✅ docs folder found"
echo "✅ Files ready for deployment"
echo ""

# Check git status
echo "📊 Git Status:"
git status --short

echo ""
echo "🚀 Ready to deploy!"
echo ""
echo "Next steps:"
echo ""
echo "1️⃣  Add files to git:"
echo "   git add docs/ practice-questions/"
echo ""
echo "2️⃣  Commit changes:"
echo "   git commit -m 'Add interactive GitHub Pages platform with 1000 Python questions'"
echo ""
echo "3️⃣  Push to GitHub:"
echo "   git push origin main"
echo ""
echo "4️⃣  Enable GitHub Pages:"
echo "   • Go to: https://github.com/PavanMudigondaTR/python-bro-code"
echo "   • Settings → Pages"
echo "   • Source: main branch"
echo "   • Folder: /docs"
echo "   • Save"
echo ""
echo "5️⃣  Wait 2-3 minutes, then visit:"
echo "   👉 https://pavanmudigondatr.github.io/python-bro-code/"
echo ""
echo "────────────────────────────────────────────────────────────────────"
echo ""

# Ask if user wants to auto-commit
read -p "Would you like to commit and push now? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "📝 Adding files..."
    git add docs/ GITHUB_PAGES_SETUP.md FEATURES.md deploy-github-pages.sh README.md
    git add practice-questions/progress.yaml 2>/dev/null || true
    
    echo "💾 Committing..."
    git commit -m "Add interactive GitHub Pages platform with 1000 Python practice questions

Features:
- Interactive Python code editor (PyScript/WebAssembly)
- Progress tracking with localStorage
- 1000 questions across 6 difficulty levels
- Achievement system with 14 badges
- Responsive design for all devices
- Zero-config deployment ready"
    
    echo "🚀 Pushing to GitHub..."
    git push origin main
    
    echo ""
    echo "✅ Deployment complete!"
    echo ""
    echo "Next: Enable GitHub Pages in your repo settings"
    echo "Then visit: https://pavanmudigondatr.github.io/python-bro-code/"
else
    echo ""
    echo "ℹ️  You can deploy manually later using the commands above"
fi

echo ""
echo "📖 For detailed instructions, see: GITHUB_PAGES_SETUP.md"
echo ""
