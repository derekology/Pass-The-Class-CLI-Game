"""
Derek Woo
A01351415
"""
from character_management import HP_UPGRADE_AMOUNT, STRENGTH_UPGRADE_AMOUNT, LUCK_UPGRADE_AMOUNT


def calculate_character_level(character: dict) -> None:
    """
    Calculate the overall level of a character.

    :param character: a dictionary representing the character's status
    :precondition: character must be a dictionary
    :precondition: character must contain a "Current HP" key associated with an integer greater than or equal to 0
    :precondition: character must contain a "Strength" key associated with an integer greater than or equal to 0
    :postcondition: creates or updates "Level" key in character dictionary with the character's overall level

    >>> test_character = {"Current HP": 0, "Strength": 0}
    >>> calculate_character_level(character=test_character)
    >>> test_character
    {'Current HP': 0, 'Strength': 0, 'Level': 0}
    >>> test_character = {"Current HP": 5, "Strength": 10}
    >>> calculate_character_level(character=test_character)
    >>> test_character
    {'Current HP': 5, 'Strength': 10, 'Level': 3}
    """
    character_level = (character["Current HP"] + character["Strength"]) // 5

    character["Level"] = character_level


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

    >>> test_board = {(0, 0): "['R']", (1, 0): "[   ]"}
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> check_for_resources(board=test_board, character=test_character)
    True
    >>> test_board = {(0, 0): "[   ]", (1, 0): "['R']"}
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> check_for_resources(board=test_board, character=test_character)
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
        search_target = "['B']" if boss else "['R']"
        character_location = (character["X-coordinate"], character["Y-coordinate"])

    return board[character_location] == "['R']"


def apply_resource(character: dict) -> None:
    """
    Apply a resource to upgrade character's selected skill attribute.

    :param character: a dictionary representing the character's status
    :precondition: board must be a dictionary containing tuples of two positive integers as keys and strings as values
    :precondition: character must be a dictionary
    :precondition: character must contain a "Current HP" key associated with an integer greater than or equal to zero
    :precondition: character must contain a "Strength" key associated with an integer greater than or equal to zero
    :precondition: character must contain a "Luck" key associated with an integer greater than or equal to zero
    :postcondition: prompts for user's desired skill attribute as one of "Health", "Strength", or "Luck"
    :postcondition: increases the character's selected skill attribute by specified amount
    """
    user_choice = input(f"You found a resource!\nWhat would you like to it to?\n\n"
                        f"(H) Health + 3\t\t(Current: {character['Current HP']})\n"
                        f"(S) Strength + 1\t(Current: {character['Strength']})\n"
                        f"(L) Luck + 1\t\t(Current: {character['Luck']})\n\n"
                        "Your choice: ").capitalize()

    while user_choice not in ["Health", "Strength", "Luck", "H", "S", "L"]:
        user_choice = input("Unknown attribute. Please pick one of: Health, Strength, or Luck: ").capitalize()

    if user_choice == "Health" or user_choice == "H":
        character["Current HP"] += HP_UPGRADE_AMOUNT

    elif user_choice == "Strength" or user_choice == "S":
        character["Strength"] += STRENGTH_UPGRADE_AMOUNT

    else:
        character["Luck"] += LUCK_UPGRADE_AMOUNT


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
