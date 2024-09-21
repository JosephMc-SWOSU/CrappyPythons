# Function to get a valid number input from the user
def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Get four valid numbers from the user
number1 = get_valid_number("Please enter the first number: ")
number2 = get_valid_number("Please enter the second number: ")
number3 = get_valid_number("Please enter the third number: ")
number4 = get_valid_number("Please enter the fourth number: ")

# Function to check if a number is odd
def is_odd(number):
    return number % 2 != 0

# Check if the numbers are odd and print the results
print(f"The first number ({number1}) is {'odd' if is_odd(number1) else 'even'}.")
print(f"The second number ({number2}) is {'odd' if is_odd(number2) else 'even'}.")
print(f"The third number ({number3}) is {'odd' if is_odd(number3) else 'even'}.")
print(f"The fourth number ({number4}) is {'odd' if is_odd(number4) else 'even'}.")