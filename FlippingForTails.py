import random

class GVCoin:
    def __init__(self, seed):
        random.seed(seed)
        self.is_heads = True
        self.heads = 0
        self.flips = 0

    def flip(self):
        self.is_heads = random.randint(0, 1)
        self.flips += 1
        if self.is_heads == 1:
            self.heads += 1

    def get_is_heads(self):
        return self.is_heads

    def num_flips(self):
        return self.flips

    def num_heads(self):
        return self.heads

    def num_tails(self):
        return self.flips - self.heads

    def set_to_heads(self, h):
        self.is_heads = h

def flip_for_tails(gv_coin, goal):
    tails = 0
    while tails < goal:
        gv_coin.flip()
        if not gv_coin.get_is_heads():
            tails += 1
    return gv_coin.num_flips()

if __name__ == "__main__":
    gv_coin = GVCoin(random.randint(1, 100))
    num_tails = int(input("Enter the number of tails you want: "))
    total = flip_for_tails(gv_coin, num_tails)
    print(f'Total number of flips for {num_tails} tails: { total }')