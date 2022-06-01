from unittest.mock import patch

from app import hello_to_you

@patch("builtins.print")
def test_prints_hello_to_you(mock_print):
    hello_to_you("John") # Act
    mock_print.assert_called_with("Hello, John!") # Passes