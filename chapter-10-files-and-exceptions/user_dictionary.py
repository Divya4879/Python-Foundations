# Problem 10-13: User Dictionary

from pathlib import Path
import json

def get_stored_user_details(path):
    content = path.read_text()
    user_details = json.loads(content)
    user_name = user_details['Name']

    response = input(f"Hello! Is it {user_name}?(yes/no): ")
    if response == 'no':
        get_new_user_details(path)
        return

    print("\nUSER DETAILS:\n")
    for detail, val in user_details.items():
        print(f"{detail.title()}: {val.title()}")

def get_new_user_details(path):
    print("\nHELLO NEW USER.")
    print("Please answer a few of our ques to get a customized greeting next time you come here!\n")

    user_details = {}
    user_details['Name'] = input("Please tell us your name: ").title()
    user_details['Field'] = input("Please tell us about your field of work: ").title()
    user_details['Specialization'] = input("Please tell us about your specialization/mastery topic: ").title()

    print(f"\nHey {user_details['Name']}! We'll remember you next time you come back!\n")

    user_dictionary = json.dumps(user_details)
    path.write_text(user_dictionary)

def greet_user():
    path = Path('user_dictionary.json')
    if path.exists():
        get_stored_user_details(path)
    else:
        get_new_user_details(path)

greet_user()