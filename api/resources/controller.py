def check_win(board):
    """ Check for a win condition
    Args:
        board (list): board state represented by 2 dimensional list
    Returns:
        winner (string): The winner ("O" or "X") or "" if no winner yet
    """
    rows = [row for row in board]
    diagonals = [[board[x][x] for x in range(0, len(board))], [board[0][2], board[1][1], board[2][0]]]
    columns = [[board[row][column] for row in range(0, len(board))] for column in range(0, len(board))]
    to_test = [rows, diagonals, columns]

    for direction in to_test:
        for element in direction:
            if len(set(element)) == 1:
                matched = set(element).pop()
                if matched != "":
                    return set(element).pop()
    return None


def check_draw(board):
    """
    Check if the state of the current board is a draw
    Args:
        board (list):  the state of the board represented by a two dimensional array

    Returns:
        bool: True or False
    """
    return all("" not in row for row in board)
