# Simple Usage

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide any number by 0!\n")

# Section: Using Exceptions to Prevent Crashes

while True:
    print("Please enter 2 numbers here.")
    print("Enter q whenever you wanna quit.\n")

    first_number = input("Enter the first number: ")
    if first_number == 'q':
        break
    
    second_number = input("Enter the second no: ")
    if second_number == 'q':
        break
    try:
        res = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't have 0 as a denominator!\n")
        continue

    print(f"\n{first_number}/{second_number} = {res}\n\n")