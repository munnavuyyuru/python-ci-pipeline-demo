"""
Python Demo Package
"""

__version__ = "0.1.0"
__author__ = "Venkata Bhargav"

from .calculator import Calculator
from .utils import (
    calculate_average,
    find_max_min,
    format_result,
    is_number,
    validate_inputs,
)

__all__ = [
    "Calculator",
    "is_number",
    "validate_inputs",
    "format_result",
    "calculate_average",
    "find_max_min",
]
