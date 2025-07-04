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
