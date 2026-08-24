# Problem 4-13: Buffet

foods = ('Oatmeal', 'Ice Cream', 'Chocolate', 'Burger', 'Pizza')

print('The restaurant offers these food items:-')
for food in foods:
    print(food)

print()

# foods[0]= 'Maggi' # TypeError: 'tuple' object does not support item assignment

# Having to recreate the entire tuple for changing some items 
# coz tuple is an immutable list.

foods= ('Oatmeal', 'Palak Paneer', 'Chocolate', 'Burger', 'Cookies')
print("The revised food items in the restaurant's menu :-")
for food in foods:
    print(food)