"""
Chapter 9: Classes and Object-Oriented Programming
This module covers instantiation, state modification, inheritance, 
composition, module imports (including standard library), and PEP 8 styling.
"""

# ---------------------------------------------------------
# PEP 8 IMPORT STYLING RULE
# ---------------------------------------------------------
# 1. Standard library imports go first.
from random import randint, choice

# 2. Add exactly one blank line.

# 3. Then import your own custom modules/classes.
# from car import ElectricCar as EC
# import electric_car as ec


# ---------------------------------------------------------
# 1. THE FOUNDATION & MULTIPLE INSTANCES
# ---------------------------------------------------------
# PEP 8 Rule: Class names should be written in CamelCase (no underscores).
# Instance and module names should be written in lowercase with underscores.
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name  
        self.age = age

    # PEP 8 Rule: Within a class, use exactly one blank line between methods.
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


# PEP 8 Rule: Within a module, use exactly two blank lines to separate classes.


# ---------------------------------------------------------
# 2. STATE AND MODIFYING ATTRIBUTES
# ---------------------------------------------------------
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Standard cars have gas tanks."""
        print("Filling up the gas tank now!")


# ---------------------------------------------------------
# 3. COMPOSITION (MODELING THE REAL WORLD)
# ---------------------------------------------------------
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")


# ---------------------------------------------------------
# 4. INHERITANCE AND METHOD OVERRIDING
# ---------------------------------------------------------
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        
        # Composition: Assign a Battery instance as an attribute.
        self.battery = Battery()

    # METHOD OVERRIDING
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")


# ==========================================
# EXECUTION & TESTING
# ==========================================
print("--- Standard Library ---")
print(f"Random number between 1 and 6: {randint(1, 6)}")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(f"Random player selected: {choice(players)}")

print("\n--- Foundation & Multiple Instances ---")
# You can make as many instances from one class as you need
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

my_dog.sit()
my_dog.roll_over()
print(f"My friend's dog is named {your_dog.name}.")

print("\n--- Modifying State (3 Ways) ---")
my_used_car = Car('subaru', 'outback', 2019)
my_used_car.odometer_reading = 23
my_used_car.update_odometer(23_500)
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

print("\n--- Inheritance, Overriding & Composition ---")
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.fill_gas_tank() 
my_leaf.battery.describe_battery() 
my_leaf.battery.get_range()