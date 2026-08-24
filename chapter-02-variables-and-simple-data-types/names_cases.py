# Problem 2-3: Personal Message

first_name="Divya"
middle_name="successful"
last_name="Singh"

full_name=f"{first_name} {middle_name} {last_name}"
greeting= f"Hello {full_name}!! Let's accelerate through these books, the concepts, the exercises, everything and get placed ASAP!"

print(greeting)

# Problem 2-4: Name Cases

print(full_name.lower())
print(full_name.upper())
print(full_name.title())

# Problem 2-5: Famous Quote

author="Albert Einstein"
quote="A person who never made a mistake never tried anything new."

print(f'{author} once said, "{quote}"')

# Problem 2-6: Famous Quote 2

famous_person="Albert Einstein"
message= f'{famous_person} once said, "{quote}"'
print(message)

# Problem 2-7: Stripping Names

names=["Divya","Riya","Khushi","Issabella"]
print(f"My names are:\t{names[0]}\n\t\t{names[1]}\n\t\t{names[2]}\n\t\t{names[3]}")

name="\nDivya"
print(name)
print(name.lstrip())
print(name)

name=name.lstrip()
print(name)

name='\n\tDivya\n'
print(name)
print(name.rstrip())
print(name.lstrip())
print(name.strip())
print(name)

name=name.strip()
print(name)

# Problem 2-8: File Extensions

filename='https://www.google.com/'
print(filename.removeprefix('https://'))
print(filename.removesuffix('/'))
print(filename.removeprefix('https://').removesuffix('/'))
