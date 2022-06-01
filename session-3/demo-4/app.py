from typing import List, Union


Num = Union[int, float]


def add_price(price_list: List[Num]): # No DI
    value = int(input("Please enter a number: ")) # Dependency
    price_list.append(value)
    return price_list
