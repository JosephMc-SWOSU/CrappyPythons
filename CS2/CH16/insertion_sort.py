def read_nums():
    """Read numbers from input and return them as a list."""
    return [int(num) for num in input("Enter unsorted numbers separated by spaces: ").split()]


def print_nums(nums):
    """Print numbers separated by spaces."""
    print(' '.join(map(str, nums)), end='')


def swap(nums, n, m):
    """Swap elements at indices n and m in the list."""
    nums[n], nums[m] = nums[m], nums[n]


def insertion_sort(numbers):
    """Sort the list using insertion sort and count comparisons and swaps."""
    global comparisons, swaps
    comparisons = 0
    swaps = 0

    for i in range(1, len(numbers)):
        j = i
        while j > 0:
            comparisons += 1
            if numbers[j] < numbers[j - 1]:
                swap(numbers, j, j - 1)
                swaps += 1
                j -= 1
            else:
                break

        # Print the list after each iteration of the outer loop
        print_nums(numbers)
        print()


if __name__ == '__main__':
    # Read numbers into a list
    numbers = read_nums()

    # Print the unsorted list
    print_nums(numbers)
    print('\n')

    # Sort the list
    insertion_sort(numbers)
    print()

    # Print the number of comparisons and swaps
    print(f"comparisons: {comparisons}")
    print(f"swaps: {swaps}")
