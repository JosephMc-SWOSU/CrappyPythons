def int_to_reverse_binary(integer_value: int) -> str:
    """Converts an integer to a binary string in reverse order."""
    binary_str = ""
    while integer_value > 0:
        binary_str += str(integer_value % 2)
        integer_value = integer_value // 2
    return binary_str

def string_reverse(input_string: str) -> str:
    """Reverses the input string."""
    return input_string[::-1]

if __name__ == "__main__":
    print("Welcome to the Binary Converter Program!")
    
    # Read the input integer
    integer_value = int(input("Please enter a positive integer: "))
    
    # Convert the integer to a reverse binary string
    reverse_binary_str = int_to_reverse_binary(integer_value)
    
    # Reverse the binary string to get the correct binary representation
    binary_str = string_reverse(reverse_binary_str)
    
    # Output the binary string
    print(f"The binary representation of {integer_value} is: {binary_str}")
    print("Have a great day!")