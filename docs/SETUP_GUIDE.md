# PackagePilot Setup Guide

## Getting Started

Follow these steps to set up and run PackagePilot on your machine:

### Prerequisites

- Python 3.7 or higher
- Basic understanding of terminal/command line

### Installation Steps

#### 1. Download the Project

If you have this folder, you're good! Otherwise:
```bash
# If on GitHub:
git clone https://github.com/yourusername/packagepilot.git
cd packagepilot
```

#### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

You'll see `(venv)` in your terminal when activated.

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** Currently using built-in libraries. Will add typer and rich later.

#### 4. Seed the Database

```bash
python seed_database.py
```

You should see:
```
Seeding database with packages...
✓ Added: requests
✓ Added: httpx
...
Database seeded successfully! Total packages: 14
```

#### 5. Test It Out!

```bash
# Search for packages
python -m packagepilot search "http"

# Get package info
python -m packagepilot info requests

# List categories
python -m packagepilot categories

# See packages in a category
python -m packagepilot category web

# List all packages
python -m packagepilot list
```

## All Commands

| Command | Description | Example |
|---------|-------------|---------|
| `search <query>` | Search for packages | `python -m packagepilot search "web scraping"` |
| `info <name>` | Get package details | `python -m packagepilot info beautifulsoup4` |
| `category <name>` | List category packages | `python -m packagepilot category data` |
| `categories` | Show all categories | `python -m packagepilot categories` |
| `list` | List all packages | `python -m packagepilot list` |

## Troubleshooting

### "ModuleNotFoundError: No module named 'packagepilot'"

**Solution:** Make sure you're running from the project root directory:
```bash
cd packagepilot
python -m packagepilot search "http"
```

### "No packages found"

**Solution:** Run the seed script:
```bash
python seed_database.py
```

### Database already exists error

**Solution:** Delete the old database:
```bash
rm packagepilot/data/packages.db
python seed_database.py
```

### Virtual environment not activating

**Solution:**
- Windows: Use `venv\Scripts\activate.bat` instead
- Make sure you're in the project directory

## Project Structure

```
packagepilot/
├── packagepilot/           # Main source code
│   ├── cli.py             # Command line interface
│   ├── database.py        # Database operations
│   ├── search.py          # Search logic
│   ├── models.py          # Data structures
│   └── data/
│       └── packages.db    # SQLite database (created after seeding)
├── tests/                  # Tests (empty for now)
├── seed_database.py       # Database seeding script
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## Adding More Packages

Want to add your own packages? Edit `seed_database.py`:

```python
{
    "package": Package(
        id=None,
        name="your-package",
        description="What it does",
        category="web",  # or data, cli, testing, file, utilities
        install_command="pip install your-package",
        code_example="""import your_package

# Example usage here""",
        pypi_url="https://pypi.org/project/your-package/",
        github_url="https://github.com/user/repo",
        documentation_url="https://docs.example.com"
    ),
    "keywords": ["keyword1", "keyword2", "keyword3"]
},
```

Then run:
```bash
python seed_database.py
```

## Development Tips

### Testing Your Changes

After modifying code:
1. Save the file
2. Run the command again
3. Check if it works as expected

### Viewing the Database

Install SQLite browser or use command line:
```bash
sqlite3 packagepilot/data/packages.db
.tables
SELECT * FROM packages;
.quit
```

### Making It Global (Optional)

To run `packagepilot` from anywhere:

1. Create `setup.py` (coming in Day 7)
2. Install in development mode:
```bash
pip install -e .
```

Then you can just type:
```bash
packagepilot search "http"
```

## Next Steps

1. ✅ Installation complete
2. ✅ Database seeded
3. ✅ Tested commands
4. 📝 Add more packages
5. 🎨 Customize for your needs
6. 🚀 Push to GitHub

## Need Help?

- Check `DAY1_COMPLETE.md` for detailed explanation
- Read the code comments
- Experiment and learn by doing!

Happy coding! 🚀
