import random

# Define a dictionary with multiple options for each letter
leet_dict = {
    "a": ["4", "@", "Д"],
    "b:": ["8", "ß", "13"],
    "e": ["3", "€", "ë"],
    "f": ["|=", "ƒ", "ph"],
    "g": ["6", "&", "9"],
    "h": ["#", "4",],
    "i": ["1", "!",],
    "o": ["0", "ø"],
    "q": ["9"],
    "s": ["5", "$", "§"],
    "u": ["µ", "v"],
    "x": ["><",],
    "z": ["7_",]
}
def greet() -> None:
    print("      Hello! Are you ready to become an epic HAXOR?")

def main():
    greet()
    unconverted = input("Enter text to convert to leetspeak: ")

    # Convert the input text to leetspeak
    converted = ""
    for char in unconverted:
        if char.lower() in leet_dict:
            converted += random.choice(leet_dict[char.lower()])
        else:
            converted += char

    # Print the converted text
    print(f"Here's your 3P1C L33T5P34K: {converted}. \n      Goodbye! Stay L33T!")
    

if __name__ == "__main__":
    main()