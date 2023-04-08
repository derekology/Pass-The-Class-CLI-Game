"""
Derek Woo
A01351415
"""
from character_management import MIN_CHARACTER_NAME_LENGTH, MIN_HEALTH


def make_character() -> dict:
    """
    Create a new default character at the origin coordinates.

    :postcondition: asks the user to input a name for their character
    :postcondition: creates a character at the origin and with the default skill attributes
    :return: a level 1 character as a dictionary at coordinates (0, 0) with 5 health points, 1 Luck point,
             and 1 Strength point
    """
    char_name = input("What should your character's name be?: ")

    while len(char_name) == MIN_CHARACTER_NAME_LENGTH:
        char_name = input("Name cannot be blank. Try again: ")

    return {"Name": char_name, "X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5,
            "Luck": 1, "Strength": 1, "Level": 1}


def is_alive(character: dict, alive_message=None, not_alive_message=None) -> bool:
    """
    Check whether the character is still alive.

    :param character: a dictionary representing the character's current status
    :param alive_message: optional string representing a message to be printed if character is still alive
    :param not_alive_message: optional string representing a message to be printed if character is not alive
    :precondition: character must contain a "Current HP" key associated with an integer greater than or equal to zero
    :precondition: alive_message must be a nonempty string
    :precondition: not_alive_message must be a nonempty string
    :postcondition: checks whether the character has health points remaining
    :return: whether the character's current number of health points is greater than zero as a boolean

    >>> test_character = {"Current HP": 5}
    >>> is_alive(character=test_character)
    True
    >>> test_character = {"Current HP": 0}
    >>> is_alive(character=test_character)
    False
    >>> test_character = {"Current HP": -5}
    >>> is_alive(character=test_character)
    False
    """
    if character["Current HP"] > MIN_HEALTH:
        print(alive_message)
        return True

    else:
        print(not_alive_message)
        return False


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
