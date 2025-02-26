import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def display_rules():
    print("Rules:")
    print("1. You start with a certain number of credits.")
    print("2. On each turn, you can choose to roll the dice or cash out.")
    print("3. If you roll a 7 or 11, you win one credit.")
    print("4. If you roll a 2, 3, or 12, you lose one credit.")
    print("5. If you roll any other number, that number becomes your goal.")
    print("6. On subsequent rolls, if you roll a 7, you lose one credit.")
    print("7. If you roll your goal number, you win one credit.")
    print("8. The game ends when you run out of credits or choose to cash out.")
    print()

def play_game(seed, credits):
    if seed is not None:
        random.seed(seed)
    rounds = 0
    goal = -1

    while credits > 0:
        choice = input("Enter 'r' to roll the dice or 'c' to cash out: ").strip().lower()
        if choice == 'c':
            break

        dice_total = roll_dice()
        print(f"Dice total: {dice_total}")

        if goal == -1:
            if dice_total in [7, 11]:
                credits += 1
            elif dice_total in [2, 3, 12]:
                credits -= 1
            else:
                goal = dice_total
        else:
            if dice_total == 7:
                credits -= 1
                goal = -1
            elif dice_total == goal:
                credits += 1
                goal = -1

        print(f"Credits: {credits}")
        rounds += 1

    print(f"Rounds: {rounds}")
    print(f"Final credits: {credits}")

def main_menu():
    while True:
        print("Main Menu")
        print("1. Start Game")
        print("2. Display Rules")
        print("3. Exit")
        choice = input("Please enter your choice: ").strip()

        if choice == '1':
            seed_input = input("Please enter the seed (or 'random' for a random seed): ").strip().lower()
            if seed_input == 'random':
                seed = None
            else:
                seed = int(seed_input)
            credits = int(input("Please enter the number of credits: "))
            play_game(seed, credits)
        elif choice == '2':
            display_rules()
        elif choice == '3':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()