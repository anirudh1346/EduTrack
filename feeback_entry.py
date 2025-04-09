import json
from datetime import datetime

def collect_feedback():
    print("Please provide your feedback:")
    
    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")
    rating = input("Rate your experience (1-5): ")
    
    feedback_data = {
        "name": name,
        "feedback": feedback,
        "rating": rating,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    return feedback_data

def save_feedback(feedback_data, filename="feedback.json"):
    try:
        with open(filename, "r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []
    
    existing_data.append(feedback_data)
    
    with open(filename, "w") as file:
        json.dump(existing_data, file, indent=4)
    
    print("Feedback saved successfully.")

def main():
    feedback_data = collect_feedback()
    save_feedback(feedback_data)

if __name__ == "__main__":
    main()
