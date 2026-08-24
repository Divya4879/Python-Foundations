# Problem 4-3: Counting to Twenty

for item in range(1,21):
    print(item,end=' ')

# Problem 4-4: One Million

for item in range(1,1000_001):
    print(item, end=' ')
print()

# Problem 4-5: Summing a Million

numbers= [item for item in range(1,1000_001)]

print(min(numbers))
print(max(numbers))
print(sum(numbers))
print()

# Problem 4-6: Odd Numbers

for num in range(1,21,2):
    print(num)
print()

# Problem 4-7: Threes

for num in range(1,11):
    print(f"3 * {num} = {3 * num}")
print()


for num in range(3,31,3):
    print(num)
print()

# Problem 4-8: Cubes

cubes= [val**3 for val in range(1,11)]
for cube in cubes:
    print(cube)
print()

# Problem 4-9: Cube Comprehension

cubes= [val**3 for val in range(1,11)]