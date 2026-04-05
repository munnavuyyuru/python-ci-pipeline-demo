from typing import Any, List, Union


def is_number(value: Any) -> bool:
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def validate_inputs(*args) -> bool:
    return all(is_number(arg) for arg in args)


def format_result(result: float, precision: int = 2) -> str:
    return f"{result:.{precision}f}"


def calculate_average(numbers: List[Union[int, float]]) -> float:
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")

    return sum(numbers) / len(numbers)


def find_max_min(numbers: List[Union[int, float]]) -> tuple:
    if not numbers:
        raise ValueError("Cannot find max/min of empty list")

    return (max(numbers), min(numbers))
