from typing import Union, List


Num = Union[int, float]


# def price_updater(price_list: List[Num], increase_rate: float) -> List[Num]:
#     new_price_list = []
#     for price in price_list:
#         new_price_list.append(price + price * increase_rate)
#     return new_price_list


def price_updater(price_list: List[Num], increase_rate: float) -> List[Num]:
    if not isinstance(increase_rate, float):
        raise TypeError('increase_rate data type should be float')
    if increase_rate < 0 or increase_rate > 1:
        raise ValueError('increase_rate should follow the constraints')
    new_price_list = []
    for price in price_list:
        new_price_list.append(price + price * increase_rate)
    return new_price_list