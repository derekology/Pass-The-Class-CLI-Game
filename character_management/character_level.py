"""
Derek Woo
A01351415
"""


from character_management import UPGRADE_AMOUNTS
from utilities import try_play_sound


def calculate_character_level(character: dict) -> None:
    """
    Calculate the overall level of a character.

    :param character: a dictionary representing the character's status
    :precondition: character must be a dictionary
    :precondition: character must contain a "Reeses" key associated with an integer greater than or equal to 0
    :precondition: character must contain a "Smarts" key associated with an integer greater than or equal to 0
    :postcondition: creates or updates "Level" key in character dictionary with the character's overall level
    :raises TypeError: if character is not a dictionary
    :raises KeyError: if "Reeses" or "Smarts" key, or both, does not exist in character dictionary

    >>> test_character = {"Reeses": 0, "Smarts": 0}
    >>> calculate_character_level(character=test_character)
    >>> test_character
    {'Reeses': 0, 'Smarts': 0, 'Level': 0}
    >>> test_character = {"Reeses": 5, "Smarts": 10}
    >>> calculate_character_level(character=test_character)
    >>> test_character
    {'Reeses': 5, 'Smarts': 10, 'Level': 3}
    """
    character_level = (character["Reeses"] + character["Smarts"]) // 5

    character["Level"] = character_level


def get_upgrade_choice() -> str:
    """
    Ask user for their choice of upgrade in Reeses, Smarts, or Luck attributes.

    :postcondition: prompts for user's desired upgrade attribute as one of: "Reeses", "Smarts", or "Luck"
    :postcondition: play an audio chime upon prompt
    :postcondition: re-issues prompt if user enters an invalid attribute
    :return: the user's desired upgrade attribute as one of "Reese", "Smarts", or "Luck" as a string
    """
    try_play_sound.try_play_sound(filename="./sounds/res.wav", action="Sound of you finding a study resource")

    user_choice = input(f"Choose one of the following:\n\n"
                        f"(R) Reeses + 3\n(S) Smarts + 1\n(L) Luck + 1\n\nYour choice: ").capitalize()

    while user_choice not in ["Reeses", "Smarts", "Luck", "R", "S", "L"]:
        user_choice = input(f"Unknown choice. Please pick one of: Reeses, Smarts, or Luck: ").capitalize()

    if user_choice in ["Reeses", "R"]:
        return "Reeses"

    elif user_choice in ["Smarts", "S"]:
        return "Smarts"

    else:
        return "Luck"


def apply_resource(character: dict) -> None:
    """
    Apply a resource to upgrade character's selected skill attribute.

    :param character: a dictionary representing the character's status
    :precondition: character must be a dictionary
    :precondition: character must contain a "Reeses" key associated with an integer greater than or equal to zero
    :precondition: character must contain a "Smarts" key associated with an integer greater than or equal to zero
    :precondition: character must contain a "Luck" key associated with an integer greater than or equal to zero
    :postcondition: prompts for user's desired skill attribute as one of "Reeses", "Smarts", or "Luck"
    :postcondition: increases the character's selected skill attribute by specified amount
    :postcondition: plays congratulatory sound after upgrade is applied
    :raises TypeError: if character is not a dictionary
    :raises KeyError: if "Reeses", "Smarts", or "Luck" key does not exist in character dictionary
    :raises ValueError: if " Reeses", "Smarts", or "Luck" value is not an integer greater than or equal to zero
    """
    required_keys = ["Reeses", "Smarts", "Luck"]

    if type(character) is not dict:
        raise TypeError("Character must be a dictionary.")

    elif [key for key in required_keys if key not in character.keys()]:
        raise KeyError("Character dictionary must contain 'Reeses', 'Smarts', and 'Luck' keys")

    elif [value for key, value in character.items() if key in required_keys and (type(value) is not int or value < 0)]:
        raise ValueError("Character Reeses, Smarts, and Luck values must be integers greater than or equal to zero")

    else:
        upgrade_attribute = get_upgrade_choice()
        character[upgrade_attribute] += UPGRADE_AMOUNTS[upgrade_attribute]

        try_play_sound.try_play_sound(filename="./sounds/lev.wav", action="Sound of you upgrading yourself")


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
