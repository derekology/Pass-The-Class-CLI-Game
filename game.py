"""
Derek Woo
A01351415
"""


import random
from board_management import manage_board
from board_management import manage_locations
from character_management import manage_character
from character_management import character_movement
from character_management import character_level
from combat_management import manage_foes
from combat_management import foe_combat
from save_management import load_game
from save_management import save_game
import inspect


def game():
    """
    Run the game.
    """
    if input("Type 'Y' to load an existing game save: ").upper() == "Y":
        loaded_data = load_game.load_game()

        character = loaded_data[0]

        rows = loaded_data[1]
        columns = loaded_data[2]
        game_board = manage_board.make_board(rows=rows, columns=columns)

        for coordinate in loaded_data[3]:
            game_board[tuple(coordinate)] = "['R']"

        print(f"Welcome back to my game, {character['Name']}")

    else:
        rows = 5
        columns = 5
        game_board = manage_board.make_board(rows=rows, columns=columns)
        character = manage_character.make_character()
        manage_locations.mark_resources(board=game_board, character=character)

        print(f"Welcome to my game, {character['Name']}")

    while manage_character.is_alive(character=character):
        if character_level.check_for_resources(board=game_board, character=character):
            character_level.apply_resource(character=character)
            game_board[(character["X-coordinate"], character["Y-coordinate"])] = "[   ]"

        if [space for space in game_board.values()].count("['R']") == 0:
            print("Finding more resources...")
            resource_count = max(0, 4 - character["Level"]) + random.randint(1, 2)
            manage_locations.mark_resources(board=game_board, character=character, special_tiles=resource_count)

            save = input("Type 'Y' to save your game: ").upper()
            if save == "Y":
                save_game.save_game(character=character, board=game_board)

        character_level.calculate_character_level(character=character)
        manage_locations.locate_character(board=game_board, character=character)
        manage_board.draw_board(board=game_board, columns=columns)
        print(f"{character['Name']} (Level {character['Level']})\nHealth: {character['Current HP']}")

        direction = character_movement.get_user_choice()
        valid_move = character_movement.validate_move(board=game_board, character=character, direction=direction)

        if valid_move:
            game_board[(character["X-coordinate"], character["Y-coordinate"])] = "[   ]"
            character_movement.move_character(character=character, direction=direction)

            if manage_foes.check_for_foes():
                encountered_foe = manage_foes.create_foe(character=character)
                print(f"You (level {character['Level']}) encountered a {encountered_foe['Name']} "
                      f"(level {encountered_foe['Level']})! ")

                if input(f"Type \"Y\" to try to flee: ").upper() == "Y"\
                        and manage_foes.escape_from_foe(character=character):
                    print("You've successfully escaped!")

                else:
                    print("Fight initiated!\n")
                    if foe_combat.fight_foe(character=character, foe=encountered_foe) and \
                            (random.random() * character["Luck"]) > 0.80:
                        character_level.apply_resource(character=character)
                        print(f"end of combat: {[x[3] for x in inspect.stack()]}")

            print(f"end of loop: {[x[3] for x in inspect.stack()]}")

        else:
            print("You cannot go that way.")

    else:
        print("You died... restart the game to try again.")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
