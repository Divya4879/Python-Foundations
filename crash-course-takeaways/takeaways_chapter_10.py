"""
Chapter 10: Files and Exceptions
It covers paths (including subfolders), reading/writing,
the "simpler code" looping trick, converting numbers, 
failing silently (with log placeholders), and JSON persistence.
"""

import json
from pathlib import Path

# =========================================================
# 1. PATHS & READING FILES (Including Subfolders)
# =========================================================
print("--- 1. Paths & File Reading ---")

# RELATIVE PATH (Subfolder): Looks inside a folder named 'text_files' in the current directory.
# path = Path('text_files/pi_digits.txt')
path = Path('pi_digits.txt') 

if path.exists():
    contents = path.read_text().rstrip()
    
    # Building a single string from the file contents
    pi_string = ''
    
    # THE "SIMPLER CODE" TRICK: 
    # You can skip creating a temporary 'lines' variable and loop directly over splitlines()
    for line in contents.splitlines():
        pi_string += line.lstrip()
        
    print(f"First 52 digits: {pi_string[:52]}...")
    print(f"Total length: {len(pi_string)}")
    
    birthday = input("Enter your birthday (mmddyy): ")
    if birthday in pi_string:
        print("Your birthday appears in the digits of pi!")
    else:
        print("Your birthday does not appear.")
else:
    print(f"File {path} not found.")


# =========================================================
# 2. WRITING TEXT FILES & NUMERICAL CONVERSION
# =========================================================
print("\n--- 2. File Writing ---")

write_path = Path('programming.txt')

# Building a multi-line string.
new_contents = "I love programming.\n"
new_contents += "I love creating new games.\n"
new_contents += "I also love working with data.\n"

# write_text() completely ERASES existing data and overwrites it.
write_path.write_text(new_contents)
print(f"Successfully wrote text data to {write_path.name}")

# NUMERICAL DATA CONVERSION:
# Python can ONLY write strings to a text file. 
number_path = Path('favorite_number.txt')
favorite_number = 42
# You MUST convert the integer to a string using str() before writing.
number_path.write_text(str(favorite_number))
print(f"Successfully wrote numerical data to {number_path.name}")


# =========================================================
# 3. EXCEPTIONS & FAILING SILENTLY
# =========================================================
print("\n--- 3. Exceptions & Tracebacks ---")

try:
    answer = 5 / 0
except ZeroDivisionError:
    print("Error: You can't divide by zero!")
else:
    print(answer)


def count_words(file_path):
    """Count the approximate number of words in a file."""
    try:
        text = file_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # FAILING SILENTLY: 'pass' acts as a placeholder. 
        # For example, we might later decide to write any missing filenames 
        # to a file called 'missing_files.txt' right here instead of doing nothing.
        pass
    else:
        words = text.split()
        # Note: Using {file_path} directly prints the exact path string as requested.
        print(f"The file {file_path} has about {len(words)} words.")

# Loop through multiple files, including all examples from the text.
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(Path(filename))


# =========================================================
# 4. JSON DATA PERSISTENCE & REFACTORING
# =========================================================
print("\n--- 4. JSON & Refactoring ---")

# 4a. Basic JSON usage
numbers_path = Path('numbers.json')
numbers = [2, 3, 5, 7, 11, 13]
# json.dumps() converts the Python list into a JSON string.
numbers_path.write_text(json.dumps(numbers))
# json.loads() converts the JSON string back into a Python object.
read_numbers = json.loads(numbers_path.read_text())
print(f"Read numbers from JSON: {read_numbers}")


# 4b. Refactored User Greeting Program
def get_stored_username(user_path):
    """Get stored username if available."""
    if user_path.exists():
        return json.loads(user_path.read_text())
    return None

def get_new_username(user_path):
    """Prompt for a new username and save it."""
    username = input("What is your name? ")
    user_path.write_text(json.dumps(username))
    return username

def greet_user():
    """Greet the user by name. Each function has a single, clear purpose."""
    user_path = Path('username.json')
    username = get_stored_username(user_path)
    
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(user_path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()