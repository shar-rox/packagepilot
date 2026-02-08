# PackagePilot 🚀

> Your intelligent Python package discovery assistant

**PackagePilot** helps developers quickly find the right Python packages for their projects through natural language search. Stop Googling "best Python package for X" - just ask PackagePilot!

---

## 🎯 The Problem

As a Python developer, you often know **what** you want to build, but struggle to remember **which** package to use:

- "What package do I use for making HTTP requests again?"
- "I need to scrape a website - is it BeautifulSoup or Scrapy?"
- "Which testing framework should I use?"

**PackagePilot solves this.**

---

## ✨ Features

- 🔍 **Smart Search** - Natural language queries like "web scraping" or "parse HTML"
- 📦 **35+ Curated Packages** - Hand-picked popular Python packages across 7 categories
- 💡 **Search Suggestions** - Get helpful hints when nothing is found
- 📊 **Stats Dashboard** - Visualize package distribution by category
- ⚡ **Lightning Fast** - Offline SQLite database, instant results
- 📝 **Code Examples** - Every package includes working code snippets
- 🎨 **Category Browsing** - Explore packages by web, data, CLI, testing, and more

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/shar-rox/packagepilot.git
cd packagepilot

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Seed the database
python seed_database.py
```

### Usage

```bash
# Search for packages
python -m packagepilot search "web scraping"

# Get detailed info about a package
python -m packagepilot info beautifulsoup4

# Browse by category
python -m packagepilot category web

# See all categories
python -m packagepilot categories

# View statistics
python -m packagepilot stats

# List all packages
python -m packagepilot list
```

---

## 📖 Example Workflow

```bash
$ python -m packagepilot search "http requests"

[FOUND] 2 package(s) for 'http requests':

======================================================================
PACKAGE: requests
======================================================================

Simple HTTP library for making web requests

Category: web
Install: pip install requests

======================================================================
PACKAGE: httpx
======================================================================

Modern async HTTP client with HTTP/2 support

Category: web
Install: pip install httpx

[TIP] Use 'packagepilot info <package-name>' for full details
```

```bash
$ python -m packagepilot info requests

======================================================================
PACKAGE: requests
======================================================================

Simple HTTP library for making web requests

Category: web
Install: pip install requests

----------------------------------------------------------------------
Code Example:
----------------------------------------------------------------------
import requests

response = requests.get('https://api.github.com')
print(response.json())

