"""
Derek Woo
A01351415
"""


import random


def find_special_tiles(board: dict, character: dict, resource_tiles: int = 3) -> None:
    """
    Mark a specified number of random tiles on a game board.

    :param board: a dictionary representing a coordinate-based game board
    :param character: a dictionary representing the character's status
    :param resource_tiles: a positive integer representing the number of resources to create (default is 3)
    :precondition: board must be a dictionary containing tuples of two positive integers as keys and strings as values
    :precondition: character must be a dictionary containing an "X-coordinate" key associated with an integer
    :precondition: character must be a dictionary containing a "Y-coordinate" key associated with an integer
    :precondition: values of "X-coordinate" and "Y-coordinate" keys in character must exist as coordinates in board
    :precondition: special_tiles must be a positive integer greater than or equal to zero
    :precondition: special_tiles must be less than the total number of non-character coordinates on board minus one
    :postcondition: checks if a boss exists on the game board and if so, marks one random coordinate with ['B']
    :postcondition: marks the remaining number of tiles on random non-character coordinates as a resource with ['R']
    :raises TypeError: if either board or character, or both, are not dictionaries
    :raises TypeError: if special_tiles is not an integer
    :raises TypeError: if game board does not contain tuples of two positive integers as keys and strings as values
    :raises KeyError: if character dictionary does not contain 'X-coordinate' or 'Y-coordinate' key, or both
    :raises ValueError: if character's 'X-coordinate' or 'Y-coordinate' is not found on the game board
    :raises ValueError: if special_tiles is less than zero or greater than the number of non-character game tiles
    """
    if type(character["X-coordinate"]) is not int or type(character["Y-coordinate"]) is not int \
            or type(resource_tiles) is not int:
        raise TypeError("Special tiles and Character's 'X-coordinate' and 'Y-coordinate' values must be integers")

    elif character["X-coordinate"] not in [x for (x, _) in board] or \
            character["Y-coordinate"] not in [y for (_, y) in board]:
        raise ValueError("Character's coordinates must be on the game board.")

    game_spaces = [key for key in board.keys() if key != (character['X-coordinate'], character['Y-coordinate'])]

    if resource_tiles < 0 or resource_tiles > len(game_spaces) - 1:
        raise ValueError("Number of special tiles must between zero and the number of non-character game tiles.")

    else:
        if manage_foes.check_for_boss(character=character):
            boss_location = game_spaces.pop(random.randint(0, len(game_spaces) - 1))
            board[boss_location] = "['B']"

        for location in random.sample(game_spaces, k=resource_tiles):
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
    :raises TypeError: if either board or character, or both, are not dictionaries
    :raises TypeError: if game board does not contain tuples of two positive integers as keys and strings as values
    :raises KeyError: if character dictionary does not contain 'X-coordinate' or 'Y-coordinate' key, or both
    :raises ValueError: if character's 'X-coordinate' or 'Y-coordinate' is not found on the game board

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
    if type(board) is not dict or type(character) is not dict:
        raise TypeError("Character and game board must both be dictionaries.")

    elif type(character["X-coordinate"]) is not int or type(character["Y-coordinate"]) is not int:
        raise TypeError("Character's 'X-coordinate' and 'Y-coordinate' values must be integers")

    elif character["X-coordinate"] not in [x for (x, _) in board] or \
            character["Y-coordinate"] not in [y for (_, y) in board]:
        raise ValueError("Character's coordinates must be on the game board.")

    else:
        location = (character["X-coordinate"], character["Y-coordinate"])

        board[location] = "['P']"


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
