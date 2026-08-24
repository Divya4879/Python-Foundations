# Problem 7-1: Rental Car

name = input("Please enter your first name here: ")
rental_car = input(f"Hello {name.title()}! Which kind of rental car are you looking for? \n")

print(f"\nGot it {name.title()}! Lemme check if I can find you a {rental_car.title()}.")

# Problem 7-2: Restaurant Seating

customer_count = int(input("\nPlease enter the number of people in your dinner group (1,2,3,..): "))

if customer_count <= 8:
    print(f"\nYour table for {customer_count} people is reserved for you.")
else:
    print("\nPlease wait for sometime.\nWe're finding a table for your group.")

# Problem 7-3: Multiples of 10

user_choice = int(input("\nPlease enter a whole number: "))

if user_choice % 10 == 0:
    print(f"{user_choice} is a multiple of 10.")
else:
    print(f"{user_choice} is not a multiple of 10.")