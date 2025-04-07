def print_all_permutations(permList, nameList):
    # TODO: Implement method to create and output all permutations of the list of names.
    if len(nameList) == 0:
        print(permList)
    else:
        for i in range(len(nameList)):
            # Create a new list without the current name
            newPermList = permList + [nameList[i]]
            newNameList = nameList[:i] + nameList[i+1:]
            print_all_permutations(newPermList, newNameList)

if __name__ == "__main__":
    nameList = input("Please input a list of names separated by a space. ").split(' ')
    permList = []
    print_all_permutations(permList, nameList)
