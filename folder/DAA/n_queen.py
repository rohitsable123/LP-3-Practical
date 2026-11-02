
def n_queen(n):

    board = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        board.append(row)

    def is_safe(row, col):

        # column check
        for i in range(row):
            if board[i][col] == 1:
                return False

        # upper left diagonal check
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # upper right diagonal check
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def backtrack(row):
        if row == n:
            return True

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 1

                if backtrack(row + 1):
                    return True

                board[row][col] = 0

        return False

    board[0][0] = 1

    if backtrack(1):
        for row in board:
            print(row)
    else:
        print("NO solution exists for n = ", n)

n = int(input("Enter value of N: "))

if n >= 1:
    n_queen(n)
else:
    print("Error: enter a positive number! ")