# --- 1. User Input and Formatting ---
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)

# --- 2. The Modulo Operator ---
# Modulo (%) tells you the remainder, NOT how many times a number fits.

# --- 3. The Basic While Loop and Logical Fixes ---
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# --- 4. Architectural State Management (Flags) ---
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# --- 5. Directing Control Flow with 'break' ---
while True:
    city = input("Please enter a city you have visited (or 'quit'): ")
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# --- 6. Directing Control Flow with 'continue' ---
# Rather than breaking out entirely, 'continue' returns to the beginning of the loop.
current_number = 0
while current_number < 10:
    current_number += 1
    # If the number is even, skip the rest of the loop and start over.
    if current_number % 2 == 0:
        continue
    print(current_number)

# --- 7. Modifying Lists in a Loop ---
# NEVER modify a list inside a 'for' loop. Use a 'while' loop instead.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# --- 8. Removing ALL Instances of a Value ---
# .remove() only deletes the first instance. A while loop deletes them all.
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# --- 9. Infinite Loops ---
# If a program gets stuck in an infinite loop, press CTRL-C in the terminal to kill it.