def main():

    triangle_size = int(input("Enter the size of the triangle: "))

    for i in range(triangle_size, 0, -1):
        # Print asterisks
        for k in range(i):
            print("*", end="")
        # Move to the next line
        print()

if __name__ == "__main__":
    main()