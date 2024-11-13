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
        self.total_distance = 500  # Total distance to travel across Mars

    def setup(self):
        print("Welcome to the Mars Road Trip!")
        name = input("Enter your name: ")
        vehicle = input("Choose your vehicle (Rover/Buggy/Ect.): ")
        self.player = Player(name, vehicle)
        print(f"Welcome, {self.player.name}! You will be traveling across Mars in your {self.player.vehicle}.")

    def random_event(self):
        events = [
            "You found a food supply! (+20 food)",
            "You encountered a sandstorm! (-10 health)",
            "You found a fuel depot! (+20 fuel)",
            "You hit a rough patch of terrain! (-10 fuel)",
            "You found a medical kit! (+20 health)",
            "You encounter a Martian! (Choose wisely)",
            "You ran over a martian nail and got a flat tire! (-10 fuel)",
            "There was a massive solar flare! (-10 health)",
            "You discovered a Martian settlement! (Choose wisely)"
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
        elif "flat tire" in event:
            self.player.fuel -= 10
        elif "solar flare" in event:
            self.player.health -= 10
        elif "Martian" in event:
            self.martian_settlement()

    def martian_settlement(self):
        print("You have discovered a Martian settlement!")
        print("The Martians offer you a gift.")
        options = [
            ("A small can of martian food", '1'),
            ("A half jug of fuel", '2'),
            ("A Martian artifact", '3')
        ]
        for i, (option, _) in enumerate(options):
            print(f"{i + 1}. {option}")
        while True:
            choice = input("Choose your gift (1/2/3): ").strip()
            if choice in ['1', '2', '3']:
                break
            print("Invalid choice. Please enter 1, 2, or 3.")
        if choice == '1':
            print("You received a small can of martian food! (+20 food)")
            self.player.food += 20
        elif choice == '2':
            print("You received a half jug of fuel! (+20 fuel)")
            self.player.fuel += 20
        elif choice == '3':
            print("You received a Martian artifact! (+20 health)")
            self.player.health += 20

        
        # elif "Martian" in event:
        #     self.martian_encounter()

        # def martian_encounter(self):
        #     print("A Martian approaches you and asks a riddle.")
        #     print("What has keys but can't open locks?")
        #     options = [
        #         ("A piano", '1'),
        #         ("A map", '2'),  
        #         ("A car", '3')
        #     ]
        #     random.shuffle(options)
        #     for i, (option, number) in enumerate(options):
        #         print(f"{i + 1}. {option}")
        #     while True:
        #         choice = input("Choose the correct answer (1/2/3): ").strip()
        #         if choice in ['1', '2', '3']:
        #             break
        #         else:
        #             print("Invalid choice. Please enter 1, 2, or 3.")
        #     correct_answer = next(number for option, number in options if option == "A piano")
        #     if choice == correct_answer:
        #         print("Correct! The Martian is pleased and gives you a gift. (+20 health)")
        #         self.player.health += 20
        #     else:
        #         print("Wrong! The Martian is displeased and curses you. (-20 health)")
        #         self.player.health -= 20

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