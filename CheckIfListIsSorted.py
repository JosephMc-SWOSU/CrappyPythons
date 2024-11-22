def in_order(int_list):
    for i in range(len(int_list) - 1):
        if int_list[i] < int_list[i + 1]:
            return False
    return True

def primaryfunction():
    # Input the list of integers from the user
    user_input = input("Enter a list of integers separated by spaces: ")
    int_list = list(map(int, user_input.split()))

    # Check if the list is in descending order
    if in_order(int_list):
        print("In descending order")
    else:
        print("Not in order")

if __name__ == "__main__":
    primaryfunction()