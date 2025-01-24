import json
import random

def load_questions(filename):
    """Load questions from a JSON file."""
    try:
        with open(filename, 'r') as file:
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {filename} is not a valid JSON file.")
        return []

def save_score(filename, score):
    """Save the user's score to a file."""
    try:
        with open(filename, 'a') as file:
            file.write(f"Score: {score}\n")
    except IOError:
        print(f"Error: Could not write to file {filename}.")

def ask_question(question):
    """Ask a single question and return True if the answer is correct, False otherwise."""
    print(question['question'])
    for option_index, option in enumerate(question['options'], 1):
        print(f"{option_index}. {option}")
    while True:
        try:
            answer = int(input("Your answer (1-4): "))
            if 1 <= answer <= 4:
                if answer == question['answer']:
                    print("Correct!")
                    return True
                else:
                    print(f"Incorrect! The correct answer was {question['answer']}.")
                    return False
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def main():
    """Main function to run the quiz game."""
    questions = load_questions('questions.json')
    if not questions:
        return

    # Select 10 random questions from the list
    selected_questions = random.sample(questions, min(10, len(questions)))

    score = 0
    for question in selected_questions:
        if ask_question(question):
            score += 1

    print(f"Your final score: {score}/{len(selected_questions)}")
    save_score('scores.txt', score)

if __name__ == "__main__":
    main()