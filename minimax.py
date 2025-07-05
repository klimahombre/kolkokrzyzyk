import sys
from logic import check_win, is_board_full

ROWS, COLS = 3, 3

def evaluate(board):
    if check_win(board, 2):  # AI wins
        return 10
    elif check_win(board, 1):  # Human wins
        return -10
    else:
        return 0

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score in [10, -10]:
        return score
    if is_board_full(board):
        return 0

    if is_max:
        best = -sys.maxsize
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 0:
                    board[r][c] = 2
                    best = max(best, minimax(board, depth + 1, False))
                    board[r][c] = 0
        return best
    else:
        best = sys.maxsize
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 0:
                    board[r][c] = 1
                    best = min(best, minimax(board, depth + 1, True))
                    board[r][c] = 0
        return best

def find_best_move(board):
    best_val = -sys.maxsize
    best_move = (-1, -1)

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 0:
                board[r][c] = 2
                move_val = minimax(board, 0, False)
                board[r][c] = 0
                if move_val > best_val:
                    best_move = (r, c)
                    best_val = move_val
    return best_move

def ai_move(board):
    if not is_board_full(board):
        row, col = find_best_move(board)
        if row != -1 and col != -1:
            board[row][col] = 2
            return check_win(board, 2)
    return False
