def check_win(board, player):
    # Wiersze
    for row in board:
        if row.count(player) == 3:
            return True
    # Kolumny
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True
    # Przekątne
    if [board[i][i] for i in range(3)].count(player) == 3:
        return True
    if [board[i][2 - i] for i in range(3)].count(player) == 3:
        return True
    return False


def is_board_full(board):
    return all(cell != 0 for row in board for cell in row)
