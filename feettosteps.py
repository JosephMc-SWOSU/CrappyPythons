def print_greeting():
    print("Welcome to the Feet to Steps Program!")

def get_user_distance():
    feet = float(input("Please enter the the distance walked in feet: "))
    return feet

def covert_feet_to_steps(feet):
    return feet / 2.5

def eval_progress_towards_goal_and_give_feedback(steps):
    if steps >= 2000:
        print("You have walked", steps, "steps. You have reached your goal! Great job!")
    else:
        print("You have walked", steps, "steps. You have not reached your goal yet. Keep going!")

def print_farewell():
    print("Thank you for using the Feet to Steps Program. Goodbye!")
    
if __name__ == "__main__":
    print_greeting()

    feet = get_user_distance()
    # print("You have entered", feet, "feet.")
    steps = covert_feet_to_steps(feet)
    # print("after the steps print")
    eval_progress_towards_goal_and_give_feedback(steps)

    print_farewell()

