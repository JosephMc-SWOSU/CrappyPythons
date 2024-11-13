import random

class GVDie:
    def __init__(self, seed):
        random.seed(seed)
    
    def roll(self):
        return random.randint(1, 6)

def play_game(seed_value, initial_credits):
    die1 = GVDie(seed_value)
    die2 = GVDie(seed_value)
    credits = initial_credits

    while credits > 0:
        input("Press Enter to roll the dice...")
        roll1 = die1.roll()
        roll2 = die2.roll()
        total = roll1 + roll2
        print(f"Rolled: {roll1} + {roll2} = {total}")

        if total == 7:
            print("You win 1 credit!")
            credits += 1
        elif total == 2 or total == 12:
            print("You lose 1 credit!")
            credits -= 1
        else:
            goal = total
            print(f"Set a goal: {goal}")
            while True:
                input("Press Enter to roll the dice...")
                roll1 = die1.roll()
                roll2 = die2.roll()
                total = roll1 + roll2
                print(f"Rolled: {roll1} + {roll2} = {total}")

                if total == goal:
                    print("You win 1 credit!")
                    credits += 1
                    break
                elif total == 7:
                    print("You lose 1 credit!")
                    credits -= 1
                    break

        print(f"Credits: {credits}")
        if credits == 0:
            print("Game over! You have zero credits left.")

def main():
    seed_value = 15
    initial_credits = 10
    play_game(seed_value, initial_credits)

if __name__ == "__main__":
    main()