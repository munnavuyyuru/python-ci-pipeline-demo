import pytest

from src.utils import (
    calculate_average,
    find_max_min,
    format_result,
    is_number,
    validate_inputs,
)


class TestIsNumber:
    def test_integer_is_number(self):
        assert is_number(5) is True
        assert is_number(-5) is True
        assert is_number(0) is True

    def test_float_is_number(self):
        assert is_number(5.5) is True
        assert is_number(-5.5) is True
        assert is_number(0.0) is True

    def test_string_number_is_number(self):
        assert is_number("5") is True
        assert is_number("5.5") is True
        assert is_number("-5.5") is True

    def test_non_number_string(self):
        assert is_number("abc") is False
        assert is_number("12abc") is False
        assert is_number("") is False

    def test_none_is_not_number(self):
        assert is_number(None) is False

    def test_list_is_not_number(self):
        assert is_number([1, 2, 3]) is False

    def test_special_float_values(self):
        assert is_number(float("inf")) is True
        assert is_number(float("-inf")) is True

        assert is_number(float("nan")) is True


class TestValidateInputs:
    def test_all_valid_numbers(self):
        assert validate_inputs(1, 2, 3) is True
        assert validate_inputs(1.5, 2.5, 3.5) is True
        assert validate_inputs("1", "2", "3") is True

    def test_mixed_valid_numbers(self):
        assert validate_inputs(1, "2", 3.5) is True

    def test_one_invalid_input(self):
        assert validate_inputs(1, "abc", 3) is False

    def test_all_invalid_inputs(self):
        assert validate_inputs("abc", "def", "ghi") is False

    def test_empty_inputs(self):
        assert validate_inputs() is True  # All (zero) inputs are valid

    def test_none_in_inputs(self):
        assert validate_inputs(1, None, 3) is False


class TestFormatResult:
    def test_default_precision(self):
        assert format_result(3.14159) == "3.14"
        assert format_result(2.5) == "2.50"

    def test_custom_precision(self):
        assert format_result(3.14159, 3) == "3.142"
        assert format_result(3.14159, 0) == "3"
        assert format_result(3.14159, 5) == "3.14159"

    def test_integer_formatting(self):
        assert format_result(5, 2) == "5.00"
        assert format_result(5, 0) == "5"

    def test_negative_numbers(self):
        assert format_result(-3.14159, 2) == "-3.14"

    def test_zero_formatting(self):
        assert format_result(0, 2) == "0.00"
        assert format_result(0.0, 3) == "0.000"

    def test_very_small_numbers(self):
        assert format_result(0.000001, 6) == "0.000001"
        assert format_result(0.000001, 2) == "0.00"


class TestCalculateAverage:
    def test_average_positive_numbers(self):
        assert calculate_average([1, 2, 3, 4, 5]) == 3.0
        assert calculate_average([10, 20, 30]) == 20.0

    def test_average_negative_numbers(self):
        assert calculate_average([-1, -2, -3]) == -2.0

    def test_average_mixed_numbers(self):
        assert calculate_average([-5, 0, 5]) == 0.0

    def test_average_single_number(self):
        assert calculate_average([42]) == 42.0

    def test_average_floats(self):
        result = calculate_average([1.5, 2.5, 3.5])
        assert round(result, 1) == 2.5

    def test_empty_list_raises_error(self):
        with pytest.raises(ValueError) as excinfo:
            calculate_average([])
        assert "empty list" in str(excinfo.value).lower()

    def test_average_with_zero(self):
        assert calculate_average([0, 0, 0]) == 0.0
        assert calculate_average([1, 0, -1]) == 0.0


class TestFindMaxMin:
    def test_max_min_positive_numbers(self):
        max_val, min_val = find_max_min([1, 5, 3, 9, 2])
        assert max_val == 9
        assert min_val == 1

    def test_max_min_negative_numbers(self):
        max_val, min_val = find_max_min([-1, -5, -3, -9, -2])
        assert max_val == -1
        assert min_val == -9

    def test_max_min_mixed_numbers(self):
        max_val, min_val = find_max_min([-5, 0, 5, -10, 10])
        assert max_val == 10
        assert min_val == -10

    def test_max_min_single_number(self):
        max_val, min_val = find_max_min([42])
        assert max_val == 42
        assert min_val == 42

    def test_max_min_duplicates(self):
        max_val, min_val = find_max_min([5, 5, 5, 5])
        assert max_val == 5
        assert min_val == 5

    def test_max_min_floats(self):
        max_val, min_val = find_max_min([1.1, 2.2, 3.3, 0.5])
        assert max_val == 3.3
        assert min_val == 0.5

    def test_empty_list_raises_error(self):
        with pytest.raises(ValueError) as excinfo:
            find_max_min([])
        assert "empty list" in str(excinfo.value).lower()

    def test_max_min_with_zero(self):
        max_val, min_val = find_max_min([0, -5, 5])
        assert max_val == 5
        assert min_val == -5


# Parametrized tests for utilities
class TestUtilsParametrized:
    @pytest.mark.parametrize(
        "value,expected",
        [
            (5, True),
            ("5", True),
            (5.5, True),
            ("abc", False),
            (None, False),
            ([1, 2], False),
        ],
    )
    def test_is_number_parametrized(self, value, expected):
        assert is_number(value) == expected

    @pytest.mark.parametrize(
        "numbers,expected",
        [
            ([1, 2, 3], 2.0),
            ([10], 10.0),
            ([0, 0, 0], 0.0),
            ([-1, 1], 0.0),
        ],
    )
    def test_calculate_average_parametrized(self, numbers, expected):
        assert calculate_average(numbers) == expected

    @pytest.mark.parametrize(
        "numbers,expected_max,expected_min",
        [
            ([1, 5, 3], 5, 1),
            ([10], 10, 10),
            ([-1, -5, -3], -1, -5),
            ([0, 10, -10], 10, -10),
        ],
    )
    def test_find_max_min_parametrized(self, numbers, expected_max, expected_min):
        max_val, min_val = find_max_min(numbers)
        assert max_val == expected_max
        assert min_val == expected_min
