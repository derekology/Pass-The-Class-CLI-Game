def check_for_special_tile(board: dict, character: dict, boss: bool = False) -> bool:
    """
    Check if character's current location contains a resource.

    :param board: a dictionary representing a coordinate-based game board
    :param character: a dictionary representing the character's status
    :param boss: a boolean value representing whether to search for a boss tile (default is False)
    :precondition: board must be a dictionary containing tuples of two positive integers as keys and strings as values
    :precondition: character must be a dictionary containing an "X-coordinate" key associated with an integer
    :precondition: character must be a dictionary containing a "Y-coordinate" key associated with an integer
    :precondition: values of "X-coordinate" and "Y-coordinate" keys in character must exist as coordinates in board
    :precondition: boss must be a boolean value
    :postcondition: verifies whether the current coordinate of the character contains a resource tile
    :return: whether the current coordinate of the character contains a resource tile as a boolean
    :raises TypeError: if either board or character, or both, are not dictionaries
    :raises TypeError: if boss is not a boolean value
    :raises TypeError: if game board does not contain tuples of two positive integers as keys and strings as values
    :raises KeyError: if character dictionary does not contain "X-coordinate" or "Y-coordinate" key, or both
    :raises ValueError: if character's "X-coordinate" or "Y-coordinate" is not found on the game board

    >>> test_board = {(0, 0): "[\x1b[36m'L'\x1b[0m]", (1, 0): "[   ]"}
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> check_for_special_tile(board=test_board, character=test_character, boss=False)
    True
    >>> test_board = {(0, 0): "[\x1b[31m'E'\x1b[0m]", (1, 0): "[   ]"}
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> check_for_special_tile(board=test_board, character=test_character, boss=True)
    True
    >>> test_board = {(0, 0): "[   ]", (1, 0): "[\x1b[36m'L'\x1b[0m]"}
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> check_for_special_tile(board=test_board, character=test_character, boss=False)
    False
    """
    if type(board) is not dict or type(character) is not dict:
        raise TypeError("Character and game board must both be dictionaries.")

    elif type(character["X-coordinate"]) is not int or type(character["Y-coordinate"]) is not int:
        raise TypeError("Character's 'X-coordinate' and 'Y-coordinate' values must be integers")

    elif character["X-coordinate"] not in [x for (x, _) in board] or \
            character["Y-coordinate"] not in [y for (_, y) in board]:
        raise ValueError("Character's coordinates must be on the game board.")

    else:
        search_target = "[\x1b[31m'E'\x1b[0m]" if boss else "[\x1b[36m'L'\x1b[0m]"
        character_location = (character["X-coordinate"], character["Y-coordinate"])

        return board[character_location] == search_target


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
