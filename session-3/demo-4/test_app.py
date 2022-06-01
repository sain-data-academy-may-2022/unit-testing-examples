from unittest.mock import patch

from app import add_price

@patch("builtins.input")
def test_add_price(mock_input):
    # Arrange
    mock_input.return_value = '50'
    price_list = [10, 20]
    expected = [10, 20, 50]
    # Act
    actual = add_price(price_list) 

    # Assert
    assert actual == expected
    assert mock_input.call_count == 1

