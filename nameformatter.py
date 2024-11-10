def separate_name(name):
    name_parts = name.split()
    if len(name_parts) >= 2:
        # Capitalize the first letter of each name part if not already capitalized
        name_parts = [part[0].upper() + part[1:] for part in name_parts]
        
        first_name = name_parts[0]
        last_name = name_parts[-1]
        
        if len(name_parts) == 3:
            middle_name = name_parts[1]
            formatted_name = f"{last_name}, {first_name[0]}. {middle_name[0]}."
        else:
            formatted_name = f"{last_name}, {first_name[0]}."
        return formatted_name

if __name__ == "__main__":
    user_name = input("Please enter your name: ")
    formatted_name = separate_name(user_name)
    if formatted_name:
        print(f"Your name is formatted as: {formatted_name}")
    else:
        print("Please enter a first and last name, with an optional middle name.")