import pytest
from ai_logic import evaluate, minimax, find_best_move
from logic import check_win, is_board_full
from utils import format_time # Assuming you put format_time in utils.py

def test_evaluate_win_for_player2():
    board = [
        [2, 2, 2],
        [0, 1, 0],
        [1, 0, 1]
    ]
    assert evaluate(board) == 10

def test_evaluate_win_for_player1():
    board = [
        [1, 1, 1],
        [2, 0, 2],
        [0, 2, 0]
    ]
    assert evaluate(board) == -10

def test_evaluate_tie():
    board = [
        [1, 2, 1],
        [2, 2, 1],
        [1, 1, 2]
    ]
    assert evaluate(board) == 0

def test_format_time():
    assert format_time(3675) == "01:01:15"
    assert format_time(0) == "00:00:00"
    assert format_time(59) == "00:00:59"
    assert format_time(60) == "00:01:00"
    assert format_time(3600) == "01:00:00"


def test_minimax_blocks_win():
    # Player 1 (AI's opponent) is about to win
    board = [
        [1, 1, 0],  # AI should place 2 at (0,2) to block
        [0, 2, 0],
        [0, 0, 0]
    ]
    best_move = find_best_move(board)
    assert best_move == (0, 2)

def test_minimax_finds_winning_move():
    # AI (player 2) is about to win
    board = [
        [2, 2, 0],  # AI should place 2 at (0,2) to win
        [0, 1, 0],
        [1, 0, 1]
    ]
    best_move = find_best_move(board)
    assert best_move == (0, 2)

def test_check_win_row():
    board = [
        [1, 1, 1],
        [0, 2, 0],
        [0, 0, 2]
    ]
    assert check_win(board, 1)
    assert not check_win(board, 2)

def test_check_win_column():
    board = [
        [1, 2, 0],
        [1, 2, 0],
        [1, 0, 2]
    ]
    assert check_win(board, 1)
    assert not check_win(board, 2)

def test_check_win_diagonal():
    board = [
        [2, 1, 1],
        [0, 2, 0],
        [1, 0, 2]
    ]
    assert check_win(board, 2)
    assert not check_win(board, 1)

def test_is_board_full_true():
    board = [
        [1, 2, 1],
        [2, 1, 2],
        [2, 1, 2]
    ]
    assert is_board_full(board)

def test_is_board_full_false():
    board = [
        [1, 2, 0],
        [2, 1, 2],
        [2, 1, 2]
    ]
    assert not is_board_full(board)
