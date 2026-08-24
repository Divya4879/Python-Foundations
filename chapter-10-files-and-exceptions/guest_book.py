# Problem 10-5: Guest Book

from pathlib import Path

path = Path('guest_book.txt')
user_names = []

while True:
    user_name = input("Please enter your name: ")
    if user_name.isalpha():
        user_names.append(user_name)
        more_names = input('Do you have more guests with you? (yes/no): ')
        if more_names == 'no':
            break
    else:
        print("Please enter your name correctly.")

guest_book = 'OUR GUESTS:\n\n'
for guest in user_names:
    guest_book += f"{guest.title()}\n"

path.write_text(guest_book)