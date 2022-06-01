def get_todays_price_per_unit():
    return 500


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_price(self):
        price_per_unit = get_todays_price_per_unit() # Dependency
        return self.width * self.length * price_per_unit


# ------------------------------------------
import time


def get_todays_price_per_unit():
    time.sleep(3)
    return 500


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_price(self):
        price_per_unit = get_todays_price_per_unit() # Dependency
        return self.width * self.length * price_per_unit

# r = Rectangle(2, 10)
# print(r.get_price())


# --------------------------DI----------------------------------
# class Rectangle:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
    
#     #Inject price_getter_function dependency
#     def get_price(self, price_getter_function):
#         price_per_unit = price_getter_function() # Execute dependency
#         return self.width * self.length * price_per_unit

# r = Rectangle(2, 10)
# print(r.get_price(get_todays_price_per_unit))

