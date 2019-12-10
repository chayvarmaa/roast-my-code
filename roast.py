import ast
import sys
from colorama import init, Fore
from rules import (
    check_bad_variable_names,
    check_missing_docstrings,
    check_deep_nesting,
    check_long_functions,
    check_todo_comments,
    check_bare_except
)

init(autoreset=True)


def print_banner():
    print(Fore.RED + """
 ____                   _   __  __         ____          _      
|  _ \ ___   __ _ ___  | |_|  \/  |_   _ / ___|___   __| | ___ 
| |_) / _ \ / _` / __| | __| |\/| | | | | |   / _ \ / _` |/ _ |
|  _ < (_) | (_| \__ \ | |_| |  | | |_| | |__| (_) | (_| |  __/
|_| \_\___/ \__,_|___/  \__|_|  |_|\__, |\____\___/ \__,_|\___|
                                    |___/                        
    """)
    print("  A sarcastic senior dev is reviewing your code...\n")


def print_section(title):
    print(Fore.CYAN + "\n" + "=" * 55)
    print(Fore.CYAN + "  " + title)
    print(Fore.CYAN + "=" * 55)


def roast_file(filepath):
    try:
        with open(filepath, "r") as f:
            source_code = f.read()
    except FileNotFoundError:
        print(Fore.RED + "File not found: " + filepath)
        sys.exit(1)

    try:
        tree = ast.parse(source_code)
    except SyntaxError as e:
        print(Fore.RED + "Your code has a syntax error, fix that first: " + str(e))
        sys.exit(1)

    print_banner()
    print("  Roasting file: " + filepath + "\n")

    total_issues = 0

    # check variable names
    print_section("Variable Names")
    bad_vars = check_bad_variable_names(tree)
    if bad_vars:
        for line, name, reason in bad_vars:
            print(Fore.RED + "  Line " + str(line) + ": '" + name + "' - " + reason + ". Use a real name.")
            total_issues += 1
    else:
        print(Fore.GREEN + "  Variable names look decent. Shocked, honestly.")

    # check docstrings
    print_section("Docstrings")
    missing_docs = check_missing_docstrings(tree)
    if missing_docs:
        for line, name in missing_docs:
            print(Fore.RED + "  Line " + str(line) + ": '" + name + "' has no docstring. How will anyone know what this does.")
            total_issues += 1
    else:
        print(Fore.GREEN + "  All functions documented. Rare sight.")

    # check nesting
    print_section("Nesting Depth")
    deep = check_deep_nesting(tree)
    if deep:
        for line, depth in deep:
            print(Fore.RED + "  Line " + str(line) + ": " + str(depth) + " levels of nesting. This is code, not inception.")
            total_issues += 1
    else:
        print(Fore.GREEN + "  No deep nesting found.")

    # check function length
    print_section("Function Length")
    long_funcs = check_long_functions(tree)
    if long_funcs:
        for line, name, length in long_funcs:
            print(Fore.RED + "  Line " + str(line) + ": '" + name + "' is " + str(length) + " lines long. A function should do one thing.")
            total_issues += 1
    else:
        print(Fore.GREEN + "  Functions are a reasonable length.")

    # check todos
    print_section("TODO and FIXME Comments")
    todos = check_todo_comments(source_code)
    if todos:
        for line, content in todos:
            print(Fore.YELLOW + "  Line " + str(line) + ": " + content + " -- the 'I'll fix it later' graveyard.")
            total_issues += 1
    else:
        print(Fore.GREEN + "  No TODO comments found.")

    # check bare excepts
    print_section("Bare Except Clauses")
    bare = check_bare_except(tree)
    if bare:
        for line in bare:
            print(Fore.RED + "  Line " + str(line) + ": bare 'except' found. Catching all exceptions silently is how bugs hide forever.")
            total_issues += 1
    else:
        print(Fore.GREEN + "  No bare excepts found.")

    # final score
    print(Fore.CYAN + "\n" + "=" * 55)
    print(Fore.CYAN + "  FINAL VERDICT")
    print(Fore.CYAN + "=" * 55)

    if total_issues == 0:
        print(Fore.GREEN + "\n  Zero issues found. Either your code is great or my checker is broken.\n")
    elif total_issues <= 3:
        print(Fore.YELLOW + "\n  " + str(total_issues) + " issue(s) found. Room to improve but I've seen worse.\n")
    elif total_issues <= 7:
        print(Fore.RED + "\n  " + str(total_issues) + " issues. This code needs a rewrite, not a review.\n")
    else:
        print(Fore.RED + "\n  " + str(total_issues) + " issues. Please close your laptop and think about your choices.\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 roast.py <your_python_file.py>")
        sys.exit(1)

    roast_file(sys.argv[1])