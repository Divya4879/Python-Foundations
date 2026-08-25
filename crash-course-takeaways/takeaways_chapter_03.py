# --- 1. Dynamic Lists and Memory ---
# Lists are dynamic and can hold heterogeneous data. 
# Best practice: Name list variables as plurals (e.g., 'active_users').
motorcycles = ['honda', 'yamaha', 'suzuki']

# Appending adds to the end (O(1) time complexity).
motorcycles.append('ducati')

# Inserting shifts every other element to the right in memory (O(n) time complexity).
motorcycles.insert(0, 'ducati')

# --- 2. The Deletion Dilemma: del vs pop vs remove ---
# Use 'del' when you know the index and DO NOT need the value anymore.
del motorcycles[0]

# Use 'pop()' when you want to use the item after removing it (think of it like a stack).
# It defaults to the last item [-1], but accepts an index.
last_bike = motorcycles.pop()
first_bike = motorcycles.pop(0)

# Use 'remove()' when you only know the value, not the index.
# Warning: It ONLY removes the first occurrence. You need a loop to remove duplicates.
motorcycles = ['honda', 'yamaha', 'honda']
motorcycles.remove('honda') 

# --- 3. Sorting: Mutation vs. Return ---
cars = ['bmw', 'audi', 'toyota', 'subaru']

# sorted() returns a NEW list and leaves the original intact in memory.
safe_sorted_cars = sorted(cars)

# sort() mutates the original list PERMANENTLY.
cars.sort(reverse=True)

# reverse() simply flips the current order permanently, without alphabetical sorting.
cars.reverse()

# --- 4. The Off-By-One Error ---
# Python is 0-indexed. Accessing the 3rd item requires index 2.

# Accessing [-1] always gets the last item, UNLESS the list is empty,
# which throws an IndexError.
empty_list = []
# print(empty_list[-1])  # Uncommenting this throws a Traceback (IndexError).