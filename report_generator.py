def export_feedback_to_txt(feedback_data, filename="feedback_report.txt"):
    """
    Exports feedback data to a .txt file.

    Parameters:
    - feedback_data: List of dictionaries containing feedback (e.g., [{"score": 85, "grade": "A"}]).
    - filename: Name of the output .txt file (default is 'feedback_report.txt').

    Returns:
    - None
    """
    with open(filename, "w") as file:
        file.write("Feedback Report\n")
        file.write("================\n")
        for entry in feedback_data:
            file.write(f"Score: {entry['score']}, Grade: {entry['grade']}\n")
    print(f"Feedback successfully exported to {filename}")
