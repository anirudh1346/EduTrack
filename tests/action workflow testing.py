# tests/test_score_calculator.py

from src.score_calculator import calculate_average_score
import pytest

def test_calculate_average_score_empty_list():
    assert calculate_average_score([]) == 0

def test_calculate_average_score_positive_numbers():
    assert calculate_average_score([10, 20, 30]) == 20

def test_calculate_average_score_with_decimals():
    assert calculate_average_score([75.5, 80.5, 90]) == 82.0

def test_calculate_average_score_single_element():
    assert calculate_average_score([100]) == 100