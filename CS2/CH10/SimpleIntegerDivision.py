# Compute the quotient
def divide(user_num, div_num):
    try:
        quotient = user_num // div_num #quotient is the result of dividing the dividend by the divisor
        return quotient
    except ZeroDivisionError: #if divisor is 0, print an error message
        print("Cannot divide by zero")  
        return None
    except ValueError: #if dividend or divisor is not an integer, print an error message
        return None

if __name__ == "__main__": 
    user_num = int(input("Enter the dividend: ")) #Get the dividend
    div_num = int(input("Enter the divisor: ")) #Get the divisor   
    quotient = divide(user_num, div_num)
    if quotient is not None:
        print(f"{user_num} divided by {div_num} is {quotient}.")
