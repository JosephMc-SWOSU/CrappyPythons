def get_string_from_user():
    """Prompt the user to enter a string."""
    return input("Please enter a string to check whether it is an integer: ")

def is_string_integer(input_string):
    """Check if the given string is an integer."""
    return input_string.isdigit()

def reverse_string(input_string):
    """Return the reversed version of the string."""
    return input_string[::-1]

def to_uppercase(input_string):
    """Convert the string to uppercase."""
    return input_string.upper()

def to_lowercase(input_string):
    """Convert the string to lowercase."""
    return input_string.lower()

def capitalize_words(input_string):
    """Capitalize the first letter of each word in the string."""
    return input_string.title()

def replace_spaces_with_underscores(input_string):
    """Replace all spaces in the string with underscores."""
    return input_string.replace(' ', '_')

def is_palindrome(input_string):
    """Check if the string is a palindrome."""
    return input_string == input_string[::-1]

def display_menu():
    """Display the menu options to the user."""
    print("Choose an option to format the string:")
    print("1. Reverse the string")
    print("2. Convert to uppercase")
    print("3. Convert to lowercase")
    print("4. Capitalize each word")
    print("5. Replace spaces with underscores")
    print("6. Check if the string is a palindrome")
    print("7. Exit")

if __name__ == "__main__":
    user_string = input("Please enter a string: ")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            print(f"Reversed string: {reverse_string(user_string)}")
        elif choice == '2':
            print(f"Uppercase string: {to_uppercase(user_string)}")
        elif choice == '3':
            print(f"Lowercase string: {to_lowercase(user_string)}")
        elif choice == '4':
            print(f"Capitalized string: {capitalize_words(user_string)}")
        elif choice == '5':
            print(f"Underscored string: {replace_spaces_with_underscores(user_string)}")
        elif choice == '6':
            print(f"Is the string a palindrome? {'Yes' if is_palindrome(user_string) else 'No'}")
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")