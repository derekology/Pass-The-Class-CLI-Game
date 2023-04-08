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
    Create foe for combat.

    :param character: a dictionary representing the character's current status
    :param boss: a boolean representing whether the foe is a boss
    :precondition: character must be a dictionary
    :precondition: character must contain a "Current HP" key associated with an integer greater than or equal to zero
    :precondition: character must contain a "Strength" key associated with an integer greater than or equal to zero
    :precondition: boss must be a boolean value
    :postcondition: creates a foe for combat based on player health and strength
    :return: a foe for character to fight as a dictionary
    """
    foe_types = ("Goblin", "Elf", "Bear", "Cow", "Unicorn")
    boss = check_for_boss(character=character)

    foe_health = 15 if boss else int(character["Current HP"] + random.random())
    foe_strength = 7 if boss else int(character["Strength"] + random.random())

    foe_type = "Final exam" if boss else random.choice(foe_types)
    foe_luck = random.randint(1, 2)
    foe_level = (foe_health + foe_strength) // 5

    print(foe_health)
    print(foe_strength)

    foe_level = (foe_health + foe_strength) // 5

    foe = {"Name": foe_type, "Current HP": foe_health, "Strength": foe_strength, "Level": foe_level, "Luck": 2}

    return foe


def check_for_boss(character: dict) -> bool:
    """
    Determine whether a foe is a boss-level enemy.

    :param character: a dictionary representing the character's current status
    :precondition: character must be a dictionary
    :precondition: character must contain a "Level" key associated with an integer greater than or equal to zero
    :postcondition: determines whether a foe is a boss-level enemy as a function of the character's level
    :return: whether foe is a boss-level enemy as a boolean
    """
    boss_chance = (random.random() * character["Level"]) ** 2

    return True if boss_chance > 3 else False


def escape_from_foe(character: dict) -> bool:
    """
    Try to escape from a fight.

    :param character: a dictionary representing the character's current status
    :precondition: character must be a dictionary
    :precondition: character must contain a "Luck" key associated with an integer greater than or equal to zero
    :postcondition: determines whether character escapes from foe as a function of character's luck attribute
    :return: whether character escapes from foe as a boolean
    """
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
