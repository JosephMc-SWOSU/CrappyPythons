def getusername():
    inputname = input("Please enter your name to format it: ")
    return inputname

def separate_name(name):
    name_parts = name.split()
    if len(name_parts) >= 2:
        first_name = name_parts[0]
        last_name = name_parts[-1]
        if len(name_parts) == 3:
            middle_name = name_parts[1]
            formatted_name = f"{last_name}, {first_name[0]}. {middle_name[0]}."
        else:
            formatted_name = f"{last_name}, {first_name[0]}."
        return formatted_name
    else:
        return name  # Return the original name if it doesn't have at least two parts

print(separate_name(getusername()))