from app import random_list_generator
from unittest.mock import Mock


def test_random_list_generator():
    mock_randint = Mock(return_value=3)
    n = 4
    expected = [3, 3 , 3, 3]

    actual = random_list_generator(n, mock_randint)

    assert actual == expected

