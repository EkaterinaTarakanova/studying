def check_winner(board):
    for row in board:
        if row.count("X") == len(row):
            return "X"
        elif row.count("O") == len(row):
            return "O"
    for col in range(len(board[0])):
        column = [board[row][col] for row in range(len(board))]
        if column.count("X") == len(column):
            return "X"
        elif column.count("O") == len(column):
            return "O"
    diagonal1 = [board[i][i] for i in range(len(board))]
    diagonal2 = [board[i][len(board)-1-i] for i in range(len(board))]
    if diagonal1.count("X") == len(diagonal1) or diagonal2.count("X") == len(diagonal2):
        return "X"
    elif diagonal1.count("O") == len(diagonal1) or diagonal2.count("O") == len(diagonal2):
        return "O"
    return "Ничья"

board = []
for _ in range(3):
    row = input().strip()
    board.append(list(row))
winner = check_winner(board)
print(winner)
