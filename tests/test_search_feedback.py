# tests/test_search_feedback.py

import pytest
from search_feedback import search_feedback_by_name

def test_search_feedback_by_name_found():
    feedback_data = [
        {"student_name": "John Doe", "score": 85, "grade": "A"},
        {"student_name": "Jane Doe", "score": 90, "grade": "A"},
        {"student_name": "John Doe", "score": 70, "grade": "B"}
    ]
    student_name = "John Doe"
    results = search_feedback_by_name(feedback_data, student_name)
    assert len(results) == 2

def test_search_feedback_by_name_not_found():
    feedback_data = [
        {"student_name": "John Doe", "score": 85, "grade": "A"},
        {"student_name": "Jane Doe", "score": 90, "grade": "A"}
    ]
    student_name = "Bob Smith"
    results = search_feedback_by_name(feedback_data, student_name)
    assert len(results) == 0

def test_search_feedback_by_name_empty_data():
    feedback_data = []
    student_name = "John Doe"
    results = search_feedback_by_name(feedback_data, student_name)
    assert len(results) == 0
