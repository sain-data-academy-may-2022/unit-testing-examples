from unittest.mock import patch
from app import get_user_details


@patch('builtins.input', side_effect=['Jane', '25'])
@patch('builtins.print')
def test_get_user_details(mock_print, mock_input):
    get_user_details()
    mock_print.assert_called_with("Thank you, your name is Jane and your age is 25")
    assert mock_input.call_count == 2
    assert mock_print.call_count == 1
