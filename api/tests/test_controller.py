import pytest

from controller import Play


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
    assert Play(board=board, move_number=9, player="X").check_win() == winner


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
    assert Play(board=board, move_number=9, player="X").check_draw() == is_draw


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
    assert Play(board=board, move_number=9, player="X")._check_edges() == expected_return


@pytest.mark.parametrize("board, x, y", [
    ([["O", "O", ""],
      ["", "", ""],
      ["", "", ""]], 0, 2),
    ([["O", "", ""],
      ["", "O", ""],
      ["", "", ""]], 2, 2),
    ([["", "", ""],
      ["O", "", ""],
      ["O", "", ""]], 0, 0),
    ([["O", "", ""],
      ["", "O", ""],
      ["", "", "X"]], None, None)
])
def test_find_near_win(board, x, y):
    x_idx, y_idx = Play(board=board, move_number=9, player="O").find_near_win(player="O")
    assert x_idx == x
    assert y_idx == y


@pytest.mark.parametrize("board, move_number, expected_board, expected_game_status", [
    # Opponent didnt take center
    ([["O", "", ""],
      ["", "", ""],
      ["", "", ""]], 1, [["O", "", ""], ["", "X", ""], ["", "", ""]], "IN PROGRESS"),
    ([["", "O", ""],
      ["", "", ""],
      ["", "", ""]], 1, [["", "O", ""], ["", "X", ""], ["", "", ""]], "IN PROGRESS"),
    ([["", "", "O"],
      ["", "", ""],
      ["", "", ""]], 1, [["", "", "O"], ["", "X", ""], ["", "", ""]], "IN PROGRESS"),
    ([["O", "", ""],
      ["", "", ""],
      ["", "", ""]], 1, [["O", "", ""], ["", "X", ""], ["", "", ""]], "IN PROGRESS"),
    ([["", "O", ""],
      ["", "", ""],
      ["", "", ""]], 1, [["", "O", ""], ["", "X", ""], ["", "", ""]], "IN PROGRESS"),
    ([["", "", "O"],
      ["", "", ""],
      ["", "", ""]], 1, [["", "", "O"], ["", "X", ""], ["", "", ""]], "IN PROGRESS"),
    ([["O", "", ""],
      ["", "", ""],
      ["", "", ""]], 1, [["O", "", ""], ["", "X", ""], ["", "", ""]], "IN PROGRESS"),
    ([["", "O", ""],
      ["", "", ""],
      ["", "", ""]], 1, [["", "O", ""], ["", "X", ""], ["", "", ""]], "IN PROGRESS"),
    # Opponent takes center
    ([["", "", ""],
      ["", "O", ""],
      ["", "", ""]], 1, [["X", "", ""], ["", "O", ""], ["", "", ""]], "IN PROGRESS"),
    # Not first turn
    ([["O", "O", ""],
      ["", "X", ""],
      ["", "", ""]], 3, [["O", "O", "X"], ["", "X", ""], ["", "", ""]], "IN PROGRESS"),
    ([["O", "O", "X"],
      ["O", "X", ""],
      ["", "", ""]], 5, [["O", "O", "X"], ["O", "X", ""], ["X", "", ""]], "IN PROGRESS"),
    ([["O", "", ""],
      ["", "X", ""],
      ["O", "", ""]], 3, [["O", "", ""], ["X", "X", ""], ["O", "", ""]], "IN PROGRESS"),
    ([["O", "", ""],
      ["X", "X", "O"],
      ["O", "", ""]], 5, [["O", "X", ""], ["X", "X", "O"], ["O", "", ""]], "IN PROGRESS"),
    ([["O", "X", ""],
      ["X", "X", "O"],
      ["O", "O", ""]], 3, [["O", "X", ""], ["X", "X", "O"], ["O", "O", "X"]], "IN PROGRESS"),
    ([["O", "X", "O"],
      ["X", "X", "O"],
      ["O", "O", "X"]], 3, [["O", "X", "O"], ["X", "X", "O"], ["O", "O", "X"]], "DRAW"),
    ([["O", "X", "O"],
      ["X", "X", "O"],
      ["O", "X", "X"]], 3, [["O", "X", "O"], ["X", "X", "O"], ["O", "X", "X"]], "WINNER: X"),
])
def test_calculate_next_move(board, move_number, expected_board, expected_game_status):
    resulting_board, game_status = Play(board=board, move_number=move_number, player="X").calculate_next_move()
    assert resulting_board == expected_board
    assert game_status == expected_game_status


