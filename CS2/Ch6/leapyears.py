def days_in_feb(user_year: int) -> int:
    """Returns the number of days in February for the given year."""
    if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
        return 29
    else:
        return 28

def is_leap_year(user_year: int) -> bool:
    """Returns True if the given year is a leap year, False otherwise."""
    return (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0)

if __name__ == "__main__":
    print("Welcome to the Leap Year Checker Program!")
    
    # Read the input year
    user_year = int(input("Please enter a year: "))
    
    # Determine the number of days in February
    days = days_in_feb(user_year)
    
    # Determine if it is a leap year
    leap_year = is_leap_year(user_year)
    
    # Output the result
    if leap_year:
        print(f"The year {user_year} has {days} days in February, and is a leap year.")
    else:
        print(f"The year {user_year} has {days} days in February, and is not a leap year.")
    
    print("Have a great day!")