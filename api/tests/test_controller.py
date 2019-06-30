import pytest

from controller import _check_edges
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
