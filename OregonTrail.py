import random

class Player:
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle
        self.health = 100
        self.food = 100
        self.fuel = 100
        self.distance_traveled = 0

    def status(self):
        return f"Health: {self.health}, Food: {self.food}, Fuel: {self.fuel}, Distance Traveled: {self.distance_traveled} km"

class Game:
    def __init__(self):
        self.player = None
        self.total_distance = 1000  # Total distance to travel across Mars

    def setup(self):
        print("Welcome to the Mars Road Trip!")
        name = input("Enter your name: ")
        vehicle = input("Choose your vehicle (Rover/Buggy): ")
        self.player = Player(name, vehicle)
        print(f"Welcome, {self.player.name}! You will be traveling across Mars in your {self.player.vehicle}.")

    def random_event(self):
        events = [
            "You found a food supply! (+20 food)",
            "You encountered a sandstorm! (-10 health)",
            "You found a fuel depot! (+20 fuel)",
            "You hit a rough patch of terrain! (-10 fuel)",
            "You found a medical kit! (+20 health)"
        ]
        event = random.choice(events)
        print(event)
        if "food" in event:
            self.player.food += 20
        elif "sandstorm" in event:
            self.player.health -= 10
        elif "fuel depot" in event:
            self.player.fuel += 20
        elif "rough patch" in event:
            self.player.fuel -= 10
        elif "medical kit" in event:
            self.player.health += 20

    def travel(self):
        if self.player.fuel <= 0:
            print("You have run out of fuel! Game over.")
            return False
        if self.player.food <= 0:
            print("You have run out of food! Game over.")
            return False
        if self.player.health <= 0:
            print("You have succumbed to the harsh conditions of Mars. Game over.")
            return False

        self.player.distance_traveled += 50
        self.player.fuel -= 10
        self.player.food -= 10
        print(f"You traveled 50 km. {self.total_distance - self.player.distance_traveled} km to go.")
        self.random_event()
        print(self.player.status())
        return True

    def play(self):
        self.setup()
        while self.player.distance_traveled < self.total_distance:
            action = input("Do you want to (T)ravel or (Q)uit? ").strip().lower()
            if action == 't':
                if not self.travel():
                    break
            elif action == 'q':
                print("You have quit the game.")
                break
            else:
                print("Invalid action. Please choose 'T' to travel or 'Q' to quit.")
        if self.player.distance_traveled >= self.total_distance:
            print("Congratulations! You have successfully traveled across Mars.")

if __name__ == "__main__":
    game = Game()
    game.play()