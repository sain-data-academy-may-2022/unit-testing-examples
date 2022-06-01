from unittest.mock import patch

from app import print_name

@patch("builtins.input")
@patch("builtins.print")
def test_print_name(mock_print, mock_input):
    # Arrange
    mock_input.return_value = "John"

    # Act
    print_name() 

    # Assert
    mock_print.assert_called_with("Hello, John!") # Passes
    assert mock_input.call_count == 1
    assert mock_print.call_count == 1
