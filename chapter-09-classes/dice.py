import random

# PROBLEM 9-13: DICE

class Dice:
    """A class Dice, representing a real-world dice."""
    def __init__(self, sides=6):
        self.sides=sides

    def roll_die(self):
        random_no = random.randint(1,self.sides)
        print(f"The {self.sides}-sided dice rolled and landed on a {random_no}.")

my_dice = Dice()
print("\nMy Dice:\n")
for i in range(10):
    my_dice.roll_die()

new_dice = Dice(10)
print("\nYour Dice:\n")
for i in range(10):
    new_dice.roll_die()

random_dice = Dice(20)
print("\nRandom Dice:\n")
for i in range(10):
    random_dice.roll_die()