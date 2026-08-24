# Problem 8-1: Message

def display_message():
    user_name = input("Please enter your name here: ")
    print(f"\nHello {user_name.title()}, so far I've learned about functions, calling them, passing arguments & parameters, and more in this chapter.")

display_message()

# Problem 8-2: Favorite Book

def favorite_book(book):
    print(f"\nOne of my favourite books is {book.title()}.")

favorite_book('Atomic Habits')