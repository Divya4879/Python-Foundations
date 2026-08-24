# Problem 10-1: Learning Python

from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

learning_python_list = []
count = 1

for line in contents.splitlines():
    if 'In Python you can' in line:
        print(line)
        learning_python_list.append(line.removeprefix('In Python you can- '))


print('\nIn Python you can:-\n')
for item in learning_python_list:
    print(f"{count}: {item}")
    count +=1

# Problem 10-2: Learning C

path = Path('learning_python.txt')
contents = path.read_text()

print("\nGO VERSION:\n")
for line in contents.splitlines():
    if 'In Python you can' in line:
        # string immutable, so once you change it, 
        # you need to assign to a var- can be a new one, or same one.
        line = line.replace('Python','Go') 
        print(line)

# Problem 10-3: Simpler code

"""
We just removed the temp_var, 'lines'= contents.splitlines(),
and directly used this method in the file handling, in the code file.

No extra temp_var overhead.
"""