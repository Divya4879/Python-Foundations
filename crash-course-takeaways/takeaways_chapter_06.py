# --- 1. Dictionary Basics & Initialization ---
# You can start with an empty dictionary and add key-value pairs dynamically.
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# --- 2. Safe Retrieval ---
# Using square brackets for a non-existent key causes a KeyError.
# The get() method sets a default value that will be returned instead.
# If you omit the second argument, it returns 'None'.
speed = alien_0.get('speed', 'No speed assigned')

# --- 3. Deleting Data ---
# The del statement completely and permanently removes a key-value pair.
del alien_0['points']

# --- 4. Looping and Sorting ---
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# Looping through keys is the default behavior.
# This code...
# for name in favorite_languages:
# Is exactly the same as this:
for name in favorite_languages.keys():
    pass

# The keys() method returns a sequence, allowing for membership checks.
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Wrap sorted() around the keys to retrieve them in alphabetical order.
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# --- 5. Values and Sets ---
# The values() method pulls all values. set() extracts only unique items.
for language in set(favorite_languages.values()):
    print(language.title())

# Sets look like dicts (braces) but have no key-value pairs. They do not retain order.
unique_languages = {'python', 'rust', 'python', 'c'}

# --- 6. Nesting: Lists inside Dictionaries ---
# Good practice: format long dictionaries with a trailing comma.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
# Looping through the list nested inside the dictionary:
for topping in pizza['toppings']:
    print(f"\t{topping}")

# --- 7. Nesting: Dictionaries inside Lists (and Modifying Data) ---
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Modify the first 3 aliens using a slice.
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# --- 8. Nesting: Dictionaries inside Dictionaries ---
# Having an identical structure in nested dictionaries makes looping much easier.
users = {
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
}