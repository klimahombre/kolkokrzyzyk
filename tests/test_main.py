import pytest
from main import evaluate, format_time, minimax, find_best_move
from logic import check_win, is_board_full

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

def test_minimax_blocks_win():
    board = [
        [1, 1, 0],
        [0, 2, 0],
        [0, 0, 2]
    ]
    best = find_best_move(board)
    assert best == (0, 2)

def test_check_win_row():
    board = [
        [1, 1, 1],
        [0, 2, 0],
        [0, 0, 2]
    ]
    assert check_win(board, 1)

def test_check_win_column():
    board = [
        [1, 2, 0],
        [1, 2, 0],
        [1, 0, 2]
    ]
    assert check_win(board, 1)

def test_check_win_diagonal():
    board = [
        [2, 1, 1],
        [0, 2, 0],
        [1, 0, 2]
    ]
    assert check_win(board, 2)

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

Add test_main.py with pytest tests
