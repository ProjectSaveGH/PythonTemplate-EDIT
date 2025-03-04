import re

def contains_python(expression):
    """Überprüft, ob der Ausdruck gefährliche Python-Schlüsselwörter enthält."""
    python_keywords = {
        "import", "exec", "eval", "open", "os", "sys", "subprocess", "globals", "locals", "compile",
        "__import__", "lambda", "exit", "quit", "help", "breakpoint", "getattr", "setattr", "delattr",
        "def", "class", "return", "yield", "try", "except", "finally", "raise", "assert", "with",
        "async", "await", "for", "while", "if", "elif", "else", "break", "continue", "pass"
    }
    tokens = re.split(r'\W+', expression)
    return any(token in python_keywords for token in tokens)

def contains_sql(expression):
    """Überprüft, ob der Ausdruck gefährliche SQL-Schlüsselwörter enthält."""
    sql_keywords = {
        "select", "insert", "update", "delete", "drop", "alter", "create", "truncate", "union",
        "where", "from", "table", "database", "grant", "revoke", "execute", "declare", "fetch",
        "cursor", "begin", "commit", "rollback", "procedure"
    }
    tokens = re.split(r'\W+', expression)
    return any(token in sql_keywords for token in tokens)