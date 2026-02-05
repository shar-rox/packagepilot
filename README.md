# PackagePilot 🚀

**Your intelligent Python package discovery assistant**

PackagePilot helps developers discover and learn about Python packages through natural language search. Just describe what you want to build, and get instant package recommendations with code examples.

## 🎯 Why PackagePilot?

As Python developers, we often know *what* we want to build but struggle to remember *which* package to use. PackagePilot solves this by:

- 🔍 **Smart Search**: Search using natural language like "parse HTML" or "make HTTP requests"
- 📚 **Code Examples**: Get working code snippets for every package
- ⚡ **Fast**: Lightning-fast CLI tool that works offline
- 🎓 **Learn**: Discover new packages and best practices

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/shar-rox/packagepilot.git
cd packagepilot

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Seed the database
python seed_database.py
```

## 📖 Usage

```bash
# Search for packages
python -m packagepilot search "make HTTP requests"

# Get info about a specific package
python -m packagepilot info requests

# List all packages in a category
python -m packagepilot category web
```

## 🛠️ Features

- ✅ Natural language package search
- ✅ Code examples for every package
- ✅ Category-based browsing
- ✅ Offline database
- 🔜 AI-powered recommendations (coming soon)
- 🔜 Package comparison
- 🔜 Installation guides

## 📦 Current Package Categories

- **Web**: HTTP clients, web frameworks, scraping tools
- **Data**: Data analysis, visualization, manipulation
- **CLI**: Command-line tools and utilities
- **Testing**: Testing frameworks and tools
- **File**: File handling and processing
- **Utilities**: Configuration, environment management

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Add new packages to the database
- Improve search algorithms
- Add new features
- Fix bugs

## 📝 License

MIT License

## 👤 Author

Sharanya - [GitHub](https://github.com/shar-rox)

---

*Built with ❤️ to make Python development easier*
