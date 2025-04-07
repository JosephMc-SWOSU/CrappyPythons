class Pet:
    def __init__(self):
        self.name = ''
        self.age = 0

    def print_info(self):
        print('Pet Information:')
        print(f'   Name: {self.name}')
        print(f'   Age: {self.age}')


class Cat(Pet):
    def __init__(self):
        super().__init__()
        self.breed = ''

    def print_info_cat(self):
        print('Cat Information:')
        print(f'   Name: {self.name}')
        print(f'   Age: {self.age}')
        print(f'   Breed: {self.breed}')


if __name__ == "__main__":
    my_pet = Pet()
    my_cat = Cat()

    pet_name = input("Enter pet name: ")
    pet_age = int(input("Enter pet age: "))
    cat_name = input("Enter cat name: ")
    cat_age = int(input("Enter cat age: "))
    cat_breed = input("Enter cat breed: ")

    my_pet.name = pet_name
    my_pet.age = pet_age
    my_pet.print_info()

    my_cat.name = cat_name
    my_cat.age = cat_age
    my_cat.breed = cat_breed
    my_cat.print_info_cat()
