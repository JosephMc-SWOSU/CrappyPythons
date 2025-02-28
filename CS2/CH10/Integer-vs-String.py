# Split input into 2 parts: name and age
parts = input("Please enter a first name and age: ").split() #split() returns a list of a name and age
name = parts[0] #name is the first element in the list
while name != '-1':
    try:
        age = int(parts[1]) + 1 #age is the second element in the list and is converted to an integer and incremented by 1
    except ValueError as e:
        print(f'Invalid age: {parts[1]}') #if age is not an integer, print an error message
        age = 0
    print(f'{name} {age}')
   
    parts = input("Please enter another first name and age: ").split() #Get next name and age
    name = parts[0]
