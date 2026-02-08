"""
IMPROVED Search functionality for PackagePilot
Multi-word query support + better ranking
Windows-compatible version (no emojis)
"""
from typing import List
from .models import Package
from .database import Database


def search_packages(query: str, db: Database) -> List[Package]:
    """
    Search for packages with improved multi-word support.
    
    Example: "web scraping" will find beautifulsoup4, scrapy, selenium
    
    Args:
        query: Search query (can be multiple words)
        db: Database instance
        
    Returns:
        List of Package objects, ranked by relevance
    """
    # Get initial results from database
    results = db.search_packages(query)
    
    # If no results with full query, try individual words
    if not results and ' ' in query:
        words = query.split()
        all_results = []
        
        for word in words:
            if len(word) > 2:  # Skip very short words
                word_results = db.search_packages(word)
                all_results.extend(word_results)
        
        # Remove duplicates while preserving order
        seen = set()
        results = []
        for pkg in all_results:
            if pkg.id not in seen:
                seen.add(pkg.id)
                results.append(pkg)
    
    # Rank results by relevance
    if results:
        results = rank_results(results, query)
    
    return results


def rank_results(packages: List[Package], query: str) -> List[Package]:
    """
    Rank search results by relevance.
    
    Scoring system:
    - Exact name match: 100 points
    - Name contains query: 50 points
    - Description starts with query: 40 points
    - Description contains query: 30 points
    - Category match: 20 points
    - Each word match: 10 points
    
    Args:
        packages: List of Package objects
        query: Original search query
        
    Returns:
        Sorted list by relevance (highest first)
    """
    query_lower = query.lower()
    query_words = query_lower.split()
    
    def calculate_score(package: Package) -> int:
        """Calculate relevance score for a package."""
        score = 0
        
        name_lower = package.name.lower()
        desc_lower = package.description.lower()
        category_lower = package.category.lower()
        
        # Exact name match - highest priority
        if name_lower == query_lower:
            score += 100
        
        # Name contains full query
        elif query_lower in name_lower:
            score += 50
        
        # Description starts with query
        if desc_lower.startswith(query_lower):
            score += 40
        
        # Description contains full query
        elif query_lower in desc_lower:
            score += 30
        
        # Category match
        if query_lower in category_lower:
            score += 20
        
        # Individual word matches
        for word in query_words:
            if len(word) > 2:
                if word in desc_lower:
                    score += 10
                if word in name_lower:
                    score += 15
        
        return score
    
    # Sort by score (highest first)
    ranked = sorted(packages, key=calculate_score, reverse=True)
    return ranked


def get_search_suggestions(query: str) -> List[str]:
    """
    Suggest alternative search terms if no results found.
    
    Args:
        query: Original search query
        
    Returns:
        List of suggested search terms
    """
    suggestions = []
    
    # Common synonyms and related terms
    term_mapping = {
        'http': ['web', 'api', 'requests'],
        'web': ['http', 'html', 'scraping'],
        'scrape': ['beautifulsoup', 'selenium', 'scrapy'],
        'scraping': ['beautifulsoup', 'selenium', 'scrapy'],
        'api': ['rest', 'http', 'web', 'fastapi'],
        'database': ['sql', 'orm', 'mongo'],
        'db': ['database', 'sql', 'orm'],
        'test': ['testing', 'pytest', 'unittest'],
        'chart': ['plot', 'visualization', 'graph'],
        'plot': ['chart', 'visualization', 'matplotlib'],
        'viz': ['visualization', 'plot', 'chart'],
        'ml': ['machine learning', 'ai', 'scikit'],
        'ai': ['machine learning', 'ml', 'neural'],
        'excel': ['spreadsheet', 'openpyxl', 'xlsx'],
        'image': ['photo', 'picture', 'pillow'],
        'pdf': ['document', 'pypdf'],
        'cli': ['command', 'terminal', 'console'],
        'async': ['asyncio', 'concurrent', 'httpx'],
    }
    
    # Check if query matches any known terms
    query_lower = query.lower()
    for key, values in term_mapping.items():
        if key in query_lower:
            suggestions.extend(values)
    
    # Remove duplicates and the original query
    suggestions = list(set(suggestions))
    if query_lower in suggestions:
        suggestions.remove(query_lower)
    
    return suggestions[:3]  # Return top 3
