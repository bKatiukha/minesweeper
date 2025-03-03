import pytest
import random
from io import StringIO
from unittest.mock import patch
from src.minesweeper.minesweeper import Minesweeper, GameStatistics, GameMenu
from contextlib import redirect_stdout


# Helper function to capture print statements (to test print_board)
def capture_output(func):
    f = StringIO()
    with redirect_stdout(f):
        func()
    return f.getvalue()


# Test for Minesweeper board initialization
def test_board_initialization():
    game = Minesweeper(board_size=5, number_of_mines=3)

    # Ensure the board size is correct
    assert len(game.board) == 5
    assert len(game.board[0]) == 5

    # Ensure the number of mines is correct
    assert len(game.mines) == 3


# Test mine generation does not repeat mines
def test_mine_generation():
    game = Minesweeper(board_size=5, number_of_mines=3)

    # Ensure the number of mines is exactly as specified
    assert len(game.mines) == 3

    # Ensure no duplicate mines are present
    assert len(game.mines) == len(set(game.mines))


# Test that the cell revealing works as expected (check for non-mine cells)
def test_reveal_non_mine():
    game = Minesweeper(board_size=5, number_of_mines=3)

    # Reveal a cell that is not a mine
    x, y = 0, 0
    game.reveal(x, y)

    # Ensure the cell is revealed
    assert (x, y) in game.revealed
    assert game.board[x][y] != " "  # Ensure the cell is not empty (a mine)


# Test that revealing a mine ends the game
def test_reveal_mine():
    game = Minesweeper(board_size=5, number_of_mines=3)
    # Take a mine coordinate and reveal it
    mine = list(game.mines)[0]
    game.reveal(mine[0], mine[1])

    # Ensure the game is over after revealing a mine
    assert game.game_over is True


# Test flagging cells
def test_flag_cell():
    game = Minesweeper(board_size=5, number_of_mines=3)
    x, y = 0, 0

    # Flag a cell
    game.flag(x, y)

    # Ensure the cell is flagged
    assert (x, y) in game.flagged

    # Unflag the same cell
    game.flag(x, y)

    # Ensure the cell is no longer flagged
    assert (x, y) not in game.flagged


# Test printing the board
def test_print_board():
    game = Minesweeper(board_size=5, number_of_mines=3)

    # Capture the output of print_board
    output = capture_output(game.print_board)

    # Ensure the board dimensions are printed
    for i in range(game.board_size):
        assert str(i) in output

    # Ensure the board has ? marks for unrevealed cells
    assert '?' in output


# Test the GameStatistics class updates correctly
def test_game_statistics():
    stats = GameStatistics()

    # Update stats with a win
    stats.update_statistics(won=True)
    assert stats.win_games == 1
    assert stats.loss_games == 0
    assert stats.total_games == 1

    # Update stats with a loss
    stats.update_statistics(won=False)
    assert stats.win_games == 1
    assert stats.loss_games == 1
    assert stats.total_games == 2


# Test the GameMenu class to check if the statistics print correctly
def test_game_menu_statistics():
    menu = GameMenu()

    # Start a new game with win scenario
    game = Minesweeper(board_size=3, number_of_mines=1)
    game.reveal(0, 0)  # Assume this is a non-mine cell
    menu.stats.update_statistics(won=True)

    # Capture the statistics output
    output = capture_output(menu.stats.print_statistics)

    # Ensure the statistics are printed correctly
    assert "Total games played" in output
    assert "Games won" in output
    assert "Games lost" in output
