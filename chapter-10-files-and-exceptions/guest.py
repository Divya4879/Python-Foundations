# Problem 10-4: Guest

from pathlib import Path

path = Path('guest.txt')

user_name = input("Please enter your name here: ")
path.write_text(user_name)
print(f"\n{user_name}, your name has been added to our Guest List.")