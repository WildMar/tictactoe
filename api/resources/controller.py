import copy
import random


def check_win(board):
    """ Check for a win condition
    Args:
        board (list): board state represented by a matrix
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
                    return matched
    return None


def check_draw(board):
    """
    Check if the state of the current board is a draw
    Args:
        board (list):  the state of the board represented by a matrix

    Returns:
        bool: True or False
    """
    return all("" not in row for row in board)


def calculate_next_move(board, move_number):
    """
    Determines and marks the board for the next turn.
    Args:
        board (list): The board state represented by a matrix
        move_number (int): The number of move the game is on

    Returns:
        list: A new board with the new move recorded in the matrix
    """

    if move_number == 1:
        new_board = _first_move(board=board)
        return new_board
    else:
        # Check if we're close to winning and take it
        x, y = find_near_win(board=board, player="X")
        if x and y:
            new_board = copy.deepcopy(board)
            new_board[x][y] = "X"
            return new_board

        # Check if they are close to winning and block
        x, y = find_near_win(board=board, player="O")
        if x and y:
            new_board = copy.deepcopy(board)
            new_board[x][y] = "X"
            return new_board


def _first_move(board):
    """
    The first move of the game is the most important. Therefore, this method determines the
    best first move given that your opponent has already played

    If your opponent hasn't selected the middle block, take it.
    If your opponent has selected an edge, pick a far corner
    If your opponent has selected the center, pick the first corner
    Examples:
          X |    |
        ==============
            |    | O
        ==============
            |    |
    Args:
        board (list): The board state represented by a matrix

    Returns:
        list: A new board with the new move recorded in the matrix

    """

    # If the opponent hasn't taken the middle, do so
    if board[1][1] == "":
        new_board = copy.deepcopy(board)
        new_board[1][1] = "X"
        return new_board
    elif board[1][1] == "O":
        # If they had taken the center, pick the first corner
        new_board = copy.deepcopy(board)
        new_board[0][0] = "X"
        return new_board

    new_board = _check_edges(board)
    if new_board:
        return new_board


def _check_edges(board):
    """
    If an opponent has taken an edge, return the new board with your counter
    Args:
        board (list): The state of the board represented by a matrix

    Returns:
        The new board if the opponent has taken an edge, None otherwise
    """
    # If the opponent has taken an edge, take the far corner from that edge
    row1_edges = [board[0][1]]
    row2_edges = [board[1][0], board[1][2]]
    row3_edges = [board[2][1]]

    to_check = [row1_edges, row2_edges, row3_edges]
    if not any("O" in edges for edges in to_check):
        return None

    new_board = copy.deepcopy(board)
    position = random.choice(0, 2)
    if "O" in row1_edges:
        new_board[2][position] = "X"
    elif row2_edges[0] == "O":
        new_board[position][2] = "X"
    elif row2_edges[1] == "O":
        new_board[position][0] = "X"
    elif "O" in row3_edges:
        new_board[0][position] = "X"
    return new_board


def find_near_win(board, player):
    """
    Find out if the given player can win with one move based on the state of the board
    Args:
        board (list): The board state represented by a matrix
        player (string): The player's representation on the board
    Returns:
         tuple(int, int): the position to take for the winning move
    """
    rows = [row for row in board]
    diagonals = [[board[x][x] for x in range(0, len(board))], [board[0][2], board[1][1], board[2][0]]]
    columns = [[board[row][column] for row in range(0, len(board))] for column in range(0, len(board))]
    to_test = [rows, diagonals, columns]
    element_idx = 0
    for direction in to_test:
        for element in direction:
            if "" in element:
                if element.count(player) == 2:
                    # TODO: if there's time, come back and make this cleaner
                    if len(direction) == 2:
                        # It is a diagonal win, therefore treated differently
                        if direction.index(element) == 0:
                            return element.index(""), element.index("")
                        else:
                            if element.index("") == 0:
                                return 2, 0
                            elif element.index("") == 1:
                                return 1, 1
                            elif element.index("") == 2:
                                return 0, 2
                    return direction.index(element), element.index("")
            element_idx += 1
        element_idx = 0
    return None, None
