class Pet:
    def __init__(self, name="", age=0, pet_type=""):
        print("Pet __init__ called")
        self.name = name
        self.age = age
        self.pet_type = pet_type

    def set_name(self, name):
        """Set the pet's name."""
        self.name = name

    def get_name(self):
        """Get the pet's name."""
        return self.name

    def set_age(self, age):
        """Set the pet's age."""
        self.age = age

    def get_age(self):
        """Get the pet's age."""
        return self.age

    def set_pet_type(self, pet_type):
        """Set the pet's type."""
        self.pet_type = pet_type

    def get_pet_type(self):
        """Get the pet's type."""
        return self.pet_type

    def display_info(self):
        """Display the pet's information."""
        return f"Name: {self.name}, Age: {self.age}, Type: {self.pet_type}"

if __name__ == "__main__":
    mike = Pet()
    mike.set_name("Mike")
    mike.set_age(13)
    mike.set_pet_type("Cat")
    print(mike.display_info())