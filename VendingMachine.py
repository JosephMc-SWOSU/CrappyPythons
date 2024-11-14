class VendingMachine:
    def __init__(self, initial_inventory=20):
        self.inventory = initial_inventory

    def purchase(self, num_drinks: int):
        if num_drinks <= self.inventory:
            self.inventory -= num_drinks
        else:
            print("Not enough inventory to complete the purchase.")

    def restock(self, num_bottles: int):
        self.inventory += num_bottles

    def report_inventory(self):
        print(f"Inventory: {self.inventory} bottles")

if __name__ == "__main__":
    # Read input values
    initial_inventory = int(input("Please enter the initial inventory: "))
    num_drinks = int(input("Please enter the number of drinks to purchase: "))
    num_bottles = int(input("Please enter the number of bottles to restock: "))

    # Create VendingMachine object with initial inventory
    vending_machine = VendingMachine(initial_inventory)

    # Perform operations
    vending_machine.purchase(num_drinks)
    vending_machine.restock(num_bottles)
    vending_machine.report_inventory()