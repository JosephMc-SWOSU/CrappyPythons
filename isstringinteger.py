def isstringinteger(inputstring):
    return inputstring.isdigit()
#how long is the string
def stringlength(inputstring):
    return len(inputstring)
#check if the integer is prime
def isoddoreven(number):
    if number % 2 == 0:
        return "is even"
    else:
        return "is odd"

if __name__ == "__main__":
    userstring = input("Please enter a string: ")
    stringlength = stringlength(userstring)
    oddoreven = isoddoreven(stringlength)
    if isstringinteger(userstring):
        print(f"{userstring} is an integer that is {stringlength} characters long and {oddoreven}.")
    else:
        print(f"{userstring} is not an integer.")