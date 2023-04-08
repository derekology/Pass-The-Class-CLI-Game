"""
Derek Woo
A01351415
"""


import random
import itertools
from time import sleep
from character_management.manage_character import is_alive
from character_management import MIN_HEALTH
from combat_management import TIME_BETWEEN_COMBAT


def calculate_damage(fighter: dict) -> int:
    """
    Calculate the amount of damage dealt in one combat turn.

    :param fighter: a dictionary representing the character's status
    :precondition: fighter must be a dictionary
    :precondition: fighter must contain a "Strength" key associated with an integer greater than or equal to zero
    :precondition: fighter must contain a "Luck" key associated with an integer greater than or equal to zero
    :postcondition: calculates the amount of damage dealt in one turn as a function of fighter's strength and luck
    :return: the amount of damage dealt in one combat turn as an integer
    :raises TypeError: if fighter is not a dictionary
    :raises KeyError: if fighter dictionary does not contain "Strength" or "Luck" key, or both
    :raises ValueError: if fighter "Strength" or "Luck" values are not positive nonzero integers
    """
    if type(fighter) is not dict:
        raise TypeError("Fighter must be a dictionary.")

    elif [key for key in ["Strength", "Luck"] if key not in fighter.keys()]:
        raise KeyError("Fighter dictionary must contain 'Strength', and 'Luck' keys")

    elif [value for key, value in fighter.items() if key in ["Strength", "Luck"]
            and (type(value) is not int or value < 0)]:
        raise ValueError("Fighter 'Strength' and 'Luck' values must be integers greater than or equal to zero")

    else:
        raw_damage = int(fighter["Strength"] * 0.8 + random.randint(0, fighter["Luck"]) * 0.6)

        return max(0, raw_damage)


def fight_foe(character: dict, foe: dict) -> bool:
    """
    Initiate and complete a fight with a given foe.

    :param character: a dictionary representing the character's current status
    :param foe: a dictionary representing the foe's current status
    :precondition: character must be a dictionary
    :precondition: character must contain a "Current HP" key associated with an integer greater than or equal to zero
    :precondition: character must contain a "Strength" key associated with an integer greater than or equal to zero
    :precondition: character must contain a "Luck" key associated with an integer greater than or equal to zero
    :precondition: foe must be a dictionary
    :precondition: foe dictionary must contain a "Current HP" key associated with an integer
    :precondition: foe must contain a "Strength" key associated with an integer greater than or equal to zero
    :precondition: foe must contain a "Luck" key associated with an integer greater than or equal to zero
    :postcondition: alternates combat rounds between character and foe, reducing damage as calculated until either dies
    :return: whether the character is still alive as a boolean
    """
    belligerents = (character, foe)
    switch_turns = itertools.cycle((0, 1))

    while character["Current HP"] > MIN_HEALTH and foe["Current HP"] > MIN_HEALTH:
        current_turn = next(switch_turns)

        current_fighter = belligerents[current_turn]
        opposing_fighter = belligerents[(current_turn + 1) % 2]

        damage = calculate_damage(current_fighter)
        opposing_fighter["Current HP"] -= damage

        if not current_turn:
            print(f"You inflicted {damage} damage to {opposing_fighter['Name']}.\n")

        else:
            print(f"{current_fighter['Name']} inflicted {damage} damage to {opposing_fighter['Name']}.")
            print(f"You have {opposing_fighter['Current HP']}HP left\n")

        sleep(TIME_BETWEEN_COMBAT)

    return is_alive(character=character, alive_message="You win the fight!\n")


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
