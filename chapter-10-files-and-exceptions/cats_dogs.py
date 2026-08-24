# Problem 10-8: Cats and Dogs

from pathlib import Path

path_cats = Path('cats.txt')
path_dogs = Path('dogs.txt')

try:
    cats = path_cats.read_text()
except FileNotFoundError:
    print("\ncats.txt file not in current directory.\n")
else:
    print("\nCATS:")
    for cat in cats.split('\n'):
        print(cat.title())
    print()

try:
    dogs = path_dogs.read_text()
except FileNotFoundError:
    print("\ndogs.txt file not in current directory.\n")
else:
    print("DOGS:")
    for dog in dogs.split('\n'):
        print(dog.title())
    print()

# Problem 10-9: Silent Cats and Dogs

from pathlib import Path

path_cats = Path('cats.txt')
path_dogs = Path('dogs.txt')

try:
    cats = path_cats.read_text()
except FileNotFoundError:
    pass
else:
    print("\nCATS:")
    for cat in cats.split('\n'):
        print(cat.title())
    print()

try:
    dogs = path_dogs.read_text()
except FileNotFoundError:
    pass
else:
    print("DOGS:")
    for dog in dogs.split('\n'):
        print(dog.title())
    print()

# Problem 10-10: Common Words

words = ['the', 'their', 'them', 'then']
print(words.count('the '))  # 0
print(words.count('the'))   # 1

# As for the problem, I can simply create a list using split()
# so that each word can be counted correctly, not approximately. 

line = 'They installed the solar panel, then they used them in their homes.'
print(line.lower().count('the'))  # 6
print(line.lower().count('the ')) # 1
print(line.count('the '))         # 1

line = line.lower().split()
print(line.count('the'))  # 1
print(line.count('the ')) # 0
print(line.count('the ')) # 0