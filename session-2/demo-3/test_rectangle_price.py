from Rectangle import Rectangle


# def test_can_calc_rectangle_price():
#     r = Rectangle(2, 3)
#     actual = '???'

#     assert actual == r.get_price()



# -----------MOCK--------------------------
from unittest.mock import Mock


def test_can_calc_rectangle_price():
    # assemble
    mock_get_todays_price_per_unit = Mock(return_value=300)
    r = Rectangle(2, 3)
    actual = 2 * 3 * 300

    # act & assert
    assert actual == r.get_price(mock_get_todays_price_per_unit)
    assert mock_get_todays_price_per_unit.call_count == 1
    assert mock_get_todays_price_per_unit.assert_called
