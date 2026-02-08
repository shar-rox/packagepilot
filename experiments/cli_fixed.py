"""
Command-line interface for PackagePilot
Windows-compatible version (no emojis)
"""
import argparse
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from packagepilot.database import Database
from packagepilot.search import search_packages


def format_package_output(package, show_full=False):
    """Format package information for display."""
    output = []
    output.append(f"\n{'='*70}")
    output.append(f"PACKAGE: {package.name}")
    output.append(f"{'='*70}")
    output.append(f"\n{package.description}")
    output.append(f"\nCategory: {package.category}")
    output.append(f"Install: {package.install_command}")
    
    if show_full:
        output.append(f"\n{'-'*70}")
        output.append("Code Example:")
        output.append(f"{'-'*70}")
        output.append(package.code_example)
        
        output.append(f"\n{'-'*70}")
        output.append("Links:")
        output.append(f"{'-'*70}")
        output.append(f"PyPI: {package.pypi_url}")
        if package.documentation_url:
            output.append(f"Docs: {package.documentation_url}")
        if package.github_url:
            output.append(f"GitHub: {package.github_url}")
    
    return "\n".join(output)


def cmd_search(args):
    """Handle search command."""
    db = Database()
    results = search_packages(args.query, db)
    
    if not results:
        print(f"\nNo packages found for '{args.query}'")
        print("\nTry:")
        print("  - Using different keywords")
        print("  - Checking the category list with: packagepilot categories")
        db.close()
        return
    
    print(f"\nFound {len(results)} package(s) for '{args.query}':")
    
    for i, package in enumerate(results[:5], 1):
        print(format_package_output(package, show_full=False))
    
    if len(results) > 5:
        print(f"\n... and {len(results) - 5} more results")
    
    print("\nTip: Use 'packagepilot info <package-name>' for full details")
    db.close()


def cmd_info(args):
    """Handle info command."""
    db = Database()
    package = db.get_package_by_name(args.package_name)
    
    if not package:
        print(f"\nPackage '{args.package_name}' not found in database")
        db.close()
        return
    
    print(format_package_output(package, show_full=True))
    db.close()


def cmd_category(args):
    """Handle category command."""
    db = Database()
    packages = db.get_packages_by_category(args.category_name)
    
    if not packages:
        print(f"\nNo packages found in category '{args.category_name}'")
        print("\nAvailable categories: web, data, cli, testing, file, utilities")
        db.close()
        return
    
    print(f"\nPackages in '{args.category_name}' category:")
    
    for package in packages:
        print(f"\n  * {package.name}")
        print(f"    {package.description}")
    
    print(f"\nTip: Use 'packagepilot info <package-name>' for details")
    db.close()


def cmd_categories(args):
    """List all available categories."""
    print("\nAvailable Categories:\n")
    
    categories = {
        "web": "HTTP clients, web frameworks, scraping tools",
        "data": "Data analysis, visualization, manipulation",
        "cli": "Command-line tools and utilities",
        "testing": "Testing frameworks and tools",
        "file": "File handling and processing",
        "utilities": "Configuration, environment management"
    }
    
    for category, description in categories.items():
        print(f"  {category:12} - {description}")
    
    print("\nTip: Use 'packagepilot category <name>' to see packages")


def cmd_list(args):
    """List all packages."""
    db = Database()
    packages = db.get_all_packages()
    
    if not packages:
        print("\nNo packages in database. Run seed_database.py first!")
        db.close()
        return
    
    print(f"\nAll Packages ({len(packages)}):\n")
    
    # Group by category
    by_category = {}
    for package in packages:
        if package.category not in by_category:
            by_category[package.category] = []
        by_category[package.category].append(package)
    
    for category, pkgs in sorted(by_category.items()):
        print(f"\n{category.upper()}:")
        for pkg in pkgs:
            print(f"  * {pkg.name:20} - {pkg.description}")
    
    db.close()


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="packagepilot",
        description="PackagePilot - Your Python package discovery assistant",
        epilog="Examples:\n"
               "  packagepilot search 'make HTTP requests'\n"
               "  packagepilot info requests\n"
               "  packagepilot category web\n",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Search command
    search_parser = subparsers.add_parser("search", help="Search for packages")
    search_parser.add_argument("query", help="Search query")
    search_parser.set_defaults(func=cmd_search)
    
    # Info command
    info_parser = subparsers.add_parser("info", help="Get detailed info about a package")
    info_parser.add_argument("package_name", help="Name of the package")
    info_parser.set_defaults(func=cmd_info)
    
    # Category command
    category_parser = subparsers.add_parser("category", help="List packages in a category")
    category_parser.add_argument("category_name", help="Category name")
    category_parser.set_defaults(func=cmd_category)
    
    # Categories command
    categories_parser = subparsers.add_parser("categories", help="List all categories")
    categories_parser.set_defaults(func=cmd_categories)
    
    # List command
    list_parser = subparsers.add_parser("list", help="List all packages")
    list_parser.set_defaults(func=cmd_list)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Call the appropriate command function
    args.func(args)


if __name__ == "__main__":
    main()
