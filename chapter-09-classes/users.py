# Problem 9-3: Users

class User:
    """
    Creating a user class.
    Attributes: first_name, last_name, hogwarts_house, mastery_field
    Methods: describe_user(), greet_user()
    """

    def __init__(self, first_name, last_name, hogwarts_house, mastery_field):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.hogwarts_house = hogwarts_house.title()
        self.mastery_field = mastery_field.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\nUSER DETAILS:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Hogwarts House: {self.hogwarts_house}")
        print(f"Mastery in: {self.mastery_field}\n")

    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        print(f"Hello {full_name}!\nIt's nice to get to know you:))\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

harry_potter = User('Harry', 'Potter', 'Gryffinfor', 'Defense Against the Dark Arts')
harry_potter.describe_user()
harry_potter.greet_user()

draco_malfoy = User('Draco', 'Malfoy', 'Slytherin', 'Potions')
draco_malfoy.describe_user()
draco_malfoy.greet_user()

luna_lovegood = User('Luna', 'Lovegood', 'Ravenclaw', 'Divinations & Mystical Creatures')
luna_lovegood.describe_user()
luna_lovegood.greet_user()

cedric_diggory = User('Cedric', 'Diggory', 'Hupplepuff', 'Transfiguration')
cedric_diggory.describe_user()
cedric_diggory.greet_user()

# Problem 9-5: Login Attempts

divya = User('Divya', 'Singh', 'Slytherin', 'Charms')

divya.increment_login_attempts()
divya.increment_login_attempts()
divya.increment_login_attempts()
divya.increment_login_attempts()
divya.increment_login_attempts()
divya.increment_login_attempts()

print(f"{divya.first_name} has tried logging in to her account {divya.login_attempts} times.")

divya.reset_login_attempts()
print(f"{divya.first_name}'s login attempts have been reset to {divya.login_attempts}.")

# Problem 9-7: Admin

class Admin(User):
    """
    A class modeling an admin class, a child class of User.
    Attributes(new): privileges:- []
    Methods(new): show_privileges()
    """

    def __init__(self, first_name, last_name, hogwarts_house, mastery_field, privileges):
        super().__init__(first_name, last_name, hogwarts_house, mastery_field)
        self.privileges = [
            'can add post',
            'can delete any post',
            'can ban users'
            ]

    def show_privileges(self):
        print("\nADMIN'S PRIVILEGES:\n")
        for privilege in self.privileges:
            print(privilege.title())
        print()

divya_python = Admin('Divya', 'Python', 'Ravenclaw', 'Ancient Runes','')

divya_python.greet_user()
divya_python.describe_user()
divya_python.show_privileges()

# Problem 9-8: Privileges

class Privileges:
    def __init__(self):   # if you want to add val of attribute in __init__, don't add it to attributes list here
        self.privileges = [
            'can add post',
            'can delete any post',
            'can ban users'
            ]

    def show_privileges(self):
            print("\nADMIN'S PRIVILEGES:\n")
            for privilege in self.privileges:
                print(privilege.title())
            print()

class Admin(User):
    """
    A class modeling an admin class, a child class of User.
    """

    def __init__(self, first_name, last_name, hogwarts_house, mastery_field):
        super().__init__(first_name, last_name, hogwarts_house, mastery_field)
        self.privileges = Privileges()

issabella_lucifer = Admin('Issabella', 'Lucifer', 'Slytherin', 'Arithmancy')

issabella_lucifer.greet_user()
issabella_lucifer.describe_user()
issabella_lucifer.privileges.show_privileges()