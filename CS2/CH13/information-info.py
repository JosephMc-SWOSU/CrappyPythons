class Instrument:
    def __init__(self, name, manufacturer, year_built, cost):
        self.name = name
        self.manufacturer = manufacturer
        self.year_built = year_built
        self.cost = cost

    def print_info(self):
        print('Instrument Information:')
        print(f'   Name: {self.name}')
        print(f'   Manufacturer: {self.manufacturer}')
        print(f'   Year built: {self.year_built}')
        print(f'   Cost: {self.cost}')


class StringInstrument(Instrument):
    def __init__(self, name, manufacturer, year_built, cost, num_strings, num_frets, is_bowed):
        super().__init__(name, manufacturer, year_built, cost)
        self.num_strings = num_strings
        self.num_frets = num_frets
        self.is_bowed = is_bowed


if __name__ == "__main__":
    instrument_name = input("Enter instrument name: ")
    manufacturer_name = input("Enter manufacturer name: ")
    year_built = int(input("Enter year built: "))
    cost = int(input("Enter cost: "))
    string_instrument_name = input("Enter string instrument name: ")
    string_manufacturer = input("Enter string manufacturer name: ")
    string_year_built = int(input("Enter string year built: "))
    string_cost = int(input("Enter string cost: "))
    num_strings = int(input("Enter number of strings: "))
    num_frets = int(input("Enter number of frets: "))
    is_bowed = input("Is the instrument bowed? (True or False)") == 'True'

    my_instrument = Instrument(instrument_name, manufacturer_name, year_built, cost)
    my_string_instrument = StringInstrument(
        string_instrument_name, string_manufacturer, string_year_built,
        string_cost, num_strings, num_frets, is_bowed
    )

    my_instrument.print_info()
    my_string_instrument.print_info()

    print(f'   Number of strings: {my_string_instrument.num_strings}')
    print(f'   Number of frets: {my_string_instrument.num_frets}')
    print(f'   Is bowed: {my_string_instrument.is_bowed}')
