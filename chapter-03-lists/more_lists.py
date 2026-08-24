# Problem 3-8: Seeing the World

places_to_visit = ['Paris', 'London', 'New York', 'Switzerland', 'Los Angeles']
places_to_visit=[place.lower() for place in places_to_visit]

print(places_to_visit)
print(sorted(places_to_visit))
print(places_to_visit)

print()
print(sorted(places_to_visit,reverse=True))
print(places_to_visit)

print()
places_to_visit.reverse()
print(places_to_visit)

places_to_visit.reverse()
print()
print(places_to_visit)

print()
places_to_visit.sort()
print(places_to_visit)

print()
places_to_visit.sort(reverse=True)
print(places_to_visit)

# 3-9: Dinner Guests

import guest_list

print(f"\nI'm inviting {len(guest_list.guests)} to my dinner party soon.")

# 3-10: Every Function

my_function = ['Divya', 'family', 'building', 'career', 'relationships', 'life', 'health', 'fitness', 'weight loss', 'dumbell', 'planks', 'life partner', 'python', 'India', 'taxes', 4]

# 3-11: Intentionl Error

lists = [4, 'Divya', 'Python', "Backend", "Getting a Job"]
# print(lists[len(lists)]) # Index Error

print(lists[len(lists)-1])