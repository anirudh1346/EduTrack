# search_feedback.py

def search_feedback_by_name(feedback_data, student_name):
    """
    Searches for feedback entries by student name.

    Parameters:
    - feedback_data (list of dict): List of feedback dictionaries.
    - student_name (str): Name of the student to search for.

    Returns:
    - A list of feedback entries matching the student name.
    """
    matching_feedback = [entry for entry in feedback_data if entry.get("student_name") == student_name]
    return matching_feedback

# Example usage
if __name__ == "__main__":
    feedback_data = [
        {"student_name": "John Doe", "score": 85, "grade": "A"},
        {"student_name": "Jane Doe", "score": 90, "grade": "A"},
        {"student_name": "John Doe", "score": 70, "grade": "B"},
        {"student_name": "Jane Doe", "score": 90, "grade": "A"},
        {"student_name": "John Doe", "score": 60, "grade": "C"}
    ]
    
    student_name = "John Doe"
    results = search_feedback_by_name(feedback_data, student_name)
    
    print(f"Feedback for {student_name}:")
    for entry in results:
        print(f"Score: {entry['score']}, Grade: {entry['grade']}")
