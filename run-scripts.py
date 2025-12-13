#!/usr/bin/env python3
"""
Python Practice Questions - Interactive Runner
Choose and run any Python script from the repository
"""

import os
import sys
import subprocess
from pathlib import Path

def find_python_files(base_dir="."):
    """Find all Python files in the repository"""
    python_files = []
    exclude_dirs = {'.git', '.venv', 'venv', '__pycache__', 'node_modules', '.pytest_cache'}
    
    for root, dirs, files in os.walk(base_dir):
        # Remove excluded directories from search
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if file.endswith('.py') and not file.startswith('_'):
                rel_path = os.path.relpath(os.path.join(root, file), base_dir)
                python_files.append(rel_path)
    
    return sorted(python_files)

def categorize_files(files):
    """Organize files by directory"""
    categories = {}
    for file in files:
        parts = Path(file).parts
        if len(parts) > 1:
            category = parts[0]
            if category not in categories:
                categories[category] = []
            categories[category].append(file)
        else:
            if 'root' not in categories:
                categories['root'] = []
            categories['root'].append(file)
    
    return categories

def display_menu(categories):
    """Display interactive menu"""
    print("\n" + "="*70)
    print("🐍 Python Practice Questions - Interactive Runner")
    print("="*70)
    
    all_files = []
    idx = 1
    
    for category in sorted(categories.keys()):
        if category == 'practice-questions':
            continue  # Skip practice questions folder for now
        
        files = categories[category]
        print(f"\n📁 {category.upper()}")
        print("-" * 70)
        
        for file in files:
            print(f"  [{idx:3d}] {file}")
            all_files.append(file)
            idx += 1
    
    print("\n" + "="*70)
    print(f"Total scripts available: {len(all_files)}")
    print("="*70)
    
    return all_files

def run_script(filepath):
    """Run the selected Python script"""
    print("\n" + "="*70)
    print(f"▶️  Running: {filepath}")
    print("="*70 + "\n")
    
    try:
        # Run the script
        result = subprocess.run(
            [sys.executable, filepath],
            cwd=os.path.dirname(filepath) if os.path.dirname(filepath) else '.',
            check=False
        )
        
        print("\n" + "="*70)
        if result.returncode == 0:
            print("✅ Script completed successfully")
        else:
            print(f"❌ Script exited with code: {result.returncode}")
        print("="*70)
        
        return result.returncode
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Script interrupted by user")
        return 130
    except Exception as e:
        print(f"\n❌ Error running script: {e}")
        return 1

def main():
    """Main function"""
    print("\n🔍 Scanning for Python scripts...")
    
    # Find all Python files
    python_files = find_python_files()
    
    if not python_files:
        print("❌ No Python files found in the repository")
        return 1
    
    # Categorize by directory
    categories = categorize_files(python_files)
    
    # Display menu
    all_files = display_menu(categories)
    
    while True:
        try:
            print("\nOptions:")
            print("  • Enter number (1-{}) to run a script".format(len(all_files)))
            print("  • Enter 'q' to quit")
            print("  • Enter 'r' to refresh/rescan files")
            
            choice = input("\n👉 Your choice: ").strip()
            
            if choice.lower() == 'q':
                print("\n👋 Goodbye!")
                break
            
            if choice.lower() == 'r':
                main()
                break
            
            try:
                idx = int(choice)
                if 1 <= idx <= len(all_files):
                    selected_file = all_files[idx - 1]
                    run_script(selected_file)
                    
                    # Ask if user wants to continue
                    print("\n" + "="*70)
                    cont = input("Run another script? (y/n): ").strip().lower()
                    if cont != 'y':
                        print("\n👋 Goodbye!")
                        break
                    
                    # Redisplay menu
                    all_files = display_menu(categories)
                else:
                    print(f"❌ Invalid choice. Please enter 1-{len(all_files)}")
            
            except ValueError:
                print("❌ Invalid input. Please enter a number or 'q' to quit")
        
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted by user. Goodbye!")
            break
        except EOFError:
            print("\n\n👋 Goodbye!")
            break
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
