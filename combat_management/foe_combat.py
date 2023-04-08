"""
Derek Woo
A01351415
"""


import random
import itertools
from playsound import playsound
from character_management.manage_character import is_alive
from character_management import MIN_HEALTH


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
    :precondition: character must contain a "Name" key associated with an integer greater than or equal to zero
    :precondition: character must contain a "Current HP" key associated with an integer greater than or equal to zero
    :precondition: character must contain a "Strength" key associated with an integer greater than or equal to zero
    :precondition: character must contain a "Luck" key associated with an integer greater than or equal to zero
    :precondition: foe must be a dictionary
    :precondition: foe must contain a "Current HP" key associated with an integer
    :precondition: foe must contain a "Strength" key associated with an integer greater than or equal to zero
    :precondition: foe must contain a "Luck" key associated with an integer greater than or equal to zero
    :postcondition: alternates combat rounds between character and foe, reducing damage as calculated until either dies
    :return: whether the character is still alive as a boolean
    :raises TypeError: if character is not a dictionary
    :raises KeyError: if character dictionary does not contain "Name", "Current HP", "Strength" or "Luck" key
    :raises ValueError: if character "Current HP", "Strength" or "Luck" values are not positive nonzero integers
    :raises TypeError: if foe is not a dictionary
    :raises KeyError: if foe dictionary does not contain "Current HP", "Strength" or "Luck" key, or both
    :raises ValueError: if foe "Current HP", "Strength" or "Luck" values are not positive nonzero integers
    """
    keys_needed = ["Current HP", "Strength", "Luck"]

    if type(character) is not dict or type(foe) is not dict:
        raise TypeError("Character and foe both must be a dictionaries.")

    elif [value for key, value in character.items() if key in keys_needed and (type(value) is not int or value < 0)]\
            or [value for key, value in foe.items() if key in keys_needed and (type(value) is not int or value < 0)]:
        raise ValueError("'Current HP', 'Strength' and 'Luck' values must be positive nonzero integers.")

    else:
        belligerents = (character, foe)
        switch_turns = itertools.cycle((0, 1))

        while character["Current HP"] > MIN_HEALTH and foe["Current HP"] > MIN_HEALTH:
            current = belligerents[current_turn := next(switch_turns)]
            opposing = belligerents[(current_turn + 1) % 2]

            opposing["Current HP"] = opposing["Current HP"] - (damage_amount := calculate_damage(current))

            def print_round_results(opponent_turn: int, fighter: dict, opponent: dict, damage: int) -> None:
                """
                Print results of combat round.

                :postcondition: prints the amount of damage inflicted by fighter to opponent
                :postcondition: plays combat sound effect after each round
                :postcondition: prints the amount of health character has left if opponent is character
                """
                if not opponent_turn:
                    print(f"You complete {damage} questions on the {opponent['Name']}.\n")
                    playsound("wri.wav")

                else:
                    print(f"You eat {damage} pieces of Reeses Pieces due to stress from the {fighter['Name']}.")
                    print(f"You have {opponent['Current HP']} Reeses Pieces left.\n")
                    playsound("eat.wav")

            print_round_results(opponent_turn=current_turn, fighter=current, opponent=opposing, damage=damage_amount)

        return is_alive(character=character, alive_message=f"You passed the {foe['Name']}!\n")


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
