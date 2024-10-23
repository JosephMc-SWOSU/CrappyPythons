def getstringfromuser():
    return input("Enter a string: ")

def isstringinteger(inputstring):
    return inputstring.isdigit()

if __name__ == "__main__":
    userstring = getstringfromuser()
    if isstringinteger(userstring):
        print("The string you entered is an integer.")
    else:
        print("The string you entered is not an integer.")