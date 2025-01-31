def find_two_smallest(numbers):
    """Finds and returns the two smallest integers in the list."""
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two integers.")
    
    # Sort the list and return the first two elements
    sorted_numbers = sorted(numbers)
    return sorted_numbers[0], sorted_numbers[1]

if __name__ == "__main__":
    # Read the input list of integers
    input_numbers = list(map(int, input("Enter a list of integers: ").split()))
    
    # Find the two smallest integers
    smallest1, smallest2 = find_two_smallest(input_numbers)
    
    # Output the result
    print(f"{smallest1} and {smallest2}")