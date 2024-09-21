#Obtain user input for two strings and assign them to variables string1 and string2.
print("Please enter two strings to compare their lengths.")
while True:
    string1 = input("Please enter the first string: ")
    if string1.strip() == "":
        print("The first string cannot be empty. Please enter a valid string.")
        continue
    string2 = input("Please enter the second string: ")
    if string2.strip() == "":
        print("The second string cannot be empty. Please enter a valid string.")
        continue
    break
#compare the lencgth of string1 and string2 and print a message stating which string is longer or if they are the same length.
if len(string1) > len(string2):
    print(f"'{string1} is longer than '{string2}'")
elif len(string1) < len(string2):
    print(f"'{string2}' is longer than '{string1}'")
else:
    print(f"'{string1}' and '{string2}' are the same length")