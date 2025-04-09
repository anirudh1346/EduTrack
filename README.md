# EduTrack
# EduTrack Student Feedback Manager
**Version:** 1.0.0
**Description:** Providing tools for collecting student feedback and calculating average scores.

**Features:**
- `feedback_entry.py`: Allows for the entry of student feedback .
- `score_calculator.py`: Computes the average score from a list of scores provided in the script.

**Usage:**
- **Collecting Feedback**
- **Calculating Average Score**
- **Testing**
- **Continuous Integration**
**Version Control:**
- This project uses Git for version control. 

**Version:** 1.0.1
**Description:** Creating a new branch for summarizing the feedback.
**Features:**
-`feedback_summary.py`: Summarizes feedback with top scores and grade-wise count
**Usage:**
- **Summarizing feedback**
- **creating branch**
- **Continuous Integration**
**Version Control:**

**Version:** 1.1.0
<<<<<<< feature/summary
**Description:** Export feedback to .txt file
**Features:**
Added functionality to export feedback data into `.txt` files using `report_generator.py`.
**Usage:**
**To export feedback data into a text file:**

from report_generator import export_feedback_to_txt

feedback_data = [
{"score": 85, "grade": "A"},
{"score": 90, "grade": "A"},
{"score": 70, "grade": "B"},
{"score": 90, "grade": "A"},
{"score": 60, "grade": "C"}
]
export_feedback_to_txt(feedback_data)

This will generate a file named `feedback_report.txt` containing the feedback report.
=======
**Description:** Adding functionality to export feedback to a text file.
**Features:**
- `export_feedback.py`: Exports feedback data to a text file.
**Usage:**
- **Exporting Feedback**
- **Creating GitHub Issue and Milestone**
- **Linking Issue to Milestone**
- **Documenting the Change**
**Version Control:**
- Created a new GitHub Issue titled "Export Feedback Functionality".
- Created a new GitHub Milestone titled "v1.1 Release".
- Linked the "Export Feedback Functionality" issue to the "v1.1 Release" Milestone.
- Documented the addition of the export functionality in relevant documentation.







>>>>>>> main
