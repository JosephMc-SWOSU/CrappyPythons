class Car:
    def __init__(self, model_year, purchase_price):
        self.model_year = model_year
        self.purchase_price = purchase_price
        self.current_value = 0

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        age = current_year - self.model_year
        self.current_value = int(self.purchase_price * ((1 - depreciation_rate) ** age))

    def print_info(self):
        print("Car's information:")
        print(f"  Model year: {self.model_year}")
        print(f"  Purchase price: ${self.purchase_price}")
        print(f"  Current value: ${self.current_value}")

if __name__ == "__main__":
    model_year = int(input("Please enter the model year: "))
    purchase_price = int(input("Please enter the purchase price: "))
    current_year = int(input("Please enter the current year: "))

    my_car = Car(model_year, purchase_price)
    my_car.calc_current_value(current_year)
    my_car.print_info()