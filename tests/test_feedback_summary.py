# tests/test_feedback_summary.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from feedback_summary import summarize_feedback

def test_summarize_feedback():
    data = [
        {"score": 85, "grade": "A"},
        {"score": 90, "grade": "A"},
        {"score": 70, "grade": "B"},
        {"score": 90, "grade": "A"},
        {"score": 60, "grade": "C"}
    ]
    summary = summarize_feedback(data)
    assert summary["top_score"] == 90
    assert summary["grade_counts"] == {"A": 3, "B": 1, "C": 1}
