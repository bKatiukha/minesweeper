import pytest
import random
from io import StringIO
from unittest.mock import patch
from src.minesweeper.minesweeper import Minesweeper, GameStatistics


# Test Minesweeper board initialization
def test_minesweeper_initialization():
    # Initialize Minesweeper game with default board size and number of mines
    game = Minesweeper(board_size=8, number_of_mines=10)

    # Check board size
    assert len(game.board) == 8
    assert len(game.board[0]) == 8

    # Check number of mines
    assert len(game.mines) == 10

    # Check initial game state
    assert not game.game_over
    assert not game.revealed
    assert not game.flagged


# Test reveal method on non-mine cells
def test_reveal_non_mine():
    game = Minesweeper(board_size=8, number_of_mines=10)

    # Ensure reveal works correctly on a non-mine cell
    x, y = 0, 0
    game.reveal(x, y)

    # Ensure the cell is revealed and no game over occurs
    assert (x, y) in game.revealed
    assert not game.game_over


# Test reveal method on a mine
def test_reveal_mine():
    game = Minesweeper(board_size=8, number_of_mines=10)

    # Find a mine to reveal
    mine = list(game.mines)[0]
    x, y = mine
    game.reveal(x, y)

    # Game should be over after revealing a mine
    assert game.game_over
    assert len(game.revealed) == 0  # No cells should be revealed


# Test flag method
def test_flag():
    game = Minesweeper(board_size=8, number_of_mines=10)

    # Flag a cell
    x, y = 1, 1
    game.flag(x, y)

    # Ensure the cell is flagged
    assert (x, y) in game.flagged

    # Flagging the same cell should toggle the flag
    game.flag(x, y)
    assert (x, y) not in game.flagged


# Test reveal method on adjacent empty cells (recursive reveal)
def test_recursive_reveal():
    game = Minesweeper(board_size=8, number_of_mines=10)

    # Find a cell with no mines around it (empty cell)
    empty_cell = None
    for x in range(game.board_size):
        for y in range(game.board_size):
            if game.board[x][y] == ' ':
                empty_cell = (x, y)
                break
        if empty_cell:
            break

    # Reveal the empty cell
    x, y = empty_cell
    game.reveal(x, y)

    # Ensure the empty cell and its adjacent cells are revealed
    assert (x, y) in game.revealed
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < game.board_size and 0 <= ny < game.board_size:
                assert (nx, ny) in game.revealed or (nx, ny) in game.mines


# Test invalid coordinate input for reveal and flag
def test_invalid_coordinates():
    game = Minesweeper(board_size=8, number_of_mines=10)

    # Test invalid coordinates for reveal
    with patch('builtins.input', return_value="10 10"):
        x, y = game.get_input()
        assert x == -1 and y == -1  # Invalid coordinates will retry

    # Test invalid coordinates for flag
    with patch('builtins.input', return_value="10 10"):
        x, y = game.get_input()
        game.flag(x, y)
        assert (x, y) not in game.flagged  # No flag should be set for invalid coordinates


# Test game statistics update after winning or losing
def test_game_statistics():
    # Create a game statistics instance
    stats = GameStatistics()

    # Update statistics for a win
    stats.update_statistics(won=True)
    assert stats.total_games == 1
    assert stats.win_games == 1
    assert stats.loss_games == 0

    # Update statistics for a loss
    stats.update_statistics(won=False)
    assert stats.total_games == 2
    assert stats.win_games == 1
    assert stats.loss_games == 1


# Test start game scenario
def test_game_play_win():
    with patch('builtins.input', side_effect=["1", "0 0"]):
        game = Minesweeper(board_size=8, number_of_mines=10)
        game.start_game()  # Simulate a successful reveal
        assert not game.game_over  # Game should not be over after a successful reveal


# Test a full game where the player wins
def test_game_play_loss():
    with patch('builtins.input', side_effect=["1", "0 0"]):
        game = Minesweeper(board_size=8, number_of_mines=10)
        game.start_game()  # Simulate a loss (mine is revealed)
        assert game.game_over  # Game should end with a mine hit


# Test print board function (capture print output)
def test_print_board():
    game = Minesweeper(board_size=8, number_of_mines=10)

    with patch('sys.stdout', new_callable=StringIO) as fake_out:
        game.print_board()
        printed_output = fake_out.getvalue()

        # Ensure the board contains the header and the first row is printed
        assert "  0 1 2 3 4 5 6 7" in printed_output
        assert "0 ?" in printed_output
