"""
EXPANDED Seed Database - 35+ Packages
Windows-compatible version (no emojis)
Run this to expand your database from 14 to 35+ packages
"""
from packagepilot.database import Database
from packagepilot.models import Package


def seed_database():
    """Populate database with expanded package list."""
    
    db = Database()
    
    # List of packages to add
    packages_data = [
        # ==================== WEB & HTTP ====================
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
        {
            "package": Package(
                id=None,
                name="django",
                description="High-level Python web framework for rapid development",
                category="web",
                install_command="pip install django",
                code_example="""# Create project: django-admin startproject mysite
# Run server: python manage.py runserver

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django!")""",
                pypi_url="https://pypi.org/project/Django/",
                github_url="https://github.com/django/django",
                documentation_url="https://docs.djangoproject.com/"
            ),
            "keywords": ["web", "framework", "mvc", "orm", "full stack"]
        },
        {
            "package": Package(
                id=None,
                name="selenium",
                description="Browser automation tool for testing and web scraping",
                category="web",
                install_command="pip install selenium",
                code_example="""from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.python.org')
print(driver.title)
driver.quit()""",
                pypi_url="https://pypi.org/project/selenium/",
                github_url="https://github.com/SeleniumHQ/selenium",
                documentation_url="https://www.selenium.dev/documentation/"
            ),
            "keywords": ["automation", "browser", "testing", "scraping", "web automation"]
        },
        {
            "package": Package(
                id=None,
                name="scrapy",
                description="Fast high-level web crawling and scraping framework",
                category="web",
                install_command="pip install scrapy",
                code_example="""import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {'text': quote.css('span.text::text').get()}""",
                pypi_url="https://pypi.org/project/Scrapy/",
                github_url="https://github.com/scrapy/scrapy",
                documentation_url="https://docs.scrapy.org/"
            ),
            "keywords": ["scraping", "crawler", "spider", "web scraping", "data extraction"]
        },
        
        # ==================== DATA SCIENCE ====================
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
            "keywords": ["data", "dataframe", "analysis", "csv", "excel"]
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
print(f"Mean: {arr.mean()}")""",
                pypi_url="https://pypi.org/project/numpy/",
                github_url="https://github.com/numpy/numpy",
                documentation_url="https://numpy.org/doc/"
            ),
            "keywords": ["data", "arrays", "math", "scientific", "numerical"]
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
            "keywords": ["visualization", "plotting", "charts", "graphs"]
        },
        {
            "package": Package(
                id=None,
                name="seaborn",
                description="Statistical data visualization based on matplotlib",
                category="data",
                install_command="pip install seaborn",
                code_example="""import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.show()""",
                pypi_url="https://pypi.org/project/seaborn/",
                github_url="https://github.com/mwaskom/seaborn",
                documentation_url="https://seaborn.pydata.org/"
            ),
            "keywords": ["visualization", "statistical", "charts", "graphs"]
        },
        {
            "package": Package(
                id=None,
                name="scikit-learn",
                description="Machine learning library with classification, regression, clustering",
                category="data",
                install_command="pip install scikit-learn",
                code_example="""from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit([[1], [2], [3]], [2, 4, 6])
print(model.predict([[4]]))""",
                pypi_url="https://pypi.org/project/scikit-learn/",
                github_url="https://github.com/scikit-learn/scikit-learn",
                documentation_url="https://scikit-learn.org/"
            ),
            "keywords": ["machine learning", "ml", "ai", "classification", "regression"]
        },
        {
            "package": Package(
                id=None,
                name="plotly",
                description="Interactive graphing library for Python",
                category="data",
                install_command="pip install plotly",
                code_example="""import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.show()""",
                pypi_url="https://pypi.org/project/plotly/",
                github_url="https://github.com/plotly/plotly.py",
                documentation_url="https://plotly.com/python/"
            ),
            "keywords": ["visualization", "interactive", "charts", "dashboard"]
        },
        
        # ==================== CLI TOOLS ====================
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
            "keywords": ["cli", "command line", "terminal", "console"]
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
            "keywords": ["cli", "terminal", "colors", "formatting", "console"]
        },
        {
            "package": Package(
                id=None,
                name="click",
                description="Package for creating command line interfaces",
                category="cli",
                install_command="pip install click",
                code_example="""import click

@click.command()
@click.option('--name', prompt='Your name')
def hello(name):
    click.echo(f'Hello {name}!')

if __name__ == '__main__':
    hello()""",
                pypi_url="https://pypi.org/project/click/",
                github_url="https://github.com/pallets/click",
                documentation_url="https://click.palletsprojects.com/"
            ),
            "keywords": ["cli", "command line", "arguments", "options"]
        },
        {
            "package": Package(
                id=None,
                name="tqdm",
                description="Fast, extensible progress bar for loops and iterations",
                category="cli",
                install_command="pip install tqdm",
                code_example="""from tqdm import tqdm
import time

for i in tqdm(range(100)):
    time.sleep(0.01)""",
                pypi_url="https://pypi.org/project/tqdm/",
                github_url="https://github.com/tqdm/tqdm",
                documentation_url="https://tqdm.github.io/"
            ),
            "keywords": ["progress", "bar", "cli", "loading"]
        },
        
        # ==================== TESTING ====================
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
            "keywords": ["testing", "tests", "unit tests"]
        },
        {
            "package": Package(
                id=None,
                name="unittest",
                description="Built-in Python unit testing framework",
                category="testing",
                install_command="# Built-in, no installation needed",
                code_example="""import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()""",
                pypi_url="https://docs.python.org/3/library/unittest.html",
                documentation_url="https://docs.python.org/3/library/unittest.html"
            ),
            "keywords": ["testing", "tests", "built-in"]
        },
        {
            "package": Package(
                id=None,
                name="coverage",
                description="Code coverage measurement for Python",
                category="testing",
                install_command="pip install coverage",
                code_example="""# Run tests with coverage:
# coverage run -m pytest
# coverage report
# coverage html""",
                pypi_url="https://pypi.org/project/coverage/",
                github_url="https://github.com/nedbat/coveragepy",
                documentation_url="https://coverage.readthedocs.io/"
            ),
            "keywords": ["testing", "coverage", "test coverage"]
        },
        
        # ==================== FILE HANDLING ====================
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
            "keywords": ["excel", "xlsx", "spreadsheet", "file"]
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
            "keywords": ["image", "photo", "pictures", "resize"]
        },
        {
            "package": Package(
                id=None,
                name="PyPDF2",
                description="Library for reading and manipulating PDF files",
                category="file",
                install_command="pip install PyPDF2",
                code_example="""from PyPDF2 import PdfReader

reader = PdfReader('document.pdf')
page = reader.pages[0]
text = page.extract_text()
print(text)""",
                pypi_url="https://pypi.org/project/PyPDF2/",
                github_url="https://github.com/py-pdf/PyPDF2",
                documentation_url="https://pypdf2.readthedocs.io/"
            ),
            "keywords": ["pdf", "document", "file", "reader"]
        },
        {
            "package": Package(
                id=None,
                name="pathlib",
                description="Built-in object-oriented filesystem paths",
                category="file",
                install_command="# Built-in, no installation needed",
                code_example="""from pathlib import Path

p = Path('my_folder')
p.mkdir(exist_ok=True)

for file in p.glob('*.txt'):
    print(file.name)""",
                pypi_url="https://docs.python.org/3/library/pathlib.html",
                documentation_url="https://docs.python.org/3/library/pathlib.html"
            ),
            "keywords": ["file", "path", "directory", "built-in"]
        },
        
        # ==================== UTILITIES ====================
        {
            "package": Package(
                id=None,
                name="python-dotenv",
                description="Read key-value pairs from .env file",
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
            "keywords": ["environment", "env", "config", "secrets"]
        },
        {
            "package": Package(
                id=None,
                name="schedule",
                description="Simple library for scheduling Python functions",
                category="utilities",
                install_command="pip install schedule",
                code_example="""import schedule
import time

def job():
    print("Working...")

schedule.every(10).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)""",
                pypi_url="https://pypi.org/project/schedule/",
                github_url="https://github.com/dbader/schedule",
                documentation_url="https://schedule.readthedocs.io/"
            ),
            "keywords": ["scheduling", "cron", "jobs", "automation"]
        },
        {
            "package": Package(
                id=None,
                name="loguru",
                description="Library which aims to make logging in Python enjoyable",
                category="utilities",
                install_command="pip install loguru",
                code_example="""from loguru import logger

logger.info("This is an info message")
logger.warning("This is a warning")
logger.error("This is an error")""",
                pypi_url="https://pypi.org/project/loguru/",
                github_url="https://github.com/Delgan/loguru",
                documentation_url="https://loguru.readthedocs.io/"
            ),
            "keywords": ["logging", "log", "debug", "errors"]
        },
        {
            "package": Package(
                id=None,
                name="pydantic",
                description="Data validation using Python type hints",
                category="utilities",
                install_command="pip install pydantic",
                code_example="""from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name='Alice', age=25)""",
                pypi_url="https://pypi.org/project/pydantic/",
                github_url="https://github.com/pydantic/pydantic",
                documentation_url="https://docs.pydantic.dev/"
            ),
            "keywords": ["validation", "data", "models", "type hints"]
        },
        
        # ==================== DATABASE ====================
        {
            "package": Package(
                id=None,
                name="sqlalchemy",
                description="SQL toolkit and Object-Relational Mapping (ORM) library",
                category="database",
                install_command="pip install sqlalchemy",
                code_example="""from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)""",
                pypi_url="https://pypi.org/project/SQLAlchemy/",
                github_url="https://github.com/sqlalchemy/sqlalchemy",
                documentation_url="https://docs.sqlalchemy.org/"
            ),
            "keywords": ["database", "sql", "orm", "sqlite", "postgres"]
        },
        {
            "package": Package(
                id=None,
                name="pymongo",
                description="Python driver for MongoDB",
                category="database",
                install_command="pip install pymongo",
                code_example="""from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['mydatabase']
collection = db['users']

collection.insert_one({'name': 'Alice', 'age': 25})""",
                pypi_url="https://pypi.org/project/pymongo/",
                github_url="https://github.com/mongodb/mongo-python-driver",
                documentation_url="https://pymongo.readthedocs.io/"
            ),
            "keywords": ["database", "mongodb", "nosql", "document"]
        },
        {
            "package": Package(
                id=None,
                name="redis",
                description="Python client for Redis key-value store",
                category="database",
                install_command="pip install redis",
                code_example="""import redis

r = redis.Redis(host='localhost', port=6379)
r.set('key', 'value')
print(r.get('key'))""",
                pypi_url="https://pypi.org/project/redis/",
                github_url="https://github.com/redis/redis-py",
                documentation_url="https://redis-py.readthedocs.io/"
            ),
            "keywords": ["database", "redis", "cache", "key-value"]
        },
    ]
    
    print("Seeding database with EXPANDED package list...")
    print("")
    
    added = 0
    skipped = 0
    
    for item in packages_data:
        try:
            package_id = db.add_package(item["package"])
            db.add_keywords(package_id, item["keywords"])
            print(f"[OK] Added: {item['package'].name}")
            added += 1
        except Exception as e:
            print(f"[SKIP] {item['package'].name} (already exists)")
            skipped += 1
    
    print("")
    print("="*60)
    print("Database seeded successfully!")
    print(f"  Added: {added} packages")
    print(f"  Skipped: {skipped} packages")
    print(f"  Total in database: {len(db.get_all_packages())}")
    print("="*60)
    db.close()


if __name__ == "__main__":
    seed_database()
