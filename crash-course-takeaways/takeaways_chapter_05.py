# --- 1. Basic Equality and Case-Insensitive Validation ---
car = 'bmw'
print(car == 'bmw') # Returns True

# Equality checks in Python are strictly case-sensitive.
car_two = 'Audi'
print(car_two == 'audi') # Returns False
# Best practice for database checks (like unique usernames): normalize to lowercase first.
print(car_two.lower() == 'audi') # Returns True

# --- 2. The 'in' and 'not in' Operators ---
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings) # Returns True
print('pepperoni' in requested_toppings) # Returns False

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# --- 3. Boolean State Tracking ---
# Booleans are the most efficient way to track program state.
game_active = True
can_edit = False

# --- 4. Architectural Efficiency in Chains ---
# BAD: Repeating the action (e.g., print) inside every block.
# GOOD: Set the state/variable inside the block, and act on it ONCE outside.
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
    
# Only one print call needs to be maintained or modified.
print(f"Your admission cost is ${price}.")

# --- 5. The 'else' Catchall Trap ---
# 'else' will catch ANYTHING that didn't match, including malicious or invalid data.
# It is often safer to use a final 'elif' to strictly define the final accepted condition.
age = 70
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65: # Stricter and safer than 'else'
    price = 20

# --- 6. Independent 'if's vs. 'elif' Chains ---
# If multiple blocks of code need to run, you MUST use independent 'if' statements.
# An 'if-elif-else' chain stops evaluating the exact moment one test passes.
toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in toppings:
    print("Adding mushrooms.")
if 'extra cheese' in toppings:
    print("Adding extra cheese.")

# --- 7. Combining Loops and Conditionals ---
# Checking for special conditions inside a loop.
# Note: If this list of available toppings was stable, it should be stored as a Tuple.
order_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for topping in order_toppings:
    if topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {topping}.")
print("\nFinished making your pizza!")

# --- 8. PEP 8 Styling for Conditionals ---
# Always use a single space around comparison operators for readability.
# YES: if age < 4:
# NO:  if age<4: