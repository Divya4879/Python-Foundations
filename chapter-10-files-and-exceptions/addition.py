# Problem 10-6: Addition

def addition(no_1, no_2):
    try:
        res = int(no_1) + int(no_2)
    except ValueError:
        return "\nPlease enter 2 numbers in numerical form only!!\n"
    else:
        return f"\nSum of {no_1} and {no_2} equals {res}.\n"

while True:
    print("Enter 2 nos and get their sum.")
    print("Enter q anytime you wanna quit.\n")

    no_1 = input("Please enter 1st no: ")
    if no_1 == 'q':
        break

    no_2 = input("Please enter 2nd no: ")
    if no_2 == 'q':
        break

    print(addition(no_1, no_2))