feet = float(input("Please enter the the distance walked in feet: "))

def FeetToSteps(feet):
    return feet / 2.5

steps = FeetToSteps(feet)

if steps >= 2000:
    print("You have walked", steps, "steps. You have reached your goal! Great job!")
else:
    print("You have walked", steps, "steps. You have not reached your goal yet. Keep going!")