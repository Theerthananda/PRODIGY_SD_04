def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_safe(grid, row, col, num):
    if num in grid[row]:
        return False
    if num in [grid[i][col] for i in range(9)]:
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def get_sudoku_input():
    print("Enter the Sudoku puzzle row by row.")
    print("Use space-separated numbers, and enter 0 for empty cells.")
    grid = []
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Enter row {i + 1}: ").strip().split()))
                if len(row) == 9 and all(0 <= num <= 9 for num in row):
                    grid.append(row)
                    break
                else:
                    print("Invalid input. Please enter 9 numbers (0-9).")
            except ValueError:
                print("Invalid input. Please enter valid integers.")
    return grid

if __name__ == "__main__":
    sudoku_grid = get_sudoku_input()

    print("\nOriginal Sudoku Grid:")
    print_grid(sudoku_grid)

    if solve_sudoku(sudoku_grid):
        print("\nSolved Sudoku Grid:")
        print_grid(sudoku_grid)
    else:
        print("\nNo solution exists.")