----------------------------------------------------------------------
Links:
----------------------------------------------------------------------
PyPI: https://pypi.org/project/requests/
Docs: https://requests.readthedocs.io/
GitHub: https://github.com/psf/requests
```

---

## 📦 Package Categories

PackagePilot includes **35+ packages** across 7 categories:

| Category | Packages | Examples |
|----------|----------|----------|
| **Web** | 8 | requests, beautifulsoup4, flask, django, selenium, scrapy |
| **Data** | 6 | pandas, numpy, matplotlib, seaborn, scikit-learn, plotly |
| **CLI** | 4 | typer, rich, click, tqdm |
| **Testing** | 3 | pytest, unittest, coverage |
| **File** | 4 | openpyxl, pillow, PyPDF2, pathlib |
| **Utilities** | 4 | python-dotenv, schedule, loguru, pydantic |
| **Database** | 3 | sqlalchemy, pymongo, redis |

---

## 🎨 Commands Reference

| Command | Description | Example |
|---------|-------------|---------|
| `search <query>` | Search packages | `python -m packagepilot search "web scraping"` |
| `info <name>` | Get package details | `python -m packagepilot info requests` |
| `category <name>` | List category packages | `python -m packagepilot category web` |
| `categories` | Show all categories | `python -m packagepilot categories` |
| `stats` | Show statistics | `python -m packagepilot stats` |
| `list` | List all packages | `python -m packagepilot list` |

---

## 🛠️ Technical Stack

- **Language**: Python 3.7+
- **Database**: SQLite3 (built-in, no setup needed)
- **CLI Framework**: argparse (standard library)
- **Architecture**: Modular design with separation of concerns

### Project Structure

```
packagepilot/
├── packagepilot/           # Main source code
│   ├── cli.py             # Command-line interface
│   ├── database.py        # Database operations
│   ├── search.py          # Search logic & ranking
│   ├── models.py          # Data models
│   └── data/
│       └── packages.db    # SQLite database
├── tests/                  # Unit tests
├── seed_database.py       # Database population script
├── requirements.txt       # Dependencies (minimal!)
└── README.md             # This file
```

---

## 🧠 How It Works

### 1. Smart Multi-Word Search

PackagePilot uses an intelligent search algorithm:

```python
Query: "web scraping"
→ Try exact phrase first
→ If no results, split into words: ["web", "scraping"]
→ Search for each word individually
→ Combine results and rank by relevance
```

### 2. Relevance Ranking

Results are scored based on:
- Exact name match: **100 points**
- Name contains query: **50 points**
- Description contains query: **30 points**
- Category match: **20 points**
- Individual word matches: **10 points each**

### 3. Search Suggestions

When no results are found, PackagePilot suggests related terms:

```
Search: "scrape" → Suggests: beautifulsoup, selenium, scrapy
Search: "ml" → Suggests: scikit-learn, machine learning
Search: "db" → Suggests: database, sql, orm
```

---

## 💡 Why I Built This

As a Python learner, I constantly forget which packages to use for common tasks. I'd spend time Googling, reading comparisons, and checking documentation just to find the right tool.

**PackagePilot** is my solution - a fast, offline reference that suggests packages with working code examples. It's become an essential tool in my development workflow.

---

## 🎯 What I Learned

Building PackagePilot taught me:

- ✅ **Database Design** - SQLite schema, relationships, indexing
- ✅ **Search Algorithms** - Ranking, relevance scoring, fuzzy matching
- ✅ **CLI Development** - Argument parsing, user experience, error handling
- ✅ **Software Architecture** - Separation of concerns, modularity, clean code
- ✅ **Python Best Practices** - Type hints, docstrings, PEP 8
- ✅ **Version Control** - Git workflow, meaningful commits

---

## 🚧 Future Enhancements

Ideas for future versions:

- [ ] AI-powered recommendations using Claude/GPT APIs
- [ ] Package comparison feature
- [ ] Installation guide generator
- [ ] Export results to different formats
- [ ] Web interface with Flask/FastAPI
- [ ] Real-time package popularity from PyPI
- [ ] User-contributed package ratings
- [ ] Integration with pip for direct installation

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Add more packages** - Edit `seed_database.py`
2. **Improve search** - Enhance ranking in `search.py`
3. **Fix bugs** - Submit issues or pull requests
4. **Suggest features** - Open an issue with ideas

### Adding a New Package

Edit `seed_database.py` and add:

```python
{
    "package": Package(
        id=None,
        name="your-package",
        description="What it does",
        category="web",  # web, data, cli, testing, file, utilities, database
        install_command="pip install your-package",
        code_example="""import your_package

# Example usage
result = your_package.do_something()
print(result)""",
        pypi_url="https://pypi.org/project/your-package/",
        github_url="https://github.com/user/repo",
        documentation_url="https://docs.example.com"
    ),
    "keywords": ["keyword1", "keyword2", "keyword3"]
},
```

Then run: `python seed_database.py`

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Sharanya Adithya**

- GitHub: [@shar-rox](https://github.com/shar-rox)
- Project: [PackagePilot](https://github.com/shar-rox/packagepilot)

---

## 🙏 Acknowledgments

- Inspired by the need for faster Python package discovery
- Built as a learning project to understand databases, search, and CLI tools
- Thanks to the Python community for creating amazing packages

---

## 📊 Project Stats

- **35+ Packages** across 7 categories
- **Lightning fast** SQLite-based search
- **0 external dependencies** for core functionality
- **100% Python** - no frameworks needed
- **Educational project** - learn by building tools you actually use

---

<p align="center">
  <b>⭐ Star this repo if you find it helpful!</b>
  <br>
  <i>Built with ❤️ for Python developers</i>
</p>
