import random

class GVCoin:
    def __init__(self, seed):
        random.seed(seed)
    
    def flip(self):
        return 'heads' if random.randint(0, 1) == 0 else 'tails'

def consecutive_heads(coin, desired_heads):
    total_flips = 0
    current_streak = 0
    
    while current_streak < desired_heads:
        if coin.flip() == 'heads':
            current_streak += 1
        else:
            current_streak = 0
        total_flips += 1
    
    return total_flips

def main():
    seed_value = random.randint(3,6)
    desired_heads = int(input("Enter the number of consecutive heads you want: "))
    coin = GVCoin(seed_value)
    flips = consecutive_heads(coin, desired_heads)
    print(f"Total number of flips for {desired_heads} consecutive heads: {flips}")

if __name__ == "__main__":
    main()