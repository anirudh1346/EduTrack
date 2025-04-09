# tests/test_feedback_entry.py

from src.feedback_entry import collect_feedback
import pytest
from unittest.mock import patch
from io import StringIO

def test_collect_feedback_empty_input():
    with patch('builtins.input', return_value='done'):
        assert collect_feedback() == {}

def test_collect_feedback_single_entry():
    inputs = ['S101', 'Good job!', 'done']
    with patch('builtins.input', side_effect=inputs):
        assert collect_feedback() == {'S101': 'Good job!'}

def test_collect_feedback_multiple_entries():
    inputs = ['S101', 'Excellent', 'S102', 'Needs improvement', 'done']
    with patch('builtins.input', side_effect=inputs):
        assert collect_feedback() == {'S101': 'Excellent', 'S102': 'Needs improvement'}