# Problem 6-7: People

divya = {
    'first_name': 'Divya',
    'last_name': 'Singh',
    'Nationality': 'Indian',
    'Fav_language': 'Python',
    'Specialization': 'Python Backend'
    }

ria = {
    'first_name': 'Ria',
    'last_name': 'Sen',
    'Nationality': 'Indian',
    'Fav_language': 'C++',
    'Specialization': 'C#'
    }

issabella = {
    'first_name': 'Issabella',
    'last_name': 'Malfoy',
    'Nationality': 'British',
    'Fav_language': 'Parseltongue',
    'Specialization': 'Potions'
    }

# Nesting dictioanries in lists

people = [divya, ria, issabella]

print("Lemme give you a little info about 3 of the people I know.")

for person in people:
    name = f"{person['first_name']} {person['last_name']}"
    print(f"\nI know {person['first_name'].title()}.\nDetails I know:-")
    print(f"\t{name}")
    print(f"\tNationality: {person['Nationality']}")
    print(f"\tFavourite Language: {person['Fav_language']}")
    print(f"\tSpecialization: {person['Specialization']}")

# Problem 6-8: Pets

sunshine = {
    'Name' : "Sunshine",
    'Animal' : "Dog",
    'Breed' : 'Golden Retriever',
    'Owner' : 'Luna Lovegood'
    }

hedwig = {
    'Name' : "Hedwig",
    'Animal' : "Owl",
    'Breed' : 'Pure-white regal owl',
    'Owner' : 'Harry Potter'
    }

nagini = {
    'Name' : "Nagini",
    'Animal' : "Snake",
    'Breed' : 'Magical Venomenous Huge',
    'Owner' : 'Voldemort'
    }

pets = [sunshine, hedwig, nagini]

i=1
for pet in pets:
    print(f"\nPET {i} DETAILS:-")
    print(f"\tName: {pet['Name']}")
    print(f"\tAnimal: {pet['Animal']}")
    print(f"\tBreed: {pet['Breed']}")
    print(f"\tOwner: {pet['Owner']}")
    i+=1

# Problem 6-9: Favorite Places

favorite_places = {
    'Divya' : ['Los Angeles', 'San Francisco', 'London'],
    'Issabella' : ['Swizerland', 'Paris'],
    'Ria' : ['Korea'],
    'Rishika' : ['Japan', 'Korea', 'China']
}

for person,places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{person.title()} wants to visit {places[0]}.")
    else:
        print(f"\n{person.title()} wants to visit:-")
        for place in places:
            print(f"\t\t{place}")

# Problem 6-10: Favorite Numbers

favorite_nos = {
    'Divya' : [4,8,5],
    'Ria' : [9,25],
    'Raj' : [7],
    'Wednesday' : [13]
}

for person,nos in favorite_nos.items():
    if len(nos) == 1:
        print(f"\n{person.title()}'s favourite number is {nos[0]}.")
    else:
        print(f"\n{person.title()}'s favorite numbers are:-",end=' ')
        for no in nos:
            print(f"{no}",end=' ')
        print()

# Problem 6-11: Cities

cities = {}

cities['Jaipur'] = {
    'country': 'India',
    'population': 30_000,
    'fact': 'Pink City'
    }

cities['Patna'] = {
    'country': 'India',
    'population': 60_000,
    'fact': 'Capital of Bihar'
    }

cities['New Delhi'] = {
    'country': 'India',
    'population': 70_000,
    'fact': "Political hub and India's capital"
    }

for city, facts in cities.items():
    print(f"\n{city.upper()}:")
    for fact,info in facts.items():
        print(f"\t{fact.title()}: {info}")