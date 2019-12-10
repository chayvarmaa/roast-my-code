import ast
import re

def check_bad_variable_names(tree):
    bad_names = []
    meaningless = {"temp", "tmp", "data", "val", "var", "foo", "bar", "baz", "x1", "x2"}
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    name = target.id
                    if len(name) == 1 and name != "_":
                        bad_names.append((node.lineno, name, "single letter variable"))
                    elif name.lower() in meaningless:
                        bad_names.append((node.lineno, name, "meaningless name"))
    return bad_names


def check_missing_docstrings(tree):
    missing = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            if not (node.body and isinstance(node.body[0], ast.Expr) and
                    isinstance(node.body[0].value, ast.Constant)):
                missing.append((node.lineno, node.name))
    return missing


def check_deep_nesting(tree):
    issues = []

    def get_depth(node, current_depth=0):
        if isinstance(node, (ast.For, ast.While, ast.If, ast.With)):
            current_depth += 1
            if current_depth >= 3:
                issues.append((getattr(node, 'lineno', 0), current_depth))
        for child in ast.iter_child_nodes(node):
            get_depth(child, current_depth)

    get_depth(tree)
    return issues


def check_long_functions(tree):
    long_funcs = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            length = node.end_lineno - node.lineno
            if length > 30:
                long_funcs.append((node.lineno, node.name, length))
    return long_funcs


def check_todo_comments(source_code):
    todos = []
    for i, line in enumerate(source_code.splitlines(), 1):
        if re.search(r"#\s*(TODO|FIXME|HACK|XXX)", line, re.IGNORECASE):
            todos.append((i, line.strip()))
    return todos


def check_bare_except(tree):
    issues = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ExceptHandler):
            if node.type is None:
                issues.append(node.lineno)
    return issues