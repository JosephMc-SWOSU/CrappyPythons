import random

options = ["rock", "paper", "scissors", "lizard", "spock"]

rules = {
    "rock": {"scissors": "Rock crushes scissors", "lizard": "Rock crushes lizard"},
    "paper": {"rock": "Paper covers rock", "spock": "Paper disproves Spock"},
    "scissors": {"paper": "Scissors cuts paper", "lizard": "Scissors decapitates lizard"},
    "lizard": {"spock": "Lizard poisons Spock", "paper": "Lizard eats paper"},
    "spock": {"rock": "Spock vaporizes rock", "scissors": "Spock smashes scissors"}
}

def random_choice(options):
    return random.choice(options)

def user_choice(options):
    while True:
        choice = input("Enter rock, paper, scissors, lizard, or spock: ").lower()
        if choice in options:
            return choice
        else:
            print("Invalid choice. Please try again.")

def main(rounds):
    user_score = 0
    computer_score = 0
    round_counter = 0

    while round_counter < rounds:
        user = user_choice(options)
        computer = random_choice(options)
        print(f"User choice: {user}")
        print(f"Computer choice: {computer}")

        if user == computer:
            print("It's a tie! This round does not count.\n")
            continue
        elif computer in rules[user]:
            print(f"You win! {rules[user][computer]}")
            user_score += 1
        else:
            print(f"You lose! {rules[computer][user]}")
            computer_score += 1

        round_counter += 1
        print(f"Score: User {user_score} - Computer {computer_score}\n")

    print("Final Scores:")
    print(f"User: {user_score}")
    print(f"Computer: {computer_score}")

if __name__ == "__main__":
    rounds = int(input("Enter the number of rounds: "))
    main(rounds)



