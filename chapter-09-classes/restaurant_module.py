# Problem 9-10: Imported Restaurant

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