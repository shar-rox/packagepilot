"""
Seed the database with initial package data.
Windows-compatible version (no emojis)
Run this script once to populate the database with common Python packages.
"""
from packagepilot.database import Database
from packagepilot.models import Package


def seed_database():
    """Populate database with curated Python packages."""
    
    db = Database()
    
    # List of packages to add
    packages_data = [
        # WEB & HTTP
        {
            "package": Package(
                id=None,
                name="requests",
                description="Simple HTTP library for making web requests",
                category="web",
                install_command="pip install requests",
                code_example="""import requests

response = requests.get('https://api.github.com')
print(response.json())""",
                pypi_url="https://pypi.org/project/requests/",
                github_url="https://github.com/psf/requests",
                documentation_url="https://requests.readthedocs.io/"
            ),
            "keywords": ["http", "api", "web", "rest", "get", "post", "requests"]
        },
        {
            "package": Package(
                id=None,
                name="httpx",
                description="Modern async HTTP client with HTTP/2 support",
                category="web",
                install_command="pip install httpx",
                code_example="""import httpx

async with httpx.AsyncClient() as client:
    response = await client.get('https://api.github.com')
    print(response.json())""",
                pypi_url="https://pypi.org/project/httpx/",
                github_url="https://github.com/encode/httpx",
                documentation_url="https://www.python-httpx.org/"
            ),
            "keywords": ["http", "async", "api", "web", "http2", "modern"]
        },
        {
            "package": Package(
                id=None,
                name="beautifulsoup4",
                description="Library for parsing HTML and XML documents",
                category="web",
                install_command="pip install beautifulsoup4",
                code_example="""from bs4 import BeautifulSoup
import requests

html = requests.get('https://example.com').text
soup = BeautifulSoup(html, 'html.parser')
print(soup.title.string)""",
                pypi_url="https://pypi.org/project/beautifulsoup4/",
                github_url="https://www.crummy.com/software/BeautifulSoup/",
                documentation_url="https://www.crummy.com/software/BeautifulSoup/bs4/doc/"
            ),
            "keywords": ["html", "xml", "parsing", "scraping", "web scraping", "beautifulsoup"]
        },
        {
            "package": Package(
                id=None,
                name="flask",
                description="Lightweight web framework for building web applications",
                category="web",
                install_command="pip install flask",
                code_example="""from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()""",
                pypi_url="https://pypi.org/project/Flask/",
                github_url="https://github.com/pallets/flask",
                documentation_url="https://flask.palletsprojects.com/"
            ),
            "keywords": ["web", "framework", "api", "server", "web app", "rest api"]
        },
        {
            "package": Package(
                id=None,
                name="fastapi",
                description="Modern, fast web framework for building APIs with Python 3.7+",
                category="web",
                install_command="pip install fastapi uvicorn",
                code_example="""from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}""",
                pypi_url="https://pypi.org/project/fastapi/",
                github_url="https://github.com/tiangolo/fastapi",
                documentation_url="https://fastapi.tiangolo.com/"
            ),
            "keywords": ["web", "framework", "api", "fast", "modern", "rest", "async"]
        },
        
        # DATA SCIENCE & ANALYSIS
        {
            "package": Package(
                id=None,
                name="pandas",
                description="Powerful data manipulation and analysis library",
                category="data",
                install_command="pip install pandas",
                code_example="""import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30]
})
print(df)""",
                pypi_url="https://pypi.org/project/pandas/",
                github_url="https://github.com/pandas-dev/pandas",
                documentation_url="https://pandas.pydata.org/"
            ),
            "keywords": ["data", "dataframe", "analysis", "csv", "excel", "data manipulation"]
        },
        {
            "package": Package(
                id=None,
                name="numpy",
                description="Fundamental package for scientific computing with arrays",
                category="data",
                install_command="pip install numpy",
                code_example="""import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.mean())""",
                pypi_url="https://pypi.org/project/numpy/",
                github_url="https://github.com/numpy/numpy",
                documentation_url="https://numpy.org/doc/"
            ),
            "keywords": ["data", "arrays", "math", "scientific", "numerical", "matrix"]
        },
        {
            "package": Package(
                id=None,
                name="matplotlib",
                description="Comprehensive library for creating visualizations",
                category="data",
                install_command="pip install matplotlib",
                code_example="""import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.ylabel('Numbers')
plt.show()""",
                pypi_url="https://pypi.org/project/matplotlib/",
                github_url="https://github.com/matplotlib/matplotlib",
                documentation_url="https://matplotlib.org/"
            ),
            "keywords": ["visualization", "plotting", "charts", "graphs", "data viz"]
        },
        
        # CLI TOOLS
        {
            "package": Package(
                id=None,
                name="typer",
                description="Modern library for building CLI applications",
                category="cli",
                install_command="pip install typer",
                code_example="""import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    print(f"Hello {name}")

if __name__ == "__main__":
    app()""",
                pypi_url="https://pypi.org/project/typer/",
                github_url="https://github.com/tiangolo/typer",
                documentation_url="https://typer.tiangolo.com/"
            ),
            "keywords": ["cli", "command line", "terminal", "console", "commands"]
        },
        {
            "package": Package(
                id=None,
                name="rich",
                description="Library for rich text and beautiful formatting in terminal",
                category="cli",
                install_command="pip install rich",
                code_example="""from rich.console import Console

console = Console()
console.print("Hello", style="bold magenta")""",
                pypi_url="https://pypi.org/project/rich/",
                github_url="https://github.com/Textualize/rich",
                documentation_url="https://rich.readthedocs.io/"
            ),
            "keywords": ["cli", "terminal", "colors", "formatting", "console", "pretty print"]
        },
        
        # TESTING
        {
            "package": Package(
                id=None,
                name="pytest",
                description="Framework for writing and running tests",
                category="testing",
                install_command="pip install pytest",
                code_example="""def test_addition():
    assert 1 + 1 == 2

# Run with: pytest test_file.py""",
                pypi_url="https://pypi.org/project/pytest/",
                github_url="https://github.com/pytest-dev/pytest",
                documentation_url="https://docs.pytest.org/"
            ),
            "keywords": ["testing", "tests", "unit tests", "test framework"]
        },
        
        # UTILITIES
        {
            "package": Package(
                id=None,
                name="python-dotenv",
                description="Read key-value pairs from .env file and set them as environment variables",
                category="utilities",
                install_command="pip install python-dotenv",
                code_example="""from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')""",
                pypi_url="https://pypi.org/project/python-dotenv/",
                github_url="https://github.com/theskumar/python-dotenv",
                documentation_url="https://saurabh-kumar.com/python-dotenv/"
            ),
            "keywords": ["environment", "env", "config", "secrets", "configuration"]
        },
        
        # FILE HANDLING
        {
            "package": Package(
                id=None,
                name="openpyxl",
                description="Library to read/write Excel files",
                category="file",
                install_command="pip install openpyxl",
                code_example="""from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws['A1'] = 'Hello'
wb.save('example.xlsx')""",
                pypi_url="https://pypi.org/project/openpyxl/",
                github_url="https://foss.heptapod.net/openpyxl/openpyxl",
                documentation_url="https://openpyxl.readthedocs.io/"
            ),
            "keywords": ["excel", "xlsx", "spreadsheet", "file", "workbook"]
        },
        {
            "package": Package(
                id=None,
                name="pillow",
                description="Python Imaging Library for opening, manipulating, and saving images",
                category="file",
                install_command="pip install pillow",
                code_example="""from PIL import Image

img = Image.open('photo.jpg')
img = img.resize((300, 300))
img.save('resized.jpg')""",
                pypi_url="https://pypi.org/project/Pillow/",
                github_url="https://github.com/python-pillow/Pillow",
                documentation_url="https://pillow.readthedocs.io/"
            ),
            "keywords": ["image", "photo", "pictures", "graphics", "resize", "crop"]
        },
    ]
    
    print("Seeding database with packages...")
    
    for item in packages_data:
        try:
            package_id = db.add_package(item["package"])
            db.add_keywords(package_id, item["keywords"])
            print(f"[OK] Added: {item['package'].name}")
        except Exception as e:
            print(f"[ERROR] Failed to add {item['package'].name}: {e}")
    
    print(f"\nDatabase seeded successfully! Total packages: {len(packages_data)}")
    db.close()


if __name__ == "__main__":
    seed_database()
