# Problem 5-1: Conditional Tests

favs= ['Python','Building products','Hackathons']

for i in range(len(favs)):
    if i == 0:
        print(f'\n{favs[0]} is my fav programming language.\n')
    elif i == 1:
        print(f'{favs[1]} is what kept me in this stressed field yk, I love it.\n')
    else:
        print(f'{favs[-1]} have been my main choices for making projects. Most of what I build is for hackathons so far.')

# Test Cases

# All True Cases
print()

print(True == 1)
print(False == 0)
print(3 % 100 != 0)

test_list = ['a','b','c']
print('d' not in test_list)

print(True or False)

# All False Cases
print()

print(True and False)
print(True & True & False)
print(False == '')
print(False == [])
print(0 == '0')

print()

# Problem 5-2: More Conditional Tests

print('Divya' == 'Divya')
print('Divya' == 'divya') # False
print('Divya'.lower() == 'divya'.lower()) # True
print()

a,b = 18,50
print(a == b)
print(a != b)
print(a < 18 and b >= 21)
print(a < 18 or b >= 21)

test = ['Python','Go','TS','FastAPI']
print()
print('JS' not in test)
print('Python' in test)
