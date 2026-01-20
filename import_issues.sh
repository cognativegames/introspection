#!/usr/bin/env python3
"""
GitHub Issues Import Script for Introspection
Reads todo.csv and creates GitHub issues using gh CLI

Prerequisites:
1. Install GitHub CLI: https://cli.github.com/
2. Authenticate: gh auth login
3. Install Python 3.6+
4. Place todo.csv in the same directory as this script

Usage: python3 import_issues.py
"""

import csv
import subprocess
import sys
import time
from pathlib import Path

# Configuration
CSV_FILE = "todo.csv"

# Colors for output
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
NC = '\033[0m'  # No Color

def print_color(text, color):
    print(f"{color}{text}{NC}")

def check_gh_cli():
    """Check if gh CLI is installed and authenticated"""
    try:
        subprocess.run(['gh', '--version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print_color("Error: GitHub CLI (gh) is not installed", RED)
        print("Install from: https://cli.github.com/")
        sys.exit(1)
    
    try:
        subprocess.run(['gh', 'auth', 'status'], capture_output=True, check=True)
    except subprocess.CalledProcessError:
        print_color("Error: Not authenticated with GitHub CLI", RED)
        print("Run: gh auth login")
        sys.exit(1)

def get_repo():
    """Get current repository"""
    try:
        result = subprocess.run(
            ['gh', 'repo', 'view', '--json', 'nameWithOwner', '-q', '.nameWithOwner'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        print_color("Error: Could not auto-detect repository", RED)
        print("Run this script from within a git repository")
        sys.exit(1)

def create_issue(repo, issue_data):
    """Create a single GitHub issue"""
    title = issue_data['Title']
    description = issue_data['Description']
    labels = issue_data['Labels']
    milestone = issue_data['Milestone']
    epic = issue_data['Epic']
    effort = issue_data['Effort Hours']
    priority = issue_data['Priority']
    dependencies = issue_data['Dependencies']
    
    # Build issue body with metadata
    body = f"""{description}

---
**Epic:** {epic}
**Effort:** {effort} hours
**Priority:** {priority}
**Dependencies:** {dependencies}
**Milestone:** {milestone}"""
    
    # Prepare gh command
    cmd = [
        'gh', 'issue', 'create',
        '--repo', repo,
        '--title', title,
        '--body', body
    ]
    
    # Add labels if present
    if labels and labels.strip():
        for label in labels.split(','):
            cmd.extend(['--label', label.strip()])
    
    # Add milestone if present
    if milestone and milestone.strip() and milestone != "Optional":
        cmd.extend(['--milestone', milestone.strip()])
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def create_labels(repo):
    """Create all required labels"""
    labels = {
        # Type labels
        'feature': 'a2eeef',
        'bug': 'd73a4a',
        'content': '0e8a16',
        'writing': '5319e7',
        'art': 'fbca04',
        'audio': 'f9d0c4',
        'placeholder': 'c5def5',
        'testing': 'e99695',
        'documentation': '0075ca',
        
        # Priority labels
        'priority-critical': 'b60205',
        'priority-high': 'd93f0b',
        'priority-medium': 'fbca04',
        'priority-low': '0e8a16',
        
        # System labels
        'setup': '1d76db',
        'infrastructure': '5319e7',
        'core-mechanic': 'c5def5',
        'optimization': 'bfdadc',
        'accessibility': '84b6eb',
        
        # Content labels
        'nsfw': 'd73a4a',
        'sensitive-content': 'b60205',
        'dark-content': '5a1f00',
        
        # Other
        'marketing': 'd4c5f9',
        'community': 'c2e0c6',
        'distribution': 'bfd4f2',
        'support': 'fef2c0',
        'release': 'd93f0b',
        'polish': 'c5def5',
        'vfx': 'fbca04',
        'music': 'f9d0c4',
        'sfx': 'e99695',
        'ui': '84b6eb',
        'analytics': 'bfdadc',
        'technical': '5319e7',
        'data': '1d76db'
    }
    
    print("Creating labels...")
    created = 0
    exists = 0
    
    for name, color in labels.items():
        try:
            subprocess.run(
                ['gh', 'label', 'create', name, '--color', color, '--repo', repo],
                capture_output=True,
                check=True
            )
            created += 1
            print(f"  ✓ Created label: {name}")
        except subprocess.CalledProcessError as e:
            if 'already exists' in e.stderr.decode():
                exists += 1
            else:
                print(f"  ✗ Failed to create label {name}: {e.stderr.decode()}")
    
    print(f"Labels: {created} created, {exists} already existed")
    print()

def main():
    print("=" * 60)
    print("GitHub Issues Import Script for Introspection")
    print("=" * 60)
    print()
    
    # Check prerequisites
    check_gh_cli()
    
    # Get repository
    repo = get_repo()
    print_color(f"Repository: {repo}", GREEN)
    print()
    
    # Create labels first
    create_labels(repo)
    
    # Check if CSV exists
    csv_path = Path(CSV_FILE)
    if not csv_path.exists():
        print_color(f"Error: {CSV_FILE} not found", RED)
        print("Place todo.csv in the same directory as this script")
        sys.exit(1)
    
    # Read CSV
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        issues = list(reader)
    
    total = len(issues)
    print_color(f"Found {total} issues to import", YELLOW)
    print()
    
    # Confirm
    response = input(f"Create {total} issues in {repo}? (y/n): ")
    if response.lower() != 'y':
        print("Aborted.")
        sys.exit(0)
    
    print()
    print("Starting import...")
    print()
    
    # Track results
    created = 0
    failed = 0
    failed_issues = []
    
    # Create issues
    for i, issue_data in enumerate(issues, 1):
        issue_num = issue_data.get('Issue Number', i)
        title = issue_data['Title']
        
        print_color(f"[{i}/{total}] Creating issue #{issue_num}: {title}", YELLOW)
        
        success, message = create_issue(repo, issue_data)
        
        if success:
            created += 1
            print_color(f"✓ Created: {message}", GREEN)
        else:
            failed += 1
            print_color(f"✗ Failed", RED)
            failed_issues.append({
                'number': issue_num,
                'title': title,
                'error': message
            })
            print_color(f"  Error: {message[:100]}", RED)
        
        print()
        
        # Small delay to avoid rate limiting
        time.sleep(0.5)
    
    # Summary
    print("=" * 60)
    print("Import Complete")
    print("=" * 60)
    print_color(f"Created: {created}", GREEN)
    
    if failed > 0:
        print_color(f"Failed: {failed}", RED)
        print()
        print("Failed issues:")
        for issue in failed_issues:
            print(f"  #{issue['number']}: {issue['title']}")
            print(f"    Error: {issue['error'][:100]}")
        
        # Write to log file
        with open('failed_issues.log', 'w') as f:
            for issue in failed_issues:
                f.write(f"Issue #{issue['number']}: {issue['title']}\n")
                f.write(f"Error: {issue['error']}\n\n")
        print()
        print("Details logged to: failed_issues.log")
    
    print()
    print("Next steps:")
    print("1. Review created issues in GitHub")
    print("2. Create a new GitHub Project")
    print("3. Add issues to your project board")

if __name__ == '__main__':
    main()