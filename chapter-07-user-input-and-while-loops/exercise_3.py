# Problem 7-8: Deli

sandwich_orders = [
    'plain sandwich',
    'extra paneer',
    'cucumber tomatoes capsicum sandwich',
    'omelette sandwich'
    ]

finished_sandwiches = []

while sandwich_orders:
    print(f"I made your {sandwich_orders[0].title()}.\n")
    finished_sandwiches.append(sandwich_orders.pop(0))

print("\nToday we made all these sandwiches:-",end="\n\t")
print(f"{'\n\t'.join(finished_sandwiches).title()}")

# Problem 7-9: No Pastrami

sandwich_orders = [
    'pastrami',
    'plain',
    'extra paneer',
    'pastrami',
    'cucumber tomatoes capsicum',
    'pastrami',
    'omelette'
]

print("\nHello everyone! We're sorry to announce that we've run out of Patrami for today.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

sandwich_orders = [_.title() + ' Sandwich' for _ in sandwich_orders]

print(f"\nToday's Sandwich Orders:-\n\t{'\n\t'.join(sandwich_orders)}")

# Problem 7-10: Dream Vacation

dream_vacations = {}
poll_continued = True

while poll_continued:
    person = input("\nPlease enter your name: ")
    destination = input(f"{person.title()}, if you could visit one place in the world, where would you go?: ")

    dream_vacations[person] = destination

    continued = input("\nWould you like to give other people the chance to be a part of this poll? (yes/no): ")

    if continued == 'no':
        poll_continued = False

print("\n\t\t#### POLL RESULTS ####\n")
for person, destination in dream_vacations.items():
    print(f"{person.title()} would love to have a vacation in {destination.title()} someday.")
    