def create_contact_list(contact_pairs):
    contact_list = {}
    for pair in contact_pairs:
        name, phone_number = pair.split(',')
        contact_list[name] = phone_number
    return contact_list

def primaryfunction():
    # Input the contact pairs and the search name
    contact_pairs_input = input("Enter contact pairs (name,phone_number): ").split()
    search_name = input("Enter the name to search for: ")

    # Create the contact list dictionary
    contact_list = create_contact_list(contact_pairs_input)

    # Output the phone number associated with the search name
    if search_name in contact_list:
        print(contact_list[search_name])
    else:
        print("Name not found in contact list.")

if __name__ == "__main__":
    primaryfunction()