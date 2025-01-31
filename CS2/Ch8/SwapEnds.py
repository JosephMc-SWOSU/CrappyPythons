def swap_ends(numbers):
    """Swaps the first and last elements of the list."""
    if len(numbers) > 1:
        numbers[0], numbers[-1] = numbers[-1], numbers[0]
    return numbers

if __name__ == "__main__":
    # Read the input list of integers
    input_numbers = list(map(int, input("Enter a list of integers: ").split()))
    
    # Swap the first and last elements
    swapped_numbers = swap_ends(input_numbers)
    
    # Output the result
    print(" ".join(map(str, swapped_numbers)))