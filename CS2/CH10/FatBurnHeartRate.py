
def get_age():
    try:
        age = int(input("Enter your age: "))
        if age < 18 or age > 75:
            raise ValueError("Age must be between 18 and 75")
    except ValueError as e:
        print(e)
        age = get_age() #retry after exception
    return age

def fat_burning_heart_rate(age):
    heart_rate = 0.7 * (220 - age)
    return heart_rate

if __name__ == "__main__":
    age = get_age()
    heart_rate = fat_burning_heart_rate(age)
    print("Fat burning heart rate for a", age, "year-old:", heart_rate, "bpm")

