"""
Derek Woo
A01351415
"""


import random


def check_for_foes() -> bool:
    """
    Check whether a foe has been encountered.

    :postcondition: determines whether a foe has been encountered randomly at a 25% chance
    :return: whether a foe has been encountered as a boolean
    """
    chance = random.randint(1, 4)

    if chance == 1:
        return True

    else:
        return False


def create_foe(character: dict, boss: bool = False) -> dict:
    """
    Create foe for combat based on player character attributes.

    :param character: a dictionary representing the character's current status
    :param boss: a boolean representing whether the foe is a boss
    :precondition: character must be a dictionary
    :precondition: character must contain a "Current HP" key associated with an integer greater than or equal to zero
    :precondition: character must contain a "Strength" key associated with an integer greater than or equal to zero
    :precondition: boss must be a boolean value
    :postcondition: creates a foe for combat based on player health and strength
    :return: a foe for character to fight as a dictionary
    :raises TypeError: if character is not a dictionary or boss is not a boolean
    :raises KeyError: if character dictionary does not contain "Current HP" or "Strength" key, or both
    :raises ValueError: if character dictionary's "Current HP" value is not an integer greater than or equal to zero
    :raises ValueError: if character dictionary's "Strength" value is not an integer greater than or equal to zero
    """
    keys_needed = ["Current HP", "Strength"]

    if type(character) is not dict or type(boss) is not bool:
        raise TypeError("Character and foe both must be a dictionaries.")

    elif [val for key, val in character.items() if key in keys_needed and (type(val) is not int or val < 0)]:
        raise ValueError("'Current HP', 'Strength' and 'Luck' values must be positive nonzero integers.")

    foe_types = ("pop quiz", "assignment", "lab", "hand-in template", "solo quiz", "partner quiz", "lecture demo")

    foe_health = 15 if boss else int(character["Current HP"] + random.random())
    foe_strength = 7 if boss else int(character["Strength"] + random.random())

    foe_type = "Final exam" if boss else random.choice(foe_types)
    foe_luck = random.randint(1, 2)
    foe_level = (foe_health + foe_strength) // 5

    print(foe_health)
    print(foe_strength)

    return {"Name": foe_type, "Current HP": foe_health, "Strength": foe_strength, "Level": foe_level, "Luck": foe_luck}


def check_for_boss(character: dict) -> bool:
    """
    Determine whether a foe is a boss-level enemy.

    :param character: a dictionary representing the character's current status
    :precondition: character must be a dictionary
    :precondition: character must contain a "Level" key associated with an integer greater than or equal to zero
    :postcondition: determines whether a foe is a boss-level enemy as a function of the character's level
    :return: whether foe is a boss-level enemy as a boolean
    :raises TypeError: if character is not a dictionary
    :raises KeyError: if character dictionary does not contain a 'Level' key
    :raises ValueError: if character dictionary 'Level' value is not an integer greater than or equal to zero
    """
    if type(character) is not dict:
        raise TypeError("Character must be a dictionary.")

    elif "Level" not in character.keys():
        raise KeyError("Character dictionary must contain 'Level' key")

    elif type(character["Level"]) is not int or character["Level"] < 0:
        raise ValueError("Character's level must be an integer greater than or equal to zero.")

    boss_chance = (random.random() * character["Level"]) * 3

    return boss_chance > 3


def escape_from_foe(character: dict) -> bool:
    """
    Try to escape from a fight.

    :param character: a dictionary representing the character's current status
    :precondition: character must be a dictionary
    :precondition: character must contain a "Luck" key associated with an integer greater than or equal to zero
    :postcondition: determines whether character escapes from foe as a function of character's luck attribute
    :return: whether character escapes from foe as a boolean
    :raises TypeError: if character is not a dictionary
    :raises KeyError: if character dictionary does not contain a 'Luck' key
    :raises ValueError: if character dictionary 'Luck' value is not an integer greater than or equal to zero
    """
    if type(character) is not dict:
        raise TypeError("Character must be a dictionary.")

    elif "Luck" not in character.keys():
        raise KeyError("Character dictionary must contain 'Luck' key")

    elif type(character["Luck"]) is not int or character["Luck"] < 0:
        raise ValueError("Character's luck must be an integer greater than or equal to zero.")

    chance = random.random()

    if chance <= 0.1 * character["Luck"]:
        return True

    else:
        return False


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
