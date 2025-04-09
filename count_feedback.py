# count_feedback.py

def count_feedback_entries(feedback_data):
    """
    Counts the total number of feedback entries and provides additional statistics.

    Parameters:
    - feedback_data (list of dict): List of feedback dictionaries.

    Returns:
    - A dictionary containing the total count and other statistics.
    """
    total_count = len(feedback_data)
    grade_counts = {}
    
    for entry in feedback_data:
        grade = entry.get("grade")
        if grade in grade_counts:
            grade_counts[grade] += 1
        else:
            grade_counts[grade] = 1
    
    return {"total_count": total_count, "grade_counts": grade_counts}

# Example usage
if __name__ == "__main__":
    feedback_data = [
        {"student_name": "John Doe", "score": 85, "grade": "A"},
        {"student_name": "Jane Doe", "score": 90, "grade": "A"},
        {"student_name": "John Doe", "score": 70, "grade": "B"},
        {"student_name": "Jane Doe", "score": 90, "grade": "A"},
        {"student_name": "John Doe", "score": 60, "grade": "C"}
    ]
    
    stats = count_feedback_entries(feedback_data)
    
    print("Feedback Statistics:")
    print(f"Total Entries: {stats['total_count']}")
    print("Grade Counts:")
    for grade, count in stats["grade_counts"].items():
        print(f"{grade}: {count}")
