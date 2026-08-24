# Problem 5-3: Alien Colors #1

alien_color = 'green'

if alien_color == 'green':
    print('Yay! You just earned 5 points!')

if alien_color == 'red':
    print("Right choice! You're 5 points richer now.")

# Problem 5-4: Alien Colors #2

alien_color = 'green'

if alien_color == 'green':
    print('5 points earned! Stay green.')
else:
    print('10 points earned:)) Stay green.')

if alien_color != 'green':
    print('5 points earned! Stay !green.')
else:
    print('10 points earned:)) Stay !green.\n')

# Problem 5-5: Alien Colors #3

alien_colors = ['green','yellow','red']

for color in alien_colors:
    if color == 'green':
        print('Congo! You just earned 5 points.\n')
    elif color == 'yellow':
        print('Congo! You just earned 10 points.\n')
    else:
        print('Congo! You just earned 15 points.\n')

# Problem 5-6: Stages of Life

age = int(input("Please enter your age here: "))

if age < 2:
    print("Yo baby! What're you doing here?")
elif age < 4:
    print("Naughty toddler! No internet until you're 8 atleast:))")
elif age < 13:
    print("Hello kiddo! How's life treating you?")
elif age < 20:
    print("Hello teenager! Don't be dramatic.")
elif age < 65:
    print("Hello 'responsible' adult! Do you sleep when you should?")
elif age >= 65:
    print("Hello sir/madam. Wish you a blessed day!!")

print()

# Problem 5-7: Favorite Fruits

fruits= ['mangoes','apples','oranges','strawberries','bananas']

if 'mangoes' in fruits:
    print('I like mangoes.\n')
if 'lemons' in fruits:
    print("Can't be. Ik myself.\n")
if 'bananas' in fruits:
    print("Mg + Phosphorus. Yup they're here.\n")
if 'strawberries' in fruits:
    print("Fresh strawberries dipped in chocolate. Yum!\n")
if 'avocadoes' in fruits:
    print("Haven't had them yet.\n")
