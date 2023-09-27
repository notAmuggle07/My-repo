def create_tic_tac_toe_grid(size):
    if size < 3:
        print("Grid size must be at least 3.")
        return

    # Define Unicode characters for full-width horizontal and vertical lines
    horizontal_line = "━━"  # U+2501
    vertical_line = "┃"  # U+2503

    for i in range(size * 2 - 1):
        if i % 2 == 0:
            # Print the rows with vertical lines and adjusted spacing
            row = vertical_line.join(["  " * 2 + " "] * size)
            print(row)
        else:
            # Print the rows with horizontal lines and gaps
            row = horizontal_line.join([" " * 2 + " "] * (size +1 ))
            print(row)

if __name__ == "__main__":
    try:
        size = int(input("Enter the grid size: "))
        create_tic_tac_toe_grid(size)
    except ValueError:
        print("Invalid input. Please enter an integer for grid size.")