# Contributing to PackagePilot

First off, thank you for considering contributing to PackagePilot! 🎉

## How Can I Contribute?

### 1. Add New Packages

The easiest way to contribute! Edit `seed_database.py`: 
```python
{
    "package": Package(
        id=None,
        name="package-name",
        description="Brief description of what it does",
        category="web",  # Choose: web, data, cli, testing, file, utilities, database
        install_command="pip install package-name",
        code_example="""import package_name

# Add a simple, working example
result = package_name.function()
print(result)""",
        pypi_url="https://pypi.org/project/package-name/",
        github_url="https://github.com/org/repo",  # Optional
        documentation_url="https://package-docs.com"  # Optional
    ),
    "keywords": ["keyword1", "keyword2", "keyword3"]  # For better search
},
```

**Guidelines:**
- Choose popular, actively maintained packages
- Provide a working code example (test it first!)
- Add 3-5 relevant keywords
- Keep descriptions under 80 characters

### 2. Improve Search

Edit `packagepilot/search.py`:

- Enhance the ranking algorithm
- Add more synonym mappings
- Improve relevance scoring
- Add fuzzy matching

### 3. Add Features

Some ideas:
- Package comparison feature
- Export search results
- Installation guides
- Bash completion
- Color output support

### 4. Fix Bugs

Found a bug? Please:
1. Check if it's already reported in Issues
2. Create a new issue with:
   - What you expected
   - What actually happened
   - Steps to reproduce
   - Your environment (OS, Python version)

### 5. Improve Documentation

- Fix typos
- Add examples
- Improve explanations
- Add screenshots

## Development Setup

```bash
# Fork and clone
git clone https://github.com/YOUR-USERNAME/packagepilot.git
cd packagepilot

# Create branch
git checkout -b feature-name

# Make changes
# ... edit files ...

# Test your changes
python seed_database.py  # If you added packages
python -m packagepilot search "test"

# Commit
git add .
git commit -m "Add: Brief description of changes"

# Push
git push origin feature-name

# Create Pull Request on GitHub
```

## Coding Standards

- Follow PEP 8 style guide
- Add docstrings to functions
- Use type hints where appropriate
- Keep functions focused and small
- Test your changes before submitting

## Questions?

Feel free to open an issue with the "question" label!

---

**Thank you for making PackagePilot better!** 🚀
