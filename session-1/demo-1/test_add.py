from app import add_two_numbers


def test_adds_two_numbers():
    # Assemble
    a = 7
    b = 12
    expected = 19

    # Act
    result = add_two_numbers(a, b)

    # Assert
    assert result == expected

test_adds_two_numbers()
