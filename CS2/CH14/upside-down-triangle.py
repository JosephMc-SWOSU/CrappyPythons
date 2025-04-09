def draw_triangle(n, current=0):
    if current >= n:
        return
    else:
        # Calculate the width of the base of the triangle
        width = n * 2 - 1
        # Calculate the number of '#' characters for the current row
        print(('#' * ((n - current) * 2 - 1)).center(width))
        draw_triangle(n, current + 1)

if __name__ == '__main__':
    rows = int(input("Enter the number of rows: "))
    draw_triangle(rows)
