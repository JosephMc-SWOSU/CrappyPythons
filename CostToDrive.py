def GreetUser():
    # Prints a welcome message and explains the purpose of the program
    print("Welcome to the Cost to Drive Calculator!\n")
    print("This program will calculate the cost of a trip based on the number of miles driven,")
    print("the miles per gallon of the vehicle, and the price of gas per gallon.\n")
    print("Please enter the requested information below:\n")

def GetValidFloatInput(prompt, validation_fn):
    # Repeatedly prompts the user for input until a valid float that meets the validation criteria is entered
    while True:
        try:
            # Convert the user input to a float
            value = float(input(prompt))
            # Check if the input meets the validation criteria
            if validation_fn(value):
                return value
            else:
                print("Invalid input. Please enter a positive number.")
        except ValueError:
            # Handle the case where the input cannot be converted to a float
            print("Invalid input. Please enter a valid number.")

def GetUserTripMiles():
    # Prompts the user to enter the number of miles they will be driving
    return GetValidFloatInput("Please enter the number of miles you will be driving: ", lambda x: x > 0) #Input cannot be negative
    
def GetUserMPG():
    # Prompts the user to enter the miles per gallon of their vehicle
    return GetValidFloatInput("Please enter the miles per gallon of your vehicle: ", lambda x: x > 0) #Input cannot be negative

def GetUserGasPrice():
    # Prompts the user to enter the price of gas per gallon
    return GetValidFloatInput("Please enter the price of gas per gallon: ", lambda x: x > 0) #Input cannot be negative

def CalculateCostToDrive(miles, mpg, price):
    # Calculates the cost to drive based on miles, miles per gallon, and gas price
    return miles / mpg * price

def GoodbyeUser():
    # Prints a goodbye message
    print("Thank you for using the Cost to Drive Calculator. Goodbye!")

if __name__ == "__main__":
    # Main program execution
    GreetUser()  # Greet the user
    miles = GetUserTripMiles()  # Get the number of miles to be driven
    mpg = GetUserMPG()  # Get the miles per gallon of the vehicle
    price = GetUserGasPrice()  # Get the price of gas per gallon
    cost = CalculateCostToDrive(miles, mpg, price)  # Calculate the cost to drive
    print(f"The cost to drive {miles} miles is ${cost:.2f}.")  # Print the calculated cost
    GoodbyeUser()  # Say goodbye to the user