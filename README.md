# RoastMyCode

A command line tool that analyzes Python files and gives harsh but educational feedback on code quality.

I built this after my professor kept telling me my variable names were bad. 
Wanted to automate the criticism.

## What it checks

- Variable names that are too short or meaningless (x, temp, foo, data)
- Functions and classes missing docstrings
- Code nested more than 3 levels deep
- Functions that are too long (over 30 lines)
- TODO and FIXME comments left in code
- Bare except clauses that silently swallow errors

## Requirements

- Python 3.x
- colorama

## Setup
```bash
git clone https://github.com/yourusername/roast-my-code
cd roast-my-code
python3 -m venv venv
source venv/bin/activate
pip install colorama
```

## Usage
```bash
python3 roast.py yourfile.py
```

## Example
```bash
python3 roast.py sample_bad.py
```

This will analyze the included sample file which has intentional issues for testing.

## What I learned

- How Python's AST (Abstract Syntax Tree) module works
- How linters like pylint analyze code without running it
- How to build a CLI tool that accepts arguments using sys.argv
- Virtual environments and dependency management