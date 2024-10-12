def main():

    triangle_size = int(input("Enter the size of the triangle: "))

    # Loop from triangle_size down to 1
    for row in range(triangle_size, 0, -1):
        # Print asterisks for the current row
        for _ in range(row):
            print("*", end="")
        # Move to the next line after printing all asterisks in the current row
        print()

if __name__ == "__main__":
    main()