from app import price_updater

# normal case
def test_price_updater():
    price_list, increase_rate = [10, 20], 0.1
    expected = [11, 22]
    assert price_updater(price_list, increase_rate) == expected

    price_list, increase_rate = [10, 20], 0.0
    expected = [10, 20]
    assert price_updater(price_list, increase_rate) == expected

    price_list, increase_rate = [10, 20], 1.0
    expected = [20, 40]
    assert price_updater(price_list, increase_rate) == expected

test_price_updater()


# --------after installing pytest----------------

# import pytest

# def test_price_updater_errors():
#     price_list, increase_rate = [10, 20], '0.1'
#     with pytest.raises(TypeError):
#         price_updater(price_list, increase_rate)

#     price_list, increase_rate = [10, 20], 10.0
#     with pytest.raises(ValueError):
#         price_updater(price_list, increase_rate)
