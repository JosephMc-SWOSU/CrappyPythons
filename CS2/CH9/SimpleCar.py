
class SimpleCar:
    def __init__(self):
        self.miles = 0

    def drive(self, dist):
        self.miles = self.miles + dist
       
    def reverse(self, dist):
        self.miles = self.miles - dist
       
    def get_odometer(self):
        return self.miles
   
    def honk_horn(self):
        print('beep beep')
       
    def report(self):
        print(f'Car has driven: {self.miles} miles')
       
if __name__ == "__main__":
    forwardmiles = int(input("Enter the number of miles to drive forward: "))
    reversemiles = int(input("Enter the number of miles to drive in reverse: "))

    # TODO: Create SimpleCar object
    car = SimpleCar()
    # TODO: Drive input number of miles forward
    car.drive(forwardmiles)
    # TODO: Honk the horn
    car.honk_horn()
    # TODO: Report car status
    car.report()
    # TODO: Drive input number of miles in reverse
    car.reverse(reversemiles)
    # TODO: Honk the horn
    car.honk_horn()
    # TODO: Report car status
    car.report()
