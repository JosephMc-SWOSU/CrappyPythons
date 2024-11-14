class Car:
    def __init__(self, model_year: int, purchase_price: int):
        self.model_year = model_year
        self.purchase_price = purchase_price

    def calculate_current_value(self, current_year: int) -> int:
        # Assuming a depreciation rate of 15% per year
        depreciation_rate = 0.15
        age = current_year - self.model_year
        current_value = self.purchase_price * ((1 - depreciation_rate) ** age)
        return int(current_value)

    def print_info(self, current_year: int):
        current_value = self.calculate_current_value(current_year)
        print("Car's information:")
        print(f"  Model year: {self.model_year}")
        print(f"  Purchase price: ${self.purchase_price}")
        print(f"  Current value: ${current_value}")

if __name__ == "__main__":
    model_year = int(input("Please enter the car's model year: "))
    purchase_price = int(input("Please enter the car's purchase price: "))
    current_year = int(input("Please enter the current year: "))

    my_car = Car(model_year, purchase_price)
    my_car.print_info(current_year)