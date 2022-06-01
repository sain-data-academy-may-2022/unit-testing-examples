# from unittest.mock import patch, Mock, MagicMock

# from app import my_file_reader


# @patch("builtins.open")
# def test_print_name(mock_open):
#     mock_file = Mock()
#     mock_file.readlines.return_value = ['John\n', 'Jessica\n']

#     mock_open.return_value = mock_file

#     actual = my_file_reader('any_path')

#     mock_open.assert_called_once_with("any_path", "r")
#     assert actual == ['John\n', 'Jessica\n']
