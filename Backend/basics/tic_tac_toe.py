def create_tic_tac_toe_grid(size):
    if size < 3:
        print("Grid size must be at least 3.")
        return

    horizontal_line = "━━"
    vertical_line = "┃"

    for i in range(size * 2 - 1):
        if i % 2 == 0:
            row = vertical_line.join(["  " * 2 + " "] * size)
            print(row)
        else:
            row = horizontal_line.join([" " * 2 + " "] * (size +1 ))
            print(row)

if __name__ == "__main__":
    try:
        size = int(input("Enter the grid size: "))
        create_tic_tac_toe_grid(size)
    except ValueError:
        print("Invalid input. Please enter an integer for grid size.")
