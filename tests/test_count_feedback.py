# tests/test_count_feedback.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from count_feedback import count_feedback_entries

def test_count_feedback_entries():
    feedback_data = [
        {"student_name": "John Doe", "score": 85, "grade": "A"},
        {"student_name": "Jane Doe", "score": 90, "grade": "A"},
        {"student_name": "John Doe", "score": 70, "grade": "B"}
    ]
    stats = count_feedback_entries(feedback_data)
    assert stats["total_count"] == 3
    assert stats["grade_counts"] == {"A": 2, "B": 1}

def test_count_feedback_entries_empty_data():
    feedback_data = []
    stats = count_feedback_entries(feedback_data)
    assert stats["total_count"] == 0
    assert stats["grade_counts"] == {}

def test_count_feedback_entries_single_entry():
    feedback_data = [
        {"student_name": "John Doe", "score": 85, "grade": "A"}
    ]
    stats = count_feedback_entries(feedback_data)
    assert stats["total_count"] == 1
    assert stats["grade_counts"] == {"A": 1}
