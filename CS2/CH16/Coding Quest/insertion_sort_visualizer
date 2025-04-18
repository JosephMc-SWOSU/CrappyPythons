import matplotlib.pyplot as plt
import random


def visualize_sort(numbers, title):
    """Display the current state of the list as a bar chart."""
    plt.bar(range(len(numbers)), numbers, color='blue')
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(0.5)
    plt.clf()


def insertion_sort_visualized(numbers):
    """Perform insertion sort with visualization."""
    global comparisons, swaps
    comparisons = 0
    swaps = 0

    plt.ion()
    visualize_sort(numbers, "Initial List")

    for i in range(1, len(numbers)):
        j = i
        while j > 0:
            comparisons += 1
            if numbers[j] < numbers[j - 1]:
                numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
                swaps += 1
                visualize_sort(numbers, f"Iteration {i}: Swapping {numbers[j]} and {numbers[j - 1]}")
                j -= 1
            else:
                break

    plt.clf()
    plt.bar(range(len(numbers)), numbers, color='green')
    plt.title("Sorted List")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.ioff()
    plt.show()


if __name__ == '__main__':
    choice = input("Enter '1' to input numbers manually or '2' to generate a random dataset: ")

    if choice == '1':
        numbers = [int(n) for n in input("Enter unsorted numbers separated by spaces: ").split()]
    elif choice == '2':
        size = int(input("Enter the size of the dataset: "))
        numbers = [random.randint(1, 100) for _ in range(size)]
        print(f"Generated dataset: {numbers}")
    else:
        print("Invalid choice. Exiting.")
        exit()

    insertion_sort_visualized(numbers)

    print(f"comparisons: {comparisons}")
    print(f"swaps: {swaps}")