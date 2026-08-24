from pathlib import Path

def word_count(path):
    """Count the approx no of words in a text file."""

    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} doesn't exist in this directory.")
    else:
        # Count the approx no of words in the file
        words = contents.strip()
        word_count = len(words)
        print(f"'{path}' File has about {word_count} words in it.")

file_names = [
    'guest_book.txt',
    'guest.txt',
    'learning_python.txt',
    'word_count.txt',
    'written_message.txt'
    ]

for file_name in file_names:
    path = Path(file_name)
    word_count(path)