@pytest.mark.parametrize("board, x, y", [
    ([["O", "O", ""],
      ["", "", ""],
      ["", "", ""]], 0, 2),
    ([["O", "", "O"],
      ["", "", ""],
      ["", "", ""]], 0, 1),
    ([["", "O", "O"],
      ["", "", ""],
      ["", "", ""]], 0, 0),
    ([["", "", ""],
      ["O", "O", ""],
      ["", "", ""]], 1, 2),
    ([["", "", ""],
      ["O", "", "O"],
      ["", "", ""]], 1, 1),
    ([["", "", ""],
      ["", "O", "O"],
      ["", "", ""]], 1, 0),
    ([["", "", ""],
      ["", "", ""],
      ["O", "O", ""]], 2, 2),
    ([["", "", ""],
      ["", "", ""],
      ["O", "", "O"]], 2, 1),
    ([["", "", ""],
      ["", "", ""],
      ["", "O", "O"]], 2, 0),
])
def test_find_row_win(board, x, y):
    x_idx, y_idx = Play(board=board, move_number=9, player="O")._find_row_win(player="O", rows=board)
    assert x_idx == x
    assert y_idx == y


@pytest.mark.parametrize("board, x, y", [
    ([["O", "", ""],
      ["O", "", ""],
      ["", "", ""]], 2, 0),
    ([["O", "", ""],
      ["", "", ""],
      ["O", "", ""]], 1, 0),
    ([["", "", ""],
      ["O", "", ""],
      ["O", "", ""]], 0, 0),
    ([["", "O", ""],
      ["", "O", ""],
      ["", "", ""]], 2, 1),
    ([["", "O", ""],
      ["", "", ""],
      ["", "O", ""]], 1, 1),
    ([["", "", ""],
      ["", "O", ""],
      ["", "O", ""]], 0, 1),
    ([["", "", "O"],
      ["", "", "O"],
      ["", "", ""]], 2, 2),
    ([["", "", "O"],
      ["", "", ""],
      ["", "", "O"]], 1, 2),
    ([["", "", ""],
      ["", "", "O"],
      ["", "", "O"]], 0, 2),
])
def test_find_column_win(board, x, y):
    columns = [[board[row][column] for row in range(0, len(board))] for column in range(0, len(board))]
    x_idx, y_idx = Play(board=board, move_number=9, player="O")._find_column_win(columns=columns, player="O")
    assert x_idx == x
    assert y_idx == y


@pytest.mark.parametrize("board, x, y", [
    ([["O", "", ""],
      ["", "O", ""],
      ["", "", ""]], 2, 2),
    ([["", "", ""],
      ["", "O", ""],
      ["", "", "O"]], 0, 0),
    ([["O", "", ""],
      ["", "", ""],
      ["", "", "O"]], 1, 1),
    ([["", "", "O"],
      ["", "O", ""],
      ["", "", ""]], 2, 0),
    ([["", "", "O"],
      ["", "", ""],
      ["O", "", ""]], 1, 1),
    ([["", "", ""],
      ["", "O", ""],
      ["O", "", ""]], 0, 2),
])
def test_find_diagonal_win(board, x, y):
    diagonals = [[board[x][x] for x in range(0, len(board))], [board[0][2], board[1][1], board[2][0]]]

    x_idx, y_idx = Play(board=board, move_number=9, player="O")._find_diagonal_win(diagonals, player="O")
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
        board, status = Play(board=board, move_number=9, player="X").calculate_next_move()
        if "WINNER" in status or "DRAW" in status:
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
        move_number += 1

    assert "WINNER" in status or "DRAW" in status
    assert board
