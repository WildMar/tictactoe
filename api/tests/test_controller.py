import pytest

from controller import _check_edges
from controller import _find_column_win
from controller import _find_diagonal_win
from controller import _find_row_win
from controller import calculate_next_move
from controller import check_draw
from controller import check_win
from controller import find_near_win


@pytest.mark.parametrize("board, winner", [
    ([["", "", ""],
      ["", "", ""],
      ["", "", ""]], None),
    ([["O", "O", "O"],
      ["", "", ""],
      ["", "", ""]], "O"),
    ([["", "", ""],
      ["O", "O", "O"],
      ["", "", ""]], "O"),
    ([["", "", ""],
      ["", "", ""],
      ["O", "O", "O"]], "O"),
    ([["O", "", ""],
      ["", "O", ""],
      ["", "", "O"]], "O"),
    ([["", "", "O"],
      ["", "O", ""],
      ["O", "", ""]], "O"),
    ([["O", "", ""],
      ["O", "", ""],
      ["O", "", ""]], "O"),
    ([["", "O", ""],
      ["", "O", ""],
      ["", "O", ""]], "O"),
    ([["", "", "O"],
      ["", "", "O"],
      ["", "", "O"]], "O"),
    ([["O", "", ""],
      ["O", "O", ""],
      ["", "", ""]], None),
    ([["X", "O", "X"],
      ["X", "O", "X"],
      ["O", "X", "O"]], None),
])
def test_check_win(board, winner):
    assert check_win(board) == winner


@pytest.mark.parametrize("board, is_draw", [
    ([["", "", ""],
      ["", "", ""],
      ["", "", ""]], False),
    ([["O", "O", "O"],
      ["", "", ""],
      ["", "", ""]], False),
    ([["O", "X", "X"],
      ["O", "X", "O"],
      ["X", "O", "X"]], True)])
def test_draw(board, is_draw):
    assert check_draw(board) == is_draw


@pytest.mark.parametrize("board, expected_return", [
    ([["O", "", ""],
      ["", "", ""],
      ["", "", ""]], None),
    ([["", "", "O"],
      ["", "", ""],
      ["", "", ""]], None),
    ([["", "", ""],
      ["", "", ""],
      ["O", "", ""]], None),
    ([["", "", ""],
      ["", "", ""],
      ["", "", "O"]], None),
    ([["", "", ""],
      ["", "O", ""],
      ["", "", ""]], None),
    ([["", "O", ""],
      ["", "", ""],
      ["", "", ""]], [["", "O", ""], ["", "", ""], ["X", "", ""]]),
    ([["", "", ""],
      ["O", "", ""],
      ["", "", ""]], [["", "", "X"], ["O", "", ""], ["", "", ""]]),
    ([["", "", ""],
      ["", "", ""],
      ["", "O", ""]], [["X", "", ""], ["", "", ""], ["", "O", ""]]),
    ([["", "", ""],
      ["", "", "O"],
      ["", "", ""]], [["X", "", ""], ["", "", "O"], ["", "", ""]])
])
def test_check_edges(board, expected_return):
    assert _check_edges(board=board) == expected_return


@pytest.mark.parametrize("board, player, x, y", [
    ([["O", "O", ""],
      ["", "", ""],
      ["", "", ""]], "O", 0, 2),
    ([["O", "", ""],
      ["", "O", ""],
      ["", "", ""]], "O", 2, 2),
    ([["", "", ""],
      ["O", "", ""],
      ["O", "", ""]], "O", 0, 0),
    ([["O", "", ""],
      ["", "O", ""],
      ["", "", "X"]], "O", None, None)
])
def test_find_near_win(board, player, x, y):
    x_idx, y_idx = find_near_win(board=board, player=player)
    assert x_idx == x
    assert y_idx == y


@pytest.mark.parametrize("board, move_number, expected_result", [
    # Opponent didnt take center
    ([["O", "", ""],
      ["", "", ""],
      ["", "", ""]], 1, [["O", "", ""], ["", "X", ""], ["", "", ""]]),
    ([["", "O", ""],
      ["", "", ""],
      ["", "", ""]], 1, [["", "O", ""], ["", "X", ""], ["", "", ""]]),
    ([["", "", "O"],
      ["", "", ""],
      ["", "", ""]], 1, [["", "", "O"], ["", "X", ""], ["", "", ""]]),
    ([["O", "", ""],
      ["", "", ""],
      ["", "", ""]], 1, [["O", "", ""], ["", "X", ""], ["", "", ""]]),
    ([["", "O", ""],
      ["", "", ""],
      ["", "", ""]], 1, [["", "O", ""], ["", "X", ""], ["", "", ""]]),
    ([["", "", "O"],
      ["", "", ""],
      ["", "", ""]], 1, [["", "", "O"], ["", "X", ""], ["", "", ""]]),
    ([["O", "", ""],
      ["", "", ""],
      ["", "", ""]], 1, [["O", "", ""], ["", "X", ""], ["", "", ""]]),
    ([["", "O", ""],
      ["", "", ""],
      ["", "", ""]], 1, [["", "O", ""], ["", "X", ""], ["", "", ""]]),
    # Opponent takes center
    ([["", "", ""],
      ["", "O", ""],
      ["", "", ""]], 1, [["X", "", ""], ["", "O", ""], ["", "", ""]]),
    # Not first turn
    ([["O", "O", ""],
      ["", "X", ""],
      ["", "", ""]], 3, [["O", "O", "X"], ["", "X", ""], ["", "", ""]]),
    ([["O", "O", "X"],
      ["O", "X", ""],
      ["", "", ""]], 5, [["O", "O", "X"], ["O", "X", ""], ["X", "", ""]]),
    ([["O", "", ""],
      ["", "X", ""],
      ["O", "", ""]], 3, [["O", "", ""], ["X", "X", ""], ["O", "", ""]]),
    ([["O", "", ""],
      ["X", "X", "O"],
      ["O", "", ""]], 5, [["O", "X", ""], ["X", "X", "O"], ["O", "", ""]]),
    ([["O", "X", ""],
      ["X", "X", "O"],
      ["O", "O", ""]], 3, [["O", "X", ""], ["X", "X", "O"], ["O", "O", "X"]]),
    ([["O", "X", "O"],
      ["X", "X", "O"],
      ["O", "O", "X"]], 3, "DRAW"),
    ([["O", "X", "O"],
      ["X", "X", "O"],
      ["O", "X", "X"]], 3, "WINNER: X"),
])
def test_calculate_next_move(board, move_number, expected_result):
    result = calculate_next_move(board=board, move_number=move_number, player="X")
    assert result == expected_result


