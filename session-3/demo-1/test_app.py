from unittest.mock import Mock, patch
from app import slow_function_with_DI, slow_function_without_DI


def test_slow_function_with_DI():
    # assemble
    mock_func_to_call = Mock(return_value=500)
    expected = 100 * 500
    
    # act
    actual = slow_function_with_DI(100, mock_func_to_call)
    
    # assert
    assert expected == actual


@patch('app.api_call')
def test_slow_function_without_DI(mock_api_call):
    # assemble
    mock_api_call.return_value = 500
    expected = 100 * 500

    # act
    actual = slow_function_without_DI(100)

    # assert
    assert expected == actual
    assert mock_api_call.call_count == 1
