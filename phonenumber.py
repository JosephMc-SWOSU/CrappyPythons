# Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
zip_code = input("Enter your zip code: ")

# Function to format phone number
def format_phone_number(number):
    # Convert Number to a String
    number_str = str(number)
    # Obtain the area code
    area_code = number_str[:3]
    # Obtain the Prefix
    prefix = number_str[3:6]
    # Obtain the last four
    line_number = number_str[6:]
    # Format the number
    formatted_number = f"({area_code}) {prefix}-{line_number}"
    return formatted_number

# Loop until a valid 10-digit phone number is entered
while True:
    phone_number = input("Enter a 10-digit phone number: ")
    if len(phone_number) == 10 and phone_number.isdigit():
        formatted_number = format_phone_number(phone_number)
        break
    else:
        print("Invalid input. Please enter a 10-digit phone number.")

# Display user information
print("\n--- User Information ---")
print(f"Name: {first_name} {last_name}")
print(f"Zip Code: {zip_code}")
print(f"Formatted Phone Number: {formatted_number}")
print("------------------------")
