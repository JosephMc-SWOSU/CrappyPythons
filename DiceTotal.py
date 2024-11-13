import random

class GVDie:
    def __init__(self, seed):
        random.seed(seed)
    
    def roll(self):
        return random.randint(1, 6)

def roll_specific_times(die, num_rolls):
    total_sum = 0
    
    for _ in range(num_rolls):
        total_sum += die.roll()
    
    return total_sum

def main():
    seed_value = random.randint(12, 18)
    num_rolls = int(input("Enter the number of rolls: "))
    die = GVDie(seed_value)
    total = roll_specific_times(die, num_rolls)
    print(f"{num_rolls} rolls return a total of {total}.")

if __name__ == "__main__":
    main()