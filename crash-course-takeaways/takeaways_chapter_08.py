"""
Chapter 8: Functions, Scope, and Data Flow
This file contains the core concepts, code snippets, and PEP 8 styling rules 
for working with functions in Python.
"""

# PEP 8 Rule: All import statements should be written at the beginning of a file.
# import pizza 

# ---------------------------------------------------------
# 1. BASICS, DOCSTRINGS, AND KEYWORD ARGUMENTS
# ---------------------------------------------------------
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


# Positional vs Keyword Arguments
# PEP 8 Rule: No spaces around the equal sign when used for keyword arguments.
greet_user('jesse') 
greet_user(username='jesse') 


# ---------------------------------------------------------
# 2. DEFAULT VALUES & OPTIONAL ARGUMENTS
# ---------------------------------------------------------
# PEP 8 Rule: Default parameters must come AFTER non-default parameters.
# PEP 8 Rule: No spaces around the equal sign for default values.
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='willie')


# Using an empty string to make an argument optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    # Python interprets non-empty strings as True
    if middle_name: 
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


# ---------------------------------------------------------
# 3. FUNCTIONS WITH WHILE LOOPS
# ---------------------------------------------------------
def run_greeting_loop():
    """Run an interactive prompt to format names."""
    while True:
        print("\nPlease tell me your name:")
        print("(enter 'q' at any time to quit)")
        
        f_name = input("First name: ")
        if f_name == 'q':
            break
            
        l_name = input("Last name: ")
        if l_name == 'q':
            break
            
        formatted_name = get_formatted_name(f_name, l_name)
        print(f"\nHello, {formatted_name}!")


# ---------------------------------------------------------
# 4. MODIFYING LISTS & THE "ONE JOB" RULE
# ---------------------------------------------------------
# PEP 8 Rule: Separate functions by two blank lines to make them easier to see.


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted = ['phone case', 'robot pendant', 'dodecahedron']
completed = []

# Modifying the original list:
# print_models(unprinted, completed)

# Passing a SLICE [:] sends a copy to prevent modifying the original list:
print_models(unprinted[:], completed) 
show_completed_models(completed)


# ---------------------------------------------------------
# 5. ARBITRARY POSITIONAL ARGUMENTS (*args)
# ---------------------------------------------------------
# Python packs arbitrary positional arguments into a TUPLE.
# The arbitrary parameter must be placed last in the function definition.
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# ---------------------------------------------------------
# 6. ARBITRARY KEYWORD ARGUMENTS (**kwargs)
# ---------------------------------------------------------
# Python packs arbitrary keyword arguments into a DICTIONARY.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    # Add standard pieces of information directly to the dictionary
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)