class ScoreCalculator:
    def __init__(self):
        self.scores = {}

    def add_score(self, subject, score):
        """Add a score for a subject."""
        self.scores[subject] = score

    def remove_score(self, subject):
        """Remove a score for a subject."""
        if subject in self.scores:
            del self.scores[subject]
        else:
            print(f"No score found for {subject}.")

    def calculate_total_score(self):
        """Calculate the total score."""
        return sum(self.scores.values())

    def calculate_average_score(self):
        """Calculate the average score."""
        if not self.scores:
            return 0
        return self.calculate_total_score() / len(self.scores)

    def display_scores(self):
        """Display all scores."""
        for subject, score in self.scores.items():
            print(f"{subject}: {score}")

def main():
    calculator = ScoreCalculator()

    while True:
        print("\nScore Calculator Menu:")
        print("1. Add Score")
        print("2. Remove Score")
        print("3. Calculate Total Score")
        print("4. Calculate Average Score")
        print("5. Display Scores")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            subject = input("Enter subject name: ")
            score = float(input("Enter score: "))
            calculator.add_score(subject, score)
        elif choice == "2":
            subject = input("Enter subject name: ")
            calculator.remove_score(subject)
        elif choice == "3":
            print(f"Total Score: {calculator.calculate_total_score()}")
        elif choice == "4":
            print(f"Average Score: {calculator.calculate_average_score()}")
        elif choice == "5":
            calculator.display_scores()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
