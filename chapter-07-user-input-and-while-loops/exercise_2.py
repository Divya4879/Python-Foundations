# Problem 7-4: Pizza Toppings

print("Hello Customer!")

while True:
    prompt = "\nPlease enter any pizza topping you want."
    prompt += "\nPress 'quit' when you're done: "

    pizza_topping = input(prompt)

    if pizza_topping == 'quit':
        break
    print(f"{pizza_topping.title()} topping will be added to your pizza.")

print("\nYour pizza is made!\nCome to the counter & get it, and enjoy:))\n")

# Problem 7-5: Movie Tickets

print("Welcome to DIVYA theatre!\n")

response = True

while response:
    try:
        age = int(input("Please enter your age in number: "))
    except:
        break

    if age < 3:
        price = 0
    elif age <=12:
        price = 10
    elif age >12:
        price = 15
    else:
        response= "You entered nothing, or a wrong value.\nDo you want to quit? (y/n):"

    print(f"Your movie ticket will cost you ${price}.\n")

# Problem 7-6: Three Exits- For problem 7-5

# EXIT 1: CONDITIONAL TEST

print("\nWelcome to DIVYA theatre!\n")

while True:
    age = int(input("Enter your age in numbers.\nPress 0 if you want to quit: "))

    if age == 0:
        break
    else:
        if age < 3:
            price = 0
        elif age <= 12:
            price = 10
        elif age > 12:
            price = 15

    print(f"Your movie ticket will cost you ${price}.\n")

# EXIT 2: ACTIVE VARIABLE-> ALREADY USED IT

# EXIT 3: BREAK STATEMENT FOR USER'S 'quit'

print("\nWelcome to DIVYA theatre!\n")

while True:
    age = input("Enter your age in numbers.\nPress 'quit' if you want to quit: ")

    if age == 'quit':
        break

    age = int(age)

    if age == 0:
        break
    else:
        if age < 3:
            price = 0
        elif age <= 12:
            price = 10
        elif age > 12:
            price = 15

    print(f"Your movie ticket will cost you ${price}.\n")

# Problem 7-7: INFINITY

msg = "I am gonna get a niceyy job soooon!!"

while True:
    print(msg)