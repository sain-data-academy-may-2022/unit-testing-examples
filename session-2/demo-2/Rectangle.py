import requests
import json

# -----Real Function ---------------------------------
# def get_todays_price_per_unit():
#     api_url = "http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000"

#     response = requests.get(api_url)

#     if response.status_code == 200:
#         return json.loads(response.content)[0]
#     else:
#         return None

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    #Inject price_getter_function dependency
    def get_price(self, price_getter_function):
        price_per_unit = price_getter_function() # Execute dependency
        return self.width * self.length * price_per_unit

# r = Rectangle(2, 10)
# print(r.get_price(get_todays_price_per_unit))




