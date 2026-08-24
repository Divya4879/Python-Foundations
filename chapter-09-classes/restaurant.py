# Problem 9-1: Restaurant

class Restaurant:
    """
    A class trying to model a restaurant.
    Attributes are: restaurant_name & cuisine_type
    Methods are: decribe_restaurant() & open_restaurant()
    """
    def __init__(self, restaurant_name, cuisine_type):
        """
        Init Method:- attributes are self, and the 2 attributes for Restaurant class.
        """
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.capitalize()
        self.number_served = 0

    def describe_restaurant(self):
        """
        Method describing the Restaurant class.
        Use self in arguments of the function method.
        describe_restaurant(self)
        """
        print(f"{self.restaurant_name} is famous for its {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """
        Method stating a simple message.
        Use self in arguments of the function method.
        open_restaurant(self)
        """
        print("Hello customer! Our restaurant is open for you.")

    def set_number_served(self, customers_served):
        """
        Sets the number_served (total no of customers) to a set value.
        """
        if customers_served>=self.number_served:
            self.number_served = customers_served
        else:
            print("You can't decrement the customers count of the restaurant!\n")

    def increment_number_served(self, customer_count):
        """
        Method to increment number_served with the customer_count each time.
        """
        if customer_count > 0:
            self.number_served += customer_count
        else:
            print("Negative no. of customers coming to the restaurant! Really!\n")

restaurant = Restaurant('Gokul Restaurant', 'confectionaries')

print(f"{restaurant.restaurant_name} is located in my city.")
print(f"It's pretty renowned for its food, especially for its {restaurant.cuisine_type}.")

restaurant.describe_restaurant()
restaurant.open_restaurant()

# Problem 9-2: Three Restaurants

taj_hotel = Restaurant("Taj Hotel", "mushroom")
harry_parlor = Restaurant("Harry Parlours", "ice cream")
sweet_corner = Restaurant("Sweet Corner", "sweets")

print()
taj_hotel.describe_restaurant()
harry_parlor.describe_restaurant()
sweet_corner.describe_restaurant()

# Problem 9-4: Number Served

restaurant_new = Restaurant('Divya Drinks', 'fruits juice')
restaurant_new.describe_restaurant()
restaurant_new.open_restaurant()

print(f"""\nSince it's just opened this noon, the no of customers it has served so far is {restaurant_new.number_served}.\n""")

restaurant_new.set_number_served(2)
restaurant_new.set_number_served(5)
restaurant_new.set_number_served(-10)
restaurant_new.increment_number_served(5)
restaurant_new.increment_number_served(2)
restaurant_new.increment_number_served(-1)
restaurant_new.increment_number_served(15)

print(f"""Well well well!
So far we've received {restaurant_new.number_served} customers since the opening:)""")

# Problem 9-6: Ice Cream Stand

class IceCreamStand(Restaurant):
    """
    Class modeling an ice-cream stand, child class of Restaurant class.
    """
    def __init__(self, restaurant_name, cuisine_type, flavors): # flavors added to child class attribute in its init method
        # No self attribute in this super().init method
        super().__init__(restaurant_name, cuisine_type)
        
        self.flavors = flavors
        self.cuisine_type = 'Ice Cream'

    def display_flavors(self):
        print("\nFLAVORS OFFERED:\n")
        for flavor in self.flavors:
            print(flavor.title())

dia_stand = IceCreamStand('Dia Stands',"",
    ['Strawberry', 'Chocolate', 'Raspberry', 'Vanilla', 'Hazelnut', 'Mango'])

print(f"\n{dia_stand.restaurant_name} is my cousion's {dia_stand.cuisine_type} stand.")
dia_stand.display_flavors()

print()