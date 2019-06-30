import pytest

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
