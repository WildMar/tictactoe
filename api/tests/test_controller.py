import pytest

from controller import _check_edges, find_near_win
from controller import check_draw
from controller import check_win


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
