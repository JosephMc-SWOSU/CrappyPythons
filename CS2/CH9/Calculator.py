
class Calculator:

    def __init__(self):
        self.value = 0

    def get_value(self):
        return self.value

    def addition(self, num):
        self.value += num

    def subtraction(self, num):
        self.value -= num

    def multiplication(self, num):
        self.value *= num

    def division(self, num):
        self.value /= num

    def clear(self):
        self.value = 0
    
    

if __name__ == "__main__":

    def get_float_input(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a number.")

    calc = Calculator()
    num1 = get_float_input("Enter the first number: ")
    num2 = get_float_input("Enter the second number: ")

    # 1. The initial value
    print("Initial value:")
    print(f'{calc.get_value():.1f}')

    # 2. The The value after adding num1
    print("Adding num1:")
    calc.addition(num1)
    print(f'{calc.get_value():.1f}')

    # 3. The value after multiplying by 3
    print("Multiplying by 3:")
    calc.multiplication(3)
    print(f'{calc.get_value():.1f}')

    # 4. The value after subtracting num2
    print("Subtracting num2:")
    calc.subtraction(num2)
    print(f'{calc.get_value():.1f}')

    # 5. The value after dividing by 2
    print("Dividing by 2:")
    calc.division(2)
    print(f'{calc.get_value():.1f}')

    # 6. The value after calling the clear() method
    print("Clearing the value:")
    calc.clear()
    print(f'{calc.get_value():.1f}')
