# Problem 11-3: Employee

class Employee:
    """A class modeling a real-world employee."""

    def __init__(self, first_name, last_name, salary):
        """__init__ function stating attributes of this class."""

        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self,salary=5000):
        """Method to increase salary by a default/given amount."""
        self.salary += salary