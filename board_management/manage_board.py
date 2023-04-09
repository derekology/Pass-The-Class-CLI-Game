"""
Derek Woo
A01351415
"""

from board_management import MIN_ROWS, MIN_COLUMNS


def draw_board(board: dict, columns: int) -> None:
    """
    Print an evenly-spaced coordinate-based game board with the specified number of columns.

    :param board: a dictionary representing a coordinate-based game board
    :param columns: an integer representing the number of columns on the board
    :precondition: board must be a dictionary containing tuples of two positive integers as keys and strings as values
    :precondition: columns must be an integer greater than or equal to two
    :postcondition: prints three line breaks, then a game board of values with the specified number of columns
    :raises TypeError: if board is not a dictionary
    :raises TypeError: if columns is not an integer
    :raises TypeError: if game board does not contain tuples of two positive integers as keys and strings as values
    :raises ValueError: columns is not greater than or equal to two

    >>> test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (0, 1): "[   ]", (1, 1): "[   ]"}
    >>> draw_board(board=test_board, columns=2)
    [   ][   ]
    [   ][   ]
    >>> test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (0, 1): "[   ]", (1, 1): "[   ]"}
    >>> draw_board(board=test_board, columns=3)
    [   ][   ][   ]
    [   ]
    >>> test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (0, 1): "[   ]", (1, 1): "[   ]"}
    >>> draw_board(board=test_board, columns=4)
    [   ][   ][   ][   ]
    """
    if type(board) is not dict or type(columns) is not int:
        raise TypeError("Game board must be a dictionary and columns must be an integer")

    elif [value for value in board.values() if type(value) is not str] or \
            [key for key in board.keys() if ((type(key) is not tuple) or (len(key) != 2) or
                                             ([coordinate for coordinate in key if type(coordinate) is not int]))]:
        raise TypeError("Game board must contain tuples of two positive integers as keys and strings as values.")

    elif columns < MIN_COLUMNS:
        raise ValueError(f"Game board must have {MIN_COLUMNS} or more columns.")

    else:
        counter = 0
        game_spaces = [space for space in board.values()]

        for space in game_spaces:
            end_char = '\n' if (counter + 1) % columns == 0 else ''
            print(space, end=end_char)
            counter += 1


def make_board(rows: int = MIN_COLUMNS, columns: int = MIN_COLUMNS) -> dict:
    """
    Generate a coordinate-based game board with of the specified size with assigned room names.

    :param rows: an integer representing the number of rows on the board
    :param columns: an integer representing the number of columns on the board
    :precondition: rows must be an integer greater than or equal to MIN_ROWS
    :precondition: columns must be an integer greater than or equal to MAX_ROWS
    :precondition: rows and columns must be equal
    :postcondition: generates a coordinate-based game board of specified size with room names for each coordinate
    :return: a game board of specified size as a dictionary with coordinates as keys and room name strings as values
    :raises TypeError: if either rows, columns, or both, are not of type integer
    :raises ValueError: if either rows, columns, or both, are less than two

    >>> make_board(rows=2, columns=2)
    {(0, 0): '[   ]', (1, 0): '[   ]', (0, 1): '[   ]', (1, 1): '[   ]'}
    """
    if type(rows) is not int or type(columns) is not int:
        raise TypeError(f"Both rows and columns must be integers.")

    elif rows < MIN_ROWS or columns < MIN_COLUMNS:
        raise ValueError(f"Board must have at least {MIN_ROWS} rows and {MIN_COLUMNS} columns.")

    elif rows != columns:
        raise ValueError(f"Number of rows and columns must be equal.")

    else:
        game_board = {(x, y): "[   ]" for y in range(columns) for x in range(rows)}

    return game_board


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
