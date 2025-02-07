
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

    car = SimpleCar()
    car.drive(forwardmiles)
    car.honk_horn()
    car.report()
    car.reverse(reversemiles)
    car.honk_horn()
    car.report()
