def calculate_fibonacci(n):
    # Calculates the nth Fibonacci number
    if n == 0:
        return 0  # Base case: the 0th Fibonacci number is 0
    elif n == 1:
        return 1  # Base case: the 1st Fibonacci number is 1

    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    # Iterate from 2 to n to calculate the nth Fibonacci number
    for _ in range(2, n + 1):
        a, b = b, a + b  # Update a and b to the next Fibonacci numbers
    return b  # Return the nth Fibonacci number

def prompt_for_numbers():
    # Prompts the user to enter numbers separated by spaces and returns them as a list of integers
    while True:
        input_str = input("Please enter numbers separated by spaces to return the nth values in the sequence: ")
        try:
            # Split the input string by spaces and convert each part to an integer
            numbers = [int(x.strip()) for x in input_str.split()]
            return numbers  # Return the list of integers
        except ValueError:
            # Handle the case where the input cannot be converted to integers
            print("Invalid input. Please enter only numbers separated by spaces.")

if __name__ == "__main__":
    # Main program execution
    numbers = prompt_for_numbers()  # Prompt the user for numbers
    
    # Calculate and print the Fibonacci number for each input number
    for n in numbers:
        print(f"The {n}th Fibonacci number is: {calculate_fibonacci(n)}")