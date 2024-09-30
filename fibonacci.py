def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Please enter a number to return the nth value in the sequence: "))

print(fibonacci(n))
