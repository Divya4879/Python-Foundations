# Problem 6-1: Person

person_dict = {
    'first name' : 'Divya',
    'last name' : 'Singh',
    'country' : 'India',
    'age' : 24,
    'job' : 'SDE1/ Python Backend Dev'
    }

for key,val in person_dict.items():
    print(f"{key.title()}: {val}")
print()

# Problem 6-2: Favorite Numbers

fav_nos = {
    'Divya' : 4,
    'Ria' : 8,
    'Raj' : 7,
    'Happy' : 5,
    'Wednesday' : 13
}

for key,val in fav_nos.items():
    print(f"{key}'s favourite no is {val}.")
print()

# Problem 6-3: Glossary

glossary = {
    'List' : "Mutable Data Structure which can store different objects.",
    'Tuple' : "An immutable list",
    'Dictionary' : 'A key-value pair of a unique key, and the value can be any Python object',
    'Interpreter' : "Used to read the language, line by line, compile it, interpret it, and run it."
}

glossary['Set'] = 'A unique collection of items, not ordered.'
glossary['Traceback'] = 'An error message in Python, tracing back to the source of error/filename.'

for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning.capitalize()}\n")
