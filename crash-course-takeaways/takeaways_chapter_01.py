# 1. The standard execution check
print("Environment is set up and running.")

# 2. Understanding Tracebacks
# A traceback is an error report showing exactly where the interpreter ran into trouble.
# Below is a function designed to intentionally crash to demonstrate a traceback.

def trigger_traceback():
    # This will raise a NameError because the variable does not exist.
    print(uninitialized_variable)

trigger_traceback()

"""
--- Terminal Cheat Sheet ---
Execution:
    python learning_chapter_01.py

Exiting the Python Interactive Shell (REPL):
    Windows: Ctrl + Z (or type exit())
    Linux/Mac: Ctrl + D (or type exit())
"""
