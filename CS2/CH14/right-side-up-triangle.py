def draw_triangle(n, current=1):
    if current > n:
        return
    else:
        # Calculate the width of the base of the triangle
        width = n * 2 - 1
        # Center the current row of '#' characters
        print(('#' * (current * 2 - 1)).center(width))
        draw_triangle(n, current + 1)


if __name__ == '__main__':
    base_length = int(input("how many rows? "))
    draw_triangle(base_length)
