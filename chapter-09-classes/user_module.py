# Problem 9-11: Imported Admin

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