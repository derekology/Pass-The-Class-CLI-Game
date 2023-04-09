"""
Derek Woo
A01351415
"""
from character_management import MIN_CHARACTER_NAME_LENGTH, MIN_REESES


def make_character() -> dict:
    """
    Create a new default character at the origin coordinates.

    :postcondition: asks the user to input a name for their character
    :postcondition: creates a character at the origin and with the default skill attributes
    :return: a level 1 character as a dictionary at coordinates (0, 0) with 5 reeses points, 1 Luck point,
             and 1 Smarts point
    """
    char_name = input("What should your character's name be?: ")

    while len(char_name) == MIN_CHARACTER_NAME_LENGTH:
        char_name = input("Name cannot be blank. Try again: ")

    return {"Name": char_name, "X-coordinate": 0, "Y-coordinate": 0, "Reeses": 5,
            "Luck": 1, "Smarts": 1, "Level": 1}


def is_alive(character: dict, alive_message=None, not_alive_message=None) -> bool:
    """
    Check whether the character is still alive.

    :param character: a dictionary representing the character's current status
    :param alive_message: optional string representing a message to be printed if character is still alive
    :param not_alive_message: optional string representing a message to be printed if character is not alive
    :precondition: character must contain a "Reeses" key associated with an integer greater than or equal to zero
    :precondition: alive_message must be a non-empty string
    :precondition: not_alive_message must be a non-empty string
    :postcondition: checks whether the character has reeses points remaining
    :return: whether the character's current number of reeses points is greater than zero as a boolean
    :raises ValueError: if alive_message is present but is an empty string or not a string
    :raises ValueError: if not_alive_message is present but is an empty string or not a string

    >>> test_character = {"Reeses": 5}
    >>> is_alive(character=test_character)
    True
    >>> test_character = {"Reeses": 0}
    >>> is_alive(character=test_character)
    False
    >>> test_character = {"Reeses": -5}
    >>> is_alive(character=test_character)
    False
    """
    if alive_message and (type(alive_message) is not str or len(alive_message) == 0):
        raise ValueError("alive_message must be a non-empty string.")

    elif not_alive_message and (type(not_alive_message) is not str or len(not_alive_message) == 0):
        raise ValueError("not_alive_message must be a non-empty string.")

    else:
        if character["Reeses"] > MIN_REESES:
            print(alive_message) if alive_message else None
            return True

        else:
            print(not_alive_message) if not_alive_message else None
            return False


def print_character_stats(character: dict) -> None:
    """
    Print character name, current reeses, smarts, and luck.

    :param character: a dictionary representing the character's current status
    :precondition: character must contain a "Name" key associated with a non-empty string
    :precondition: character must contain a "Level" key associated with an integer greater than or equal to zero
    :precondition: character must contain a "Reeses" key associated with an integer greater than or equal to zero
    :precondition: character must contain a "Smarts" key associated with an integer greater than or equal to zero
    :precondition: character must contain a "Luck" key associated with an integer greater than or equal to zero
    :postcondition: prints character's name, reeses points, smarts, and luck attributes
    :raises KeyError: if character dictionary does not contain a "Name" key
    :raises KeyError: if character dictionary does not contain a "Level" key
    :raises KeyError: if character dictionary does not contain a "Reeses" key
    :raises KeyError: if character dictionary does not contain a "Smarts" key
    :raises KeyError: if character dictionary does not contain a "Luck" key
    :raises TypeError: if character dictionary's "Name" value is not a non-empty string
    :raises ValueError: if character dictionary's "Level" value is not positive nonzero integer
    :raises ValueError: if character dictionary's "Reeses" value is not positive nonzero integer
    :raises ValueError: if character dictionary's "Smarts" value is not positive nonzero integer
    :raises ValueError: if character dictionary's "Luck" value is not positive nonzero integer
    """
    if type(character) is not dict:
        raise TypeError("Character must be a dictionary.")

    elif [key for key in ["Name", "Level", "Reeses", "Smarts", "Luck"] if key not in character.keys()]:
        raise KeyError("Character dictionary must contain 'Reeses', 'Smarts', and 'Luck' keys")

    elif type(character["Name"]) is not str or len(character["Name"]) == 0:
        raise TypeError("Character name must be a non-empty string.")

    elif [value for key, value in character.items() if key in ["Level", "Reeses", "Smarts", "Luck"]
            and (type(value) is not int or value < 0)]:
        raise ValueError("Character Level, Reeses, Smarts, and Luck must be integers greater than or equal to zero")

    else:
        print(f"{character['Name']} (Level {character['Level']})\nReeses: {character['Reeses']}\n"
              f"Smarts: {character['Smarts']}\nLuck:{character['Luck']}")


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
