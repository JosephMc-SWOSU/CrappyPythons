import random

def unique_random_ints(how_many, max_num):
    random_ints = []
    while len(random_ints) < how_many:
        random_num = random.randint(0, max_num)
        if random_num not in random_ints:
            random_ints.append(random_num)
    print(random_ints)

if __name__ == '__main__':
    seed = int(input("Enter a seed for the random number generator: "))
    how_many = int(input("How many random numbers do you want to generate? "))
    max_num = int(input("Enter the maximum number for the random numbers: "))

    random.seed(seed)
    unique_random_ints(how_many, max_num)