from Rectangle import Rectangle


# def test_can_calc_rectangle_price():
#     r = Rectangle(2, 3)
#     actual = '???'

#     assert actual == r.get_price()



# -----------MOCK--------------------------

def test_can_calc_rectangle_price():
    # arrange
    r = Rectangle(2, 3)

    def mock_get_todays_price_per_unit():
        return 300

    expected = 2 * 3 * 300

    # Act
    actual = r.get_price(mock_get_todays_price_per_unit)

    # Assert
    assert expected == actual
