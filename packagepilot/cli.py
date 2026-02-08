"""
ENHANCED Command-line interface for PackagePilot
Added: search suggestions, stats command, better UX
Windows-compatible version (no emojis)
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from packagepilot.database import Database
from packagepilot.search import search_packages, get_search_suggestions


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
    """Handle search command with suggestions."""
    db = Database()
    results = search_packages(args.query, db)
    
    if not results:
        print(f"\n[!] No packages found for '{args.query}'")
        
        # Try to provide suggestions
        suggestions = get_search_suggestions(args.query)
        
        if suggestions:
            print("\n[TIP] Did you mean to search for:")
            for suggestion in suggestions:
                print(f"      - {suggestion}")
            print(f"\n      Try: packagepilot search \"{suggestions[0]}\"")
        else:
            print("\n[TIP] Try:")
            print("      - Using different keywords")
            print("      - packagepilot categories (see all categories)")
            print("      - packagepilot list (see all packages)")
        
        db.close()
        return
    
    print(f"\n[FOUND] {len(results)} package(s) for '{args.query}':")
    
    # Show top results
    display_count = min(5, len(results))
    for package in results[:display_count]:
        print(format_package_output(package, show_full=False))
    
    if len(results) > display_count:
        print(f"\n... and {len(results) - display_count} more results")
        print(f"\n[TIP] Refine search or use 'packagepilot info <name>' for details")
    else:
        print("\n[TIP] Use 'packagepilot info <name>' for full details")
    
    db.close()


def cmd_info(args):
    """Handle info command."""
    db = Database()
    package = db.get_package_by_name(args.package_name)
    
    if not package:
        print(f"\n[!] Package '{args.package_name}' not found")
        
        # Try fuzzy search for similar names
        all_packages = db.get_all_packages()
        similar = [p for p in all_packages if args.package_name.lower() in p.name.lower()]
        
        if similar:
            print("\n[TIP] Did you mean one of these?")
            for pkg in similar[:3]:
                print(f"      - {pkg.name}")
        else:
            print("\n[TIP] Try 'packagepilot search <keyword>' to find packages")
        
        db.close()
        return
    
    print(format_package_output(package, show_full=True))
    db.close()


def cmd_category(args):
    """Handle category command."""
    db = Database()
    packages = db.get_packages_by_category(args.category_name)
    
    if not packages:
        print(f"\n[!] No packages in category '{args.category_name}'")
        print("\n[TIP] Available categories:")
        
        # Get all unique categories
        all_packages = db.get_all_packages()
        categories = sorted(set(p.category for p in all_packages))
        for cat in categories:
            print(f"      - {cat}")
        
        db.close()
        return
    
    print(f"\n[{args.category_name.upper()}] {len(packages)} packages:\n")
    
    for package in packages:
        print(f"  * {package.name}")
        print(f"    {package.description}")
        print("")
    
    print("[TIP] Use 'packagepilot info <name>' for details")
    db.close()


def cmd_categories(args):
    """List all categories with counts."""
    db = Database()
    all_packages = db.get_all_packages()
    
    # Count packages per category
    category_counts = {}
    for package in all_packages:
        category_counts[package.category] = category_counts.get(package.category, 0) + 1
    
    print("\n[CATEGORIES] Available:\n")
    
    for category in sorted(category_counts.keys()):
        count = category_counts[category]
        print(f"  {category:12} ({count:2} packages)")
    
    print(f"\n[TIP] Use 'packagepilot category <name>' to browse")
    print(f"      Total packages: {len(all_packages)}")
    
    db.close()


def cmd_list(args):
    """List all packages."""
    db = Database()
    packages = db.get_all_packages()
    
    if not packages:
        print("\n[!] No packages in database. Run seed_database.py first!")
        db.close()
        return
    
    print(f"\n[ALL PACKAGES] ({len(packages)} total):\n")
    
    # Group by category
    by_category = {}
    for package in packages:
        if package.category not in by_category:
            by_category[package.category] = []
        by_category[package.category].append(package)
    
    for category, pkgs in sorted(by_category.items()):
        print(f"\n{category.upper()} ({len(pkgs)}):")
        for pkg in sorted(pkgs, key=lambda p: p.name):
            desc = pkg.description[:60] + "..." if len(pkg.description) > 60 else pkg.description
            print(f"  * {pkg.name:20} - {desc}")
    
    db.close()


def cmd_stats(args):
    """Show database statistics - NEW COMMAND!"""
    db = Database()
    packages = db.get_all_packages()
    
    # Category breakdown
    by_category = {}
    for package in packages:
        by_category[package.category] = by_category.get(package.category, 0) + 1
    
    print("\n[STATISTICS] PackagePilot Database")
    print("="*60)
    print(f"\nTotal Packages: {len(packages)}")
    print(f"\nPackages by Category:")
    
    # Sort by count (highest first)
    for category, count in sorted(by_category.items(), key=lambda x: x[1], reverse=True):
        # Simple bar chart using # symbols
        bar = "#" * count
        print(f"  {category:12} {bar} {count}")
    
    print("\n" + "="*60)
    db.close()


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="packagepilot",
        description="PackagePilot - Your Python package discovery assistant",
        epilog="Examples:\n"
               "  packagepilot search 'web scraping'\n"
               "  packagepilot info requests\n"
               "  packagepilot category web\n"
               "  packagepilot stats\n",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Search command
    search_parser = subparsers.add_parser("search", help="Search for packages")
    search_parser.add_argument("query", help="Search query")
    search_parser.set_defaults(func=cmd_search)
    
    # Info command
    info_parser = subparsers.add_parser("info", help="Get detailed package info")
    info_parser.add_argument("package_name", help="Package name")
    info_parser.set_defaults(func=cmd_info)
    
    # Category command
    category_parser = subparsers.add_parser("category", help="List packages in category")
    category_parser.add_argument("category_name", help="Category name")
    category_parser.set_defaults(func=cmd_category)
    
    # Categories command
    categories_parser = subparsers.add_parser("categories", help="List all categories")
    categories_parser.set_defaults(func=cmd_categories)
    
    # List command
    list_parser = subparsers.add_parser("list", help="List all packages")
    list_parser.set_defaults(func=cmd_list)
    
    # Stats command (NEW!)
    stats_parser = subparsers.add_parser("stats", help="Show database statistics")
    stats_parser.set_defaults(func=cmd_stats)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        print("\n[TIP] Quick start:")
        print("      packagepilot search 'web scraping'")
        print("      packagepilot categories")
        return
    
    # Call the appropriate command function
    args.func(args)


if __name__ == "__main__":
    main()
