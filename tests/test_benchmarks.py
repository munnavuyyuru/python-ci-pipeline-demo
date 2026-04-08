"""
Performance benchmark tests.
These tests measure execution time to catch performance regressions.
"""

import pytest

from src.calculator import Calculator
from src.utils import calculate_average, find_max_min


class TestCalculatorBenchmarks:
    def test_benchmark_addition(self, benchmark):
        calc = Calculator()
        result = benchmark(calc.add, 100, 200)
        assert result == 300

    def test_benchmark_multiplication(self, benchmark):
        calc = Calculator()
        result = benchmark(calc.multiply, 123, 456)
        assert result == 123 * 456

    def test_benchmark_power(self, benchmark):
        calc = Calculator()
        result = benchmark(calc.power, 2, 10)
        assert result == 1024

    def test_benchmark_division(self, benchmark):
        calc = Calculator()
        result = benchmark(calc.divide, 1000, 7)
        assert abs(result - (1000 / 7)) < 0.0001

    def test_benchmark_history_operations(self, benchmark):
        calc = Calculator()

        def perform_operations():
            for i in range(100):
                calc.add(i, i + 1)
            return calc.get_history()

        result = benchmark(perform_operations)
        assert len(result) == 100


class TestUtilsBenchmarks:
    def test_benchmark_average_small_list(self, benchmark):
        numbers = list(range(100))
        result = benchmark(calculate_average, numbers)
        assert result == 49.5

    def test_benchmark_average_large_list(self, benchmark):
        numbers = list(range(10000))
        result = benchmark(calculate_average, numbers)
        assert result == 4999.5

    def test_benchmark_max_min_small_list(self, benchmark):
        numbers = list(range(100))
        max_val, min_val = benchmark(find_max_min, numbers)
        assert max_val == 99
        assert min_val == 0

    def test_benchmark_max_min_large_list(self, benchmark):
        numbers = list(range(10000))
        max_val, min_val = benchmark(find_max_min, numbers)
        assert max_val == 9999
        assert min_val == 0
