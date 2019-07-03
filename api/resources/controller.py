import copy
import random


class Play(object):

    def __init__(self, player, move_number, board):
        self.board = board
        self.player = player
        self.move_number = move_number

    def calculate_next_move(self):
        """
        Determines and marks the board for the next turn.

        Returns:
            list: A new board with the new move recorded in the matrix
        """
        if self.player == "O":
            opponent = "X"
        else:
            opponent = "O"

        if self.move_number == 1:
            new_board = self._first_move()
            return new_board, "IN PROGRESS"
        else:
            winner = self.check_win()
            if winner:
                return self.board, f"WINNER: {winner}"
            if self.check_draw():
                return self.board, "DRAW"

            # Check if we're close to winning and take it
            x, y = self.find_near_win(player=self.player)
            if x is not None and y is not None:
                new_board = copy.deepcopy(self.board)
                new_board[x][y] = self.player
                return new_board, "IN PROGRESS"

            # Check if they are close to winning and block
            x, y = self.find_near_win(player=opponent)
            if x is not None and y is not None:
                new_board = copy.deepcopy(self.board)
                new_board[x][y] = self.player
                return new_board, "IN PROGRESS"

            new_board = copy.deepcopy(self.board)
            for row in self.board:
                if "" in row:
                    new_board[self.board.index(row)][row.index("")] = self.player
                    return new_board, "IN PROGRESS"
            raise Exception("IM STUCK")

    def check_win(self):
        """ Check for a win condition
        Returns:
            winner (string): The winner ("O" or "X") or "" if no winner yet
        """
        rows = [row for row in self.board]

        diagonals = [[self.board[x][x] for x in range(0, len(self.board))],
                     [self.board[0][2], self.board[1][1], self.board[2][0]]]

        columns = [[self.board[row][column] for row in range(0, len(self.board))]
                   for column in range(0, len(self.board))]

        to_test = [rows, diagonals, columns]

        for direction in to_test:
            for element in direction:
                if len(set(element)) == 1:
                    matched = set(element).pop()
                    if matched != "":
                        return matched
        return None

    def check_draw(self):
        """
        Check if the state of the current board is a draw

        Returns:
            bool: True or False
        """
        return all("" not in row for row in self.board)

    def _first_move(self):
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


        Returns:
            list: A new board with the new move recorded in the matrix

        """

        # If the opponent hasn't taken the middle, do so
        if self.board[1][1] == "":
            new_board = copy.deepcopy(self.board)
            new_board[1][1] = "X"
            return new_board
        elif self.board[1][1] == "O":
            # If they had taken the center, pick the first corner
            new_board = copy.deepcopy(self.board)
            new_board[0][0] = "X"
            return new_board

        new_board = self._check_edges()
        if new_board:
            return new_board

    def _check_edges(self):
        """
        If an opponent has taken an edge, return the new board with your counter

        Returns:
            The new board if the opponent has taken an edge, None otherwise
        """
        # If the opponent has taken an edge, take the far corner from that edge
        row1_edges = [self.board[0][1]]
        row2_edges = [self.board[1][0], self.board[1][2]]
        row3_edges = [self.board[2][1]]

        to_check = [row1_edges, row2_edges, row3_edges]
        if not any("O" in edges for edges in to_check):
            return None

        new_board = copy.deepcopy(self.board)
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

    def find_near_win(self, player):
        """
        Find out if the given player can win with one move based on the state of the board
        Returns:
             tuple(int, int): the position to take for the winning move
        """
        rows = [row for row in self.board]

        diagonals = [[self.board[x][x] for x in range(0, len(self.board))],
                     [self.board[0][2], self.board[1][1], self.board[2][0]]]

        columns = [[self.board[row][column] for row in range(0, len(self.board))]
                   for column in range(0, len(self.board))]

        x, y = self._find_row_win(rows, player)
        if x is not None and y is not None:
            return x, y

        x, y = self._find_column_win(columns, player)
        if x is not None and y is not None:
            return x, y

        x, y = self._find_diagonal_win(diagonals, player)
        if x is not None and y is not None:
            return x, y

        return None, None

    @staticmethod
    def _find_row_win(rows, player):
        for row in rows:
            if "" in row:
                if row.count(player) == 2:
                    return rows.index(row), row.index("")
        return None, None

    @staticmethod
    def _find_column_win(columns, player):
        for col in columns:
            if "" in col:
                if col.count(player) == 2:
                    return col.index(""), columns.index(col)
        return None, None

    @staticmethod
    def _find_diagonal_win(diagonals, player):
        for diag in diagonals:
            if "" in diag:
                if diag.count(player) == 2:
                    if diagonals.index(diag) == 0:
                        return diag.index(""), diag.index("")
                    else:
                        if diag.index("") == 0:
                            return 0, 2
                        elif diag.index("") == 1:
                            return 1, 1
                        elif diag.index("") == 2:
                            return 2, 0

        return None, None
