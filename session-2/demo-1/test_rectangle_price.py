from Rectangle import Rectangle


def test_can_calc_rectangle_price():
    r = Rectangle(2, 3)
    actual = 2 * 3 * 500

    assert actual == r.get_price()
    