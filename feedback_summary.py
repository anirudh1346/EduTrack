def summarize_feedback(feedback_list):
    scores = [f["score"] for f in feedback_list]
    top_score = max(scores)
    grade_counts = {}

    for feedback in feedback_list:
        grade = feedback["grade"]
        grade_counts[grade] = grade_counts.get(grade, 0) + 1

    return {
        "top_score": top_score,
        "grade_counts": grade_counts
    }
