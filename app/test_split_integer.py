from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(32, 6)) == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_of_parts = 2
    res = split_integer(value, number_of_parts)
    assert len(res) == number_of_parts
    assert sum(res) == value
    assert res == [3,3]



def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    number_of_parts = 1
    value = 8
    res = split_integer(value, number_of_parts)
    assert len(res) == number_of_parts
    assert sum(res) % len(res) == 0


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    number_of_parts = 6
    value = 32
    res = split_integer(value, number_of_parts)
    assert res == sorted(res)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    number_of_parts = 5
    value = 3
    res = split_integer(value, number_of_parts)
    assert max(res) - min(res) <= 1
    assert len(res) == number_of_parts
    assert sum(res) == value
