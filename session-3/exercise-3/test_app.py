from unittest.mock import patch
from app import add_multiple_products


@patch('builtins.input', side_effect=['Pizza'])
def test_can_add_one_products(mock_input):
    products_list = ['Soup']

    expected = ['Soup', 'Pizza']

    actual = add_multiple_products(products_list, 1)

    assert expected == actual
    assert mock_input.call_count == 1


@patch('builtins.input', side_effect=['Pizza', 'Burger'])
def test_can_add_two_products(mock_input):
    products_list = ['Soup']

    expected = ['Soup', 'Pizza', 'Burger']

    actual = add_multiple_products(products_list, 2)

    assert expected == actual
    assert mock_input.call_count == 2


@patch('builtins.input', side_effect=['Pizza', 'Burger'])
def test_can_add_one_new_and_one_available_products(mock_input):
    products_list = ['Soup', 'Burger']

    expected = ['Soup', 'Burger', 'Pizza']

    actual = add_multiple_products(products_list, 1)

    assert expected == actual
    assert mock_input.call_count == 1

