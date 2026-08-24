from user import User

class Privileges:
    def __init__(self):  
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