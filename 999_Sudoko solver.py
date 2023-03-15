def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
            return False

    return True


def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def print_board(board):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - -")
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("| ", end="")
            print(board[row][col], end=" ")
        print()


def main():
    board = [[0] * 9 for _ in range(9)]

    print("Enter the initial cells (use 0 for empty cells):")
    for row in range(9):
        row_values = input(f"Row {row + 1}: ")
        for col, value in enumerate(row_values):
            board[row][col] = int(value)

    print("Initial Sudoku board:")
    print_board(board)

    if solve(board):
        print("Solution:")
        print_board(board)
    else:
        print("No solution exists.")


if __name__ == "__main__":
    main()
