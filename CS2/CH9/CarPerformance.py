class Car:
    def __init__(self, make, model, year, engine_type, displacement):
        # Initialize the car with make, model, year, engine type, and displacement
        self.make = make
        self.model = model
        self.year = year
        self.engine_type = engine_type
        self.displacement = displacement
        self.performance_metrics = None

    def add_performance_metrics(self, zero_to_sixty, quarter_mile, top_speed, fuel_efficiency):
        # Add performance metrics to the car
        self.performance_metrics = PerformanceMetric(zero_to_sixty, quarter_mile, top_speed, fuel_efficiency)

    def __str__(self):
        # Return a string representation of the car
        return f"{self.year} {self.make} {self.model} ({self.engine_type})"

class PerformanceMetric:
    def __init__(self, zero_to_sixty, quarter_mile, top_speed, fuel_efficiency):
        # Initialize the performance metrics with 0-60 mph time, quarter-mile time, top speed, and fuel efficiency
        self.zero_to_sixty = zero_to_sixty
        self.quarter_mile = quarter_mile
        self.top_speed = top_speed
        self.fuel_efficiency = fuel_efficiency

    def __str__(self):
        # Return a string representation of the performance metrics
        return (f"0-60 mph: {self.zero_to_sixty} seconds, "
                f"Quarter-mile: {self.quarter_mile} seconds, "
                f"Top speed: {self.top_speed} mph, "
                f"Fuel efficiency: {self.fuel_efficiency} mpg")

class ComparisonReport:
    @staticmethod
    def compare_cars(car1, car2):
        # Check if both cars have performance metrics assigned
        if car1.performance_metrics is None or car2.performance_metrics is None:
            print("One or both cars do not have performance metrics assigned.")
            return
        
        # Print the comparison results
        print(f"\nComparison Results: {car1} vs {car2}")

        # Compare 0-60 mph
        value1 = car1.performance_metrics.zero_to_sixty
        value2 = car2.performance_metrics.zero_to_sixty
        print(f"0-60 mph: {value1} seconds vs {value2} seconds (lower is better)")

        # Compare Quarter-mile
        value1 = car1.performance_metrics.quarter_mile
        value2 = car2.performance_metrics.quarter_mile
        print(f"Quarter-mile: {value1} seconds vs {value2} seconds (lower is better)")

        # Compare Top speed
        value1 = car1.performance_metrics.top_speed
        value2 = car2.performance_metrics.top_speed
        print(f"Top speed: {value1} mph vs {value2} mph (higher is better)")

        # Compare Fuel efficiency
        value1 = car1.performance_metrics.fuel_efficiency
        value2 = car2.performance_metrics.fuel_efficiency
        print(f"Fuel efficiency: {value1} mpg vs {value2} mpg (higher is better)")

        # Compare Displacement
        value1 = car1.displacement
        value2 = car2.displacement
        print(f"Displacement: {value1}L vs {value2}L")

if __name__ == "__main__":
    # Create a list of cars
    cars = [
        Car("Nissan", "Skyline GT-R", 1999, "I6", 2.6),
        Car("Toyota", "Supra", 1998, "I6", 3.0),
        Car("Mazda", "RX-7", 1995, "R2", 1.3),
        Car("Honda", "NSX", 1995, "V6", 3.0),
        Car("Mitsubishi", "Lancer Evolution VI", 1999, "I4", 2.0),
        Car("Mazda", "Miata", 1990, "I4", 1.6)
    ]

    # Add performance metrics to the cars
    cars[0].add_performance_metrics(4.9, 13.1, 156, 17)
    cars[1].add_performance_metrics(4.6, 13.3, 155, 19)
    cars[2].add_performance_metrics(5.3, 13.5, 155, 19)
    cars[3].add_performance_metrics(5.7, 13.9, 168, 20)
    cars[4].add_performance_metrics(4.4, 13.1, 157, 18)
    cars[5].add_performance_metrics(8.6, 16.4, 116, 25)

    # Display available cars
    print("Available cars:")
    for i, car in enumerate(cars):
        print(f"{i + 1}. {car}")

    # Prompt the user to select cars to compare
    car1_index = int(input("Enter the number of the first car to compare: ")) - 1
    car2_index = int(input("Enter the number of the second car to compare: ")) - 1

    # Generate a comparison report
    ComparisonReport.compare_cars(cars[car1_index], cars[car2_index])