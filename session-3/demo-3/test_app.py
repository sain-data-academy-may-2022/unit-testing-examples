from unittest.mock import patch
from app import greeting


@patch("builtins.input")
def test_greeting(mock_input):
    # Arrange
    mock_input.return_value = 'Jessica'
    expected = 'Nice to meet you, Jessica'

    # Act
    actual = greeting()

    # Assert
    assert actual == expected
    assert mock_input.call_count == 1
