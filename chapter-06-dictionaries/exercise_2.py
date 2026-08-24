# Problem 6-5: Rivers

rivers = {
    'nile' : 'egypt',
    'ganga' : 'india',
    'thames' : 'london'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print()

print("The rivers are:-")
for river in rivers:
    print(river.title())
print()

print("The countries are:")
for country in rivers.values():
    print(country.title())
print()

# Problem 6-6: Favorite Languages

favorite_languages = {
    'Divya' : 'Python',
    'Rajrani' : 'C#',
    'Divyam' : 'JS',
    'Harry' : 'Java'
}

persons = ['Divya', 'Divyam', 'Ria', 'Raj', 'Anjali']

for person in persons:
    if person in favorite_languages:
        print(f"{person}, thank you so much for taking the poll.\n")
    else:
        print(f"Hello {person}, please take the poll.\n")
print()