from pathlib import Path

path = Path('lines_count.txt')
contents = path.read_text().rstrip()
contents = contents
print(contents)

# Using Absolute Paths in different folder
path = Path("C:/Users/LENOVO/desktop/python-crash-course/CHAPTER 1/test.txt")
contents = path.read_text()
print(contents)

# Works with .py extension as well, just simply gives everything in the file

path = Path('C:/Users/LENOVO/desktop/python-crash-course/chapter-01-getting-started/hello_world.py')
content = path.read_text()
print(content)

# Using Relative Paths in different folder

path_relative = Path('../chapter-01-getting-started/test.txt') ## used ../Folder_name/file_name.extension in relative path
content_relative_path = path_relative.read_text()

lines = content_relative_path.splitlines()
for line in lines:
    print(line)

# Section: Working with a File's contents

path = Path('../chapter-01-getting-started/test.txt')
contents = path.read_text()
lines = contents.splitlines()
line_string = ''
for line in lines:
    # line.rstrip() or line.rstrip() or line.strip()- if there're extra blank spaces
    line_string += line 

print(line_string)
print(len(line_string))