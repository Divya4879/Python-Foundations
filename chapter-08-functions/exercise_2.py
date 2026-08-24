# Problem 8-3: T-Shirt

def make_shirt(size, message):
    print(f"\nYou want a {size.lower()}-sized shirt, with this message printed: '{message}'.")

make_shirt("Small", "You're gonna be happy soon:)") # POSITIONAL ARGUMENTS
make_shirt(message='Python is awesome!',size='medium') # KEYWORD ARGUMENTS

# Problem 8-4: Large Shirts

def make_shirt(size='large', message='I love Python'):
    print(f"\nYou want a {size.lower()}-sized shirt, with this message printed: '{message}'.")

make_shirt()
make_shirt('medium')
make_shirt(message='I really like Python') # POSITIONAL ARGUMENTS WASN'T POSSIBLE HERE

# Problem 8-5: Cities

def describe_city(city, country='India'):
    print(f"\n{city.title()} is in {country.title()}.")

describe_city('Jaipur')
describe_city(country='the united states of america',city='los angeles')
describe_city('Seoul','South Korea')