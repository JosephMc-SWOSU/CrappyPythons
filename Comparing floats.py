import math

# Grab input from user
while True:
	input1 = input("Enter a number: ")
	input2 = input("Enter another number: ")
	epsilon2 = input("Enter difference threshold: ")
	try:
		float1 = float(input1)
		float2 = float(input2)
		epsilon = float(epsilon2)
		break  # Exit loop if conversion is good
	except ValueError:
		print("Invalid input. Please enter valid numbers.")

# Perform comparisons
if math.isclose(float1, float2, abs_tol=0.001):
	print("The two numbers are equal")
elif math.isclose(float1, float2, abs_tol=epsilon):
	print("Close enough")
else:
	print("The two numbers are not close")