@pytest.mark.parametrize("board, player, x, y", [
    ([["O", "O", ""],
      ["", "", ""],
      ["", "", ""]], "O", 0, 2),
    ([["O", "", "O"],
      ["", "", ""],
      ["", "", ""]], "O", 0, 1),
    ([["", "O", "O"],
      ["", "", ""],
      ["", "", ""]], "O", 0, 0),
    ([["", "", ""],
      ["O", "O", ""],
      ["", "", ""]], "O", 1, 2),
    ([["", "", ""],
      ["O", "", "O"],
      ["", "", ""]], "O", 1, 1),
    ([["", "", ""],
      ["", "O", "O"],
      ["", "", ""]], "O", 1, 0),
    ([["", "", ""],
      ["", "", ""],
      ["O", "O", ""]], "O", 2, 2),
    ([["", "", ""],
      ["", "", ""],
      ["O", "", "O"]], "O", 2, 1),
    ([["", "", ""],
      ["", "", ""],
      ["", "O", "O"]], "O", 2, 0),
])
def test_find_row_win(board, player, x, y):
    x_idx, y_idx = _find_row_win(board, player)
    assert x_idx == x
    assert y_idx == y


@pytest.mark.parametrize("board, player, x, y", [
    ([["O", "", ""],
      ["O", "", ""],
      ["", "", ""]], "O", 2, 0),
    ([["O", "", ""],
      ["", "", ""],
      ["O", "", ""]], "O", 1, 0),
    ([["", "", ""],
      ["O", "", ""],
      ["O", "", ""]], "O", 0, 0),
    ([["", "O", ""],
      ["", "O", ""],
      ["", "", ""]], "O", 2, 1),
    ([["", "O", ""],
      ["", "", ""],
      ["", "O", ""]], "O", 1, 1),
    ([["", "", ""],
      ["", "O", ""],
      ["", "O", ""]], "O", 0, 1),
    ([["", "", "O"],
      ["", "", "O"],
      ["", "", ""]], "O", 2, 2),
    ([["", "", "O"],
      ["", "", ""],
      ["", "", "O"]], "O", 1, 2),
    ([["", "", ""],
      ["", "", "O"],
      ["", "", "O"]], "O", 0, 2),
])
def test_find_column_win(board, player, x, y):
    columns = [[board[row][column] for row in range(0, len(board))] for column in range(0, len(board))]
    x_idx, y_idx = _find_column_win(columns, player)
    assert x_idx == x
    assert y_idx == y


@pytest.mark.parametrize("board, player, x, y", [
    ([["O", "", ""],
      ["", "O", ""],
      ["", "", ""]], "O", 2, 2),
    ([["", "", ""],
      ["", "O", ""],
      ["", "", "O"]], "O", 0, 0),
    ([["O", "", ""],
      ["", "", ""],
      ["", "", "O"]], "O", 1, 1),
    ([["", "", "O"],
      ["", "O", ""],
      ["", "", ""]], "O", 2, 0),
    ([["", "", "O"],
      ["", "", ""],
      ["O", "", ""]], "O", 1, 1),
    ([["", "", ""],
      ["", "O", ""],
      ["O", "", ""]], "O", 0, 2),
])
def test_find_diagonal_win(board, player, x, y):
    diagonals = [[board[x][x] for x in range(0, len(board))], [board[0][2], board[1][1], board[2][0]]]

    x_idx, y_idx = _find_diagonal_win(diagonals, player)
    assert x_idx == x
    assert y_idx == y


@pytest.mark.parametrize("board", [
    ([["O", "", ""],
      ["", "", ""],
      ["", "", ""]]),
    ([["", "O", ""],
      ["", "", ""],
      ["", "", ""]]),
    ([["", "", "O"],
      ["", "", ""],
      ["", "", ""]]),
    ([["", "", ""],
      ["O", "", ""],
      ["", "", ""]]),
    ([["", "", ""],
      ["", "O", ""],
      ["", "", ""]]),
    ([["", "", ""],
      ["", "", "O"],
      ["", "", ""]]),
    ([["", "", ""],
      ["", "", ""],
      ["O", "", ""]]),
    ([["", "", ""],
      ["", "", ""],
      ["", "O", ""]]),
    ([["", "", ""],
      ["", "", ""],
      ["", "", "O"]]),
])
def test_full_game(board):
    result = ""
    current_player = "X"
    move_number = 1
    status = ""
    while "WINNER" not in result:
        board, status = calculate_next_move(board, move_number, current_player)
        if "WINNER" in status or "DRAW" in status:
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
        move_number += 1

    assert "WINNER" in status or "DRAW" in status
    assert board
