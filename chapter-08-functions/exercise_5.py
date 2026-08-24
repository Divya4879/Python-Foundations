# Problem 8-12: Sandwiches

def sandwiches(*ingredients):
    """Printing list of ingredients in your sandwich.
    Using *args in argument.
    """
    print("Summary of ingredients in your sandwich:")
    for ingredient in ingredients:
        print(f'\t\t\t\t{ingredient}')

sandwiches('Tomato','Cucumber')
sandwiches('Paneer', 'Onion', 'Potato cakes', 'Cucumber', 'Tomato')
sandwiches('Tomato')
sandwiches() # No error-> We can use *args for 0 args as well!
print()

# Problem 8-13: User Profile

def build_profile(first_name, last_name, **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info

def show_profile(first_name, last_name, **user_info):
    print("#### USER PROFILE ####\n")
    user_info = build_profile(first_name, last_name, **user_info)
    for param,info in user_info.items():
        print(f"{param.title()}: {info.title()}")

user_info = show_profile('Divya', 'Singh', field='Tech', profession='Backend Developer', lang='Python')

# Problem 8-14: Cars

def make_car(model, manufacturer, **car_info):
    car_info['model_name']= model
    car_info['manufacturer']= manufacturer
    return car_info

print("\n#### Car Details ####\n")
car_info = make_car('Tesla', 'elon musk', color='pink', self_driving='true')

for attribute,info in car_info.items():
    print(f"{attribute.title()}: {info.title()}")

print(f"\n{car_info}\n")