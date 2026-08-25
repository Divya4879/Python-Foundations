# --- 1. Looping and Indentation Errors ---
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    # LOGICAL ERROR: If the next line isn't indented, it only prints once after the loop finishes.
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# INDENTATION ERROR: Python expects an indented block after a 'for' statement.
# for magician in magicians:
# print(magician) # This will throw an IndentationError

# --- 2. Using range() ---
# range() stops ONE item before the second index (prints 1, 2, 3, 4)
for value in range(1, 5):
    print(value)

# list() converts the range directly into a list in memory.
numbers = list(range(1, 6))
even_numbers = list(range(2, 11, 2)) 

# --- 3. Simple Statistics ---
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lowest, highest, total = min(digits), max(digits), sum(digits)

# --- 4. List Comprehensions ---
# Combines loop and creation into one line.
squares = [value**2 for value in range(1, 11)]

# --- 5. Slicing Lists ---
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_three = players[0:3] 
# Negative slicing safely grabs from the end.
last_three = players[-3:] 

# --- 6. The Memory Reference Trap ---
my_foods = ['pizza', 'falafel', 'carrot cake']

# BAD: Points to the same list in memory.
friend_foods_reference = my_foods 
# GOOD: Creates a new, independent copy using a full slice.
friend_foods_copy = my_foods[:] 

# --- 7. Tuples (Immutable State) ---
# Tuples use parentheses. They are strictly immutable.
dimensions = (200, 50) 
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250 -> This throws a TypeError: 'tuple' object does not support item assignment

# You CAN overwrite the entire tuple by reassigning the variable.
dimensions = (400, 100) 

# A single-element tuple requires a trailing comma to be recognized.
my_t = (3,) 

# You can loop through tuples exactly like lists.
for dimension in dimensions: 
    print(dimension)