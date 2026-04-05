import pytest

from src.calculator import Calculator


class TestCalculatorBasicOperations:
    def setup_method(self):
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        result = self.calc.add(5, 3)
        assert result == 8.0
        assert isinstance(result, float)

    def test_add_negative_numbers(self):
        assert self.calc.add(-5, -3) == -8.0
        assert self.calc.add(-5, 3) == -2.0
        assert self.calc.add(5, -3) == 2.0

    def test_add_zero(self):
        assert self.calc.add(5, 0) == 5.0
        assert self.calc.add(0, 0) == 0.0

    def test_add_floats(self):
        result = self.calc.add(0.1, 0.2)
        assert round(result, 1) == 0.3

    def test_subtract_positive_numbers(self):
        assert self.calc.subtract(10, 5) == 5.0
        assert self.calc.subtract(5, 10) == -5.0

    def test_subtract_negative_numbers(self):
        assert self.calc.subtract(-10, -5) == -5.0
        assert self.calc.subtract(-5, 5) == -10.0

    def test_multiply_positive_numbers(self):
        assert self.calc.multiply(5, 3) == 15.0
        assert self.calc.multiply(0, 5) == 0.0

    def test_multiply_negative_numbers(self):
        assert self.calc.multiply(-5, 3) == -15.0
        assert self.calc.multiply(-5, -3) == 15.0

    def test_multiply_by_zero(self):
        assert self.calc.multiply(100, 0) == 0.0
        assert self.calc.multiply(0, 0) == 0.0

    def test_divide_positive_numbers(self):
        assert self.calc.divide(10, 2) == 5.0
        assert self.calc.divide(7, 2) == 3.5

    def test_divide_negative_numbers(self):
        assert self.calc.divide(-10, 2) == -5.0
        assert self.calc.divide(-10, -2) == 5.0

    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError) as excinfo:
            self.calc.divide(10, 0)
        assert "Cannot divide by zero" in str(excinfo.value)

    def test_divide_zero_by_number(self):
        assert self.calc.divide(0, 5) == 0.0

    def test_power_positive_exponent(self):
        assert self.calc.power(2, 3) == 8.0
        assert self.calc.power(5, 2) == 25.0

    def test_power_zero_exponent(self):
        assert self.calc.power(5, 0) == 1.0
        assert self.calc.power(0, 0) == 1.0

    def test_power_negative_exponent(self):
        assert self.calc.power(2, -2) == 0.25
        assert self.calc.power(10, -1) == 0.1

    def test_power_fractional_exponent(self):
        assert self.calc.power(4, 0.5) == 2.0
        assert self.calc.power(27, 1 / 3) == 3.0


class TestCalculatorHistory:
    def setup_method(self):
        self.calc = Calculator()

    def test_history_starts_empty(self):
        assert self.calc.get_history() == []

    def test_history_records_operations(self):
        self.calc.add(5, 3)
        self.calc.subtract(10, 2)

        history = self.calc.get_history()
        assert len(history) == 2
        assert "5" in history[0] and "3" in history[0]
        assert "10" in history[1] and "2" in history[1]

    def test_history_clear(self):
        self.calc.add(5, 3)
        self.calc.multiply(2, 4)

        assert len(self.calc.get_history()) == 2

        self.calc.clear_history()
        assert self.calc.get_history() == []

    def test_history_isolation(self):
        self.calc.add(1, 1)

        history1 = self.calc.get_history()
        history1.append("fake entry")

        history2 = self.calc.get_history()
        assert len(history2) == 1

    def test_failed_operation_not_in_history(self):
        initial_length = len(self.calc.get_history())

        try:
            self.calc.divide(10, 0)
        except ValueError:
            pass

        assert len(self.calc.get_history()) == initial_length


class TestCalculatorEdgeCases:
    def setup_method(self):
        self.calc = Calculator()

    def test_very_large_numbers(self):
        large_num = 10**100
        result = self.calc.add(large_num, large_num)
        assert result == float(2 * large_num)

    def test_very_small_numbers(self):
        small_num = 10**-100
        result = self.calc.add(small_num, small_num)
        assert result == 2 * small_num

    def test_string_numbers(self):
        assert self.calc.add("5", "3") == 8.0
        assert self.calc.multiply("2", "4") == 8.0

    def test_mixed_types(self):
        assert self.calc.add(5, 3.5) == 8.5
        assert self.calc.multiply(2, 3.5) == 7.0

    def test_invalid_string_raises_error(self):
        with pytest.raises(ValueError):
            self.calc.add("abc", 5)

    def test_none_values_raise_error(self):
        with pytest.raises(TypeError):
            self.calc.add(None, 5)


class TestCalculatorMultipleInstances:
    def test_independent_histories(self):
        calc1 = Calculator()
        calc2 = Calculator()

        calc1.add(1, 1)
        calc2.add(2, 2)

        assert len(calc1.get_history()) == 1
        assert len(calc2.get_history()) == 1
        assert calc1.get_history() != calc2.get_history()


# Parametrized tests - testing multiple scenarios efficiently
class TestCalculatorParametrized:
    @pytest.fixture
    def calc(self):
        return Calculator()

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (2, 3, 5),
            (0, 0, 0),
            (-5, 5, 0),
            (100, 200, 300),
            (0.1, 0.2, 0.3),
        ],
    )
    def test_add_parametrized(self, calc, a, b, expected):
        result = calc.add(a, b)
        assert round(result, 1) == round(expected, 1)

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (6, 2, 3),
            (10, 5, 2),
            (-10, 2, -5),
            (7, 2, 3.5),
        ],
    )
    def test_divide_parametrized(self, calc, a, b, expected):
        assert calc.divide(a, b) == expected

    @pytest.mark.parametrize(
        "base,exp,expected",
        [
            (2, 2, 4),
            (3, 3, 27),
            (10, 0, 1),
            (5, -1, 0.2),
        ],
    )
    def test_power_parametrized(self, calc, base, exp, expected):
        assert calc.power(base, exp) == expected


class TestCalculatorPerformance:
    def test_many_operations(self):
        calc = Calculator()

        for i in range(1000):
            calc.add(i, i)

        assert len(calc.get_history()) == 1000

    def test_history_memory_management(self):
        calc = Calculator()

        for i in range(10000):
            calc.add(1, 1)

        calc.clear_history()
        assert len(calc.get_history()) == 0

    def test_main_runs(self, capsys):
        from src.calculator import main

        main()

        captured = capsys.readouterr()
        assert "Calculator Demo" in captured.out
        assert "10 + 5 = 15.0" in captured.out
