"""
Derek Woo
A01351415
"""


import random


def mark_resources(board: dict, character: dict, special_tiles: int = 3) -> None:
    """
    Mark a specified number of tiles on a game board.

    :param board: a dictionary representing a coordinate-based game board
    :param character: a dictionary representing the character's status
    :param special_tiles: a positive integer representing the number of resources to create (default is 3)
    :precondition: board must be a dictionary containing tuples of two positive integers as keys and strings as values
    :precondition: character must be a dictionary containing an "X-coordinate" key associated with an integer
    :precondition: character must be a dictionary containing a "Y-coordinate" key associated with an integer
    :precondition: values of "X-coordinate" and "Y-coordinate" keys in character must exist as coordinates in board
    :precondition: special_tiles must be a positive integer greater than or equal to zero
    :precondition: special_tiles must be less than the total number of coordinates on board
    :postcondition: marks the specified number of tiles on random non-character coordinates of a game board with "['R']"
    """
    game_spaces = [space for space in board.keys()]
    game_spaces.remove((character['X-coordinate'], character['Y-coordinate']))

    resource_locations = random.sample(game_spaces, k=special_tiles)

    for location in resource_locations:
        board[location] = "['R']"


def locate_character(board: dict, character: dict) -> None:
    """
    Mark the location of a character on a game board.

    :param board: a dictionary representing a coordinate-based game board
    :param character: a dictionary representing the character's status
    :precondition: board must be a dictionary containing tuples of two positive integers as keys and strings as values
    :precondition: character must be a dictionary containing an "X-coordinate" key associated with an integer
    :precondition: character must be a dictionary containing a "Y-coordinate" key associated with an integer
    :precondition: values of "X-coordinate" and "Y-coordinate" keys in character must exist as coordinates in board
    :postcondition: updates the value of the character's game board coordinates key to ['P']

    >>> test_board = {(0, 0): "[   ]", (1, 0): "[   ]"}
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> locate_character(board=test_board, character=test_character)
    >>> test_board
    {(0, 0): "['P']", (1, 0): '[   ]'}
    >>> test_board = {(0, 0): "[   ]", (1, 0): "[   ]"}
    >>> test_character = {"X-coordinate": 1, "Y-coordinate": 0}
    >>> locate_character(board=test_board, character=test_character)
    >>> test_board
    {(0, 0): '[   ]', (1, 0): "['P']"}
    """
    location = (character["X-coordinate"], character["Y-coordinate"])

    board[location] = "['P']"


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
