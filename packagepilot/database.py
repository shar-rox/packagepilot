"""
Database operations for PackagePilot
"""
import sqlite3
from pathlib import Path
from typing import List, Optional
from .models import Package


class Database:
    """Handles all database operations for PackagePilot."""
    
    def __init__(self, db_path: str = None):
        """
        Initialize database connection.
        
        Args:
            db_path: Path to SQLite database file. If None, uses default location.
        """
        if db_path is None:
            # Default to data/packages.db in the package directory
            package_dir = Path(__file__).parent
            db_path = package_dir / "data" / "packages.db"
        
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(str(self.db_path))
        self.connection.row_factory = sqlite3.Row  # Access columns by name
        self._create_tables()
    
    def _create_tables(self):
        """Create database tables if they don't exist."""
        cursor = self.connection.cursor()
        
        # Create packages table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS packages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                description TEXT NOT NULL,
                category TEXT NOT NULL,
                install_command TEXT NOT NULL,
                code_example TEXT NOT NULL,
                pypi_url TEXT NOT NULL,
                github_url TEXT,
                documentation_url TEXT
            )
        """)
        
        # Create keywords table for better searching
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS keywords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                package_id INTEGER NOT NULL,
                keyword TEXT NOT NULL,
                FOREIGN KEY (package_id) REFERENCES packages (id)
            )
        """)
        
        self.connection.commit()
    
    def add_package(self, package: Package) -> int:
        """
        Add a new package to the database.
        
        Args:
            package: Package object to add
            
        Returns:
            The ID of the newly added package
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO packages (name, description, category, install_command, 
                                 code_example, pypi_url, github_url, documentation_url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            package.name,
            package.description,
            package.category,
            package.install_command,
            package.code_example,
            package.pypi_url,
            package.github_url,
            package.documentation_url
        ))
        self.connection.commit()
        return cursor.lastrowid
    
    def add_keywords(self, package_id: int, keywords: List[str]):
        """
        Add search keywords for a package.
        
        Args:
            package_id: ID of the package
            keywords: List of keywords to associate with the package
        """
        cursor = self.connection.cursor()
        for keyword in keywords:
            cursor.execute("""
                INSERT INTO keywords (package_id, keyword)
                VALUES (?, ?)
            """, (package_id, keyword.lower()))
        self.connection.commit()
    
    def search_packages(self, query: str) -> List[Package]:
        """
        Search for packages by query string.
        
        Args:
            query: Search query (searches in name, description, category, keywords)
            
        Returns:
            List of matching Package objects
        """
        cursor = self.connection.cursor()
        search_term = f"%{query.lower()}%"
        
        # Search in package name, description, category, and keywords
        cursor.execute("""
            SELECT DISTINCT p.* FROM packages p
            LEFT JOIN keywords k ON p.id = k.package_id
            WHERE LOWER(p.name) LIKE ?
               OR LOWER(p.description) LIKE ?
               OR LOWER(p.category) LIKE ?
               OR LOWER(k.keyword) LIKE ?
            ORDER BY 
                CASE 
                    WHEN LOWER(p.name) LIKE ? THEN 1
                    WHEN LOWER(p.description) LIKE ? THEN 2
                    ELSE 3
                END
        """, (search_term, search_term, search_term, search_term, search_term, search_term))
        
        rows = cursor.fetchall()
        return [self._row_to_package(row) for row in rows]
    
    def get_package_by_name(self, name: str) -> Optional[Package]:
        """
        Get a specific package by its name.
        
        Args:
            name: Package name
            
        Returns:
            Package object or None if not found
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM packages WHERE LOWER(name) = ?", (name.lower(),))
        row = cursor.fetchone()
        return self._row_to_package(row) if row else None
    
    def get_all_packages(self) -> List[Package]:
        """
        Get all packages in the database.
        
        Returns:
            List of all Package objects
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM packages ORDER BY name")
        rows = cursor.fetchall()
        return [self._row_to_package(row) for row in rows]
    
    def get_packages_by_category(self, category: str) -> List[Package]:
        """
        Get all packages in a specific category.
        
        Args:
            category: Category name
            
        Returns:
            List of Package objects in that category
        """
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM packages WHERE LOWER(category) = ? ORDER BY name",
            (category.lower(),)
        )
        rows = cursor.fetchall()
        return [self._row_to_package(row) for row in rows]
    
    def _row_to_package(self, row: sqlite3.Row) -> Package:
        """
        Convert a database row to a Package object.
        
        Args:
            row: SQLite row object
            
        Returns:
            Package object
        """
        return Package(
            id=row["id"],
            name=row["name"],
            description=row["description"],
            category=row["category"],
            install_command=row["install_command"],
            code_example=row["code_example"],
            pypi_url=row["pypi_url"],
            github_url=row["github_url"],
            documentation_url=row["documentation_url"]
        )
    
    def close(self):
        """Close the database connection."""
        self.connection.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - closes connection."""
        self.close()
