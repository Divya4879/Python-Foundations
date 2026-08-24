# Problem 4-10: Slices

problem_list= ['DSA' , 'Python', 'Backend Dev', 'Job' , 'JS' , 'TS' , 'FastAPI' , 'NextJS']

print(f"The first three items in the list are: \n{'\n'.join(list(problem_list[:3]))}")

n=len(problem_list)-4
print(f"\nThe three items from the middle of the list are: \n{'\n'.join(list(problem_list[n:-1]))}")

print(f"\nThe last three items from the the list are: \n{'\n'.join(list(problem_list[-3:]))}")

# Problem 4-11: My Pizzas, Your Pizzas

my_tech_stack= ['Python', 'JS', 'React', 'TS', 'FastAPI']
friend_tech_stack = my_tech_stack[:] # copying list using slicing, else both lists will be same forever

my_tech_stack.append('Postgres')
friend_tech_stack.append('Go')

print('\nMy current tech stack is:- ')
for _ in my_tech_stack:
    print(_)

print("\nMy friend's current tech stack is:- ")
for _ in friend_tech_stack:
    print(_)
