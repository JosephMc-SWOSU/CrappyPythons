num1 = float(input("Plese enter the first number: "))
num2 = float(input("Plese enter the second number: "))
num3 = float(input("Plese enter the third number: "))
num4 = float(input("PLease enter the fourth number: "))

def average(num1, num2, num3, num4):
    return (num1 + num2 + num3 + num4) / 4

def product(num1, num2, num3, num4):
    return num1 * num2 * num3 * num4
print(f"----------------------------------------------")
print(f"The average of the numbers is: {round(average(num1, num2, num3, num4), 3)}")
print(f"The product of the numbers is: {round(product(num1, num2, num3, num4), 3)}")
print(f"The rounded average of the numbers is: {round(average(num1, num2, num3, num4))}")
print(f"The rounded product of the numbers is: {round(product(num1, num2, num3, num4))}")
print(f"----------------------------------------------")