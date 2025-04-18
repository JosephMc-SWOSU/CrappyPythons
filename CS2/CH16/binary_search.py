# Global variables to track recursions and comparisons
recursions = 0
comparisons = 0


def binary_search(nums, target, lower, upper):
    """Perform binary search recursively."""
    global recursions, comparisons
    recursions += 1

    if lower > upper:
        return -1  # Target not found

    mid = (lower + upper) // 2
    comparisons += 1
    if nums[mid] == target:
        return mid  # Target found

    comparisons += 1
    if nums[mid] < target:
        return binary_search(nums, target, mid + 1, upper)  # Search right half
    else:
        return binary_search(nums, target, lower, mid - 1)  # Search left half


if __name__ == '__main__':
    # Input a list of numbers
    nums = [int(n) for n in input("Enter numbers separated by spaces: ").split()]

    # Input the target value
    target = int(input("Enter the target value: "))

    # Perform binary search
    index = binary_search(nums, target, 0, len(nums) - 1)

    # Output the result
    print(f'index: {index}, recursions: {recursions}, comparisons: {comparisons}')
