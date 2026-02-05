"""
Search functionality for PackagePilot
"""
from typing import List
from .models import Package
from .database import Database


def search_packages(query: str, db: Database) -> List[Package]:
    """
    Search for packages based on a query string.
    
    This function performs intelligent searching by:
    1. Direct database search (name, description, keywords)
    2. Ranking results by relevance
    
    Args:
        query: Search query string
        db: Database instance
        
    Returns:
        List of Package objects, ranked by relevance
    """
    # Get initial results from database
    results = db.search_packages(query)
    
    # Additional ranking logic can be added here
    # For now, the database query already handles basic ranking
    
    return results


def rank_results(packages: List[Package], query: str) -> List[Package]:
    """
    Rank search results by relevance.
    
    Args:
        packages: List of Package objects
        query: Original search query
        
    Returns:
        Sorted list of packages by relevance score
    """
    query_lower = query.lower()
    
    def calculate_score(package: Package) -> int:
        """Calculate relevance score for a package."""
        score = 0
        
        # Exact name match - highest priority
        if package.name.lower() == query_lower:
            score += 100
        
        # Name contains query
        elif query_lower in package.name.lower():
            score += 50
        
        # Description contains query
        if query_lower in package.description.lower():
            score += 30
        
        # Category match
        if query_lower in package.category.lower():
            score += 20
        
        return score
    
    # Sort by score (highest first)
    ranked = sorted(packages, key=calculate_score, reverse=True)
    return ranked
