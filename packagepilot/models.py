"""
Data models for PackagePilot
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Package:
    """
    Represents a Python package with its metadata and usage information.
    
    Attributes:
        id: Unique identifier for the package
        name: Package name (e.g., 'requests')
        description: Short description of what the package does
        category: Category (e.g., 'web', 'data', 'testing')
        install_command: pip install command
        code_example: Basic usage example
        pypi_url: Link to PyPI page
        github_url: Link to GitHub repo (optional)
        documentation_url: Link to documentation (optional)
    """
    id: Optional[int]
    name: str
    description: str
    category: str
    install_command: str
    code_example: str
    pypi_url: str
    github_url: Optional[str] = None
    documentation_url: Optional[str] = None
    
    def __str__(self) -> str:
        """Return a formatted string representation of the package."""
        return f"{self.name} - {self.description}"
