def feet_to_steps(user_feet: float) -> int:
    """Converts feet walked to steps walked."""
    steps_per_foot = 1 / 2.5  # 1 step is 2.5 feet
    return int(user_feet * steps_per_foot)

if __name__ == "__main__":
    print("Welcome to the Step Counter Program!")
    print("This program will help you convert the number of feet you walked into steps.")
    
    # Read the number of feet walked as input
    user_feet = float(input("Please enter the number of feet you walked: "))
    
    # Call the feet_to_steps function with the input as an argument
    steps_walked = feet_to_steps(user_feet)
    
    # Output the number of steps as an integer
    print(f"You have walked approximately {steps_walked} steps.")
    print("Have a great day!")