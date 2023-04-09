"""
Derek Woo
A01351415
"""


import random
import utilities
from board_management import manage_board, manage_locations
from character_management import manage_character, character_movement, character_level
from combat_management import manage_foes, foe_combat
from save_management import save_game, load_game
from utilities import try_play_sound, check_for_special_tile, guessing_game, read_game_intro
import inspect


def game():
    """
    Run the game.
    """
    print(f"\n\n\n{utilities.TITLE_SCREEN_ASCII}")

    should_load_game = input("Type 'Y' to load an existing game save (or any other character to continue): ").upper()

    if should_load_game == "Y":
        loaded_data = None

        while not loaded_data:
            loaded_data = load_game.load_game()

            try:
                character = loaded_data[0]
                rows = loaded_data[1]
                columns = loaded_data[2]

            except TypeError:
                print("Unable to load save data. Ensure that your save file is not corrupted.")

            else:
                game_board = manage_board.make_board(rows=rows, columns=columns)

                for coordinate in loaded_data[3]:
                    game_board[tuple(coordinate)] = "[\x1b[36m'L'\x1b[0m]"

                for coordinate in loaded_data[4]:
                    game_board[tuple(coordinate)] = "[\x1b[31m'E'\x1b[0m]"

                print(f"Save loaded. Welcome back to Pass the Class, {character['Name']}!")

    else:
        rows = 5
        columns = 5
        game_board = manage_board.make_board(rows=rows, columns=columns)
        character = manage_character.make_character()
        manage_locations.find_special_tiles(board=game_board, character=character)

        try:
            read_game_intro.read_game_intro(filename="utilities/narrative")

        except FileNotFoundError:
            print(f"\nWelcome to Pass the Class!")

    while manage_character.is_alive(character=character):
        if check_for_special_tile.check_for_special_tile(board=game_board, character=character, boss=False):
            print(f"\n\n\n{utilities.LOCKER_FOUND_ASCII}")
            print(f"\nYou find a locker! What's the combinations, though?", end=" ")
            if guessing_game.guessing_game():
                print(f"The locker opens! What would you like to take?", end=" ")
                try_play_sound.try_play_sound(filename="./sounds/res.wav",
                                              action="Sound of you finding a study resource")
                character_level.apply_resource(character=character)
                try_play_sound.try_play_sound(filename="./sounds/lev.wav",
                                              action="Sound of you upgrading yourself")

            else:
                print(f"Incorrect combination. The secret is lost forever...")
                try_play_sound.try_play_sound(filename="./sounds/wrong.wav", action="Sad sound effect")

            game_board[(character["X-coordinate"], character["Y-coordinate"])] = "[   ]"

        if [space for space in game_board.values()].count("['L']") == 0:
            resource_count = max(0, 4 - character["Level"]) + random.randint(1, 2)
            game_board = manage_board.make_board(rows=rows, columns=columns)
            manage_locations.find_special_tiles(board=game_board, character=character, resource_tiles=resource_count)

            print(f"You finished a week of CST! Let's enjoy the weekend...")

            should_save_game = input("Type 'Y' to save your game (or any other character to continue): ").upper()
            if should_save_game == "Y":
                save_game.save_game(character=character, board=game_board)

            print(f"Jokes... what is a weekend anyways? Let's move onto the next week...")

        character_level.calculate_character_level(character=character)
        manage_locations.locate_character(board=game_board, character=character)
        print(f"\n\n\n")
        manage_board.draw_board(board=game_board, columns=columns)
        print(f"")
        manage_character.print_character_stats(character=character)

        direction = character_movement.get_user_choice()
        valid_move = character_movement.validate_move(board=game_board, character=character, direction=direction)

        if valid_move:
            game_board[(character["X-coordinate"], character["Y-coordinate"])] = "[   ]"
            character_movement.move_character(character=character, direction=direction)

            if check_for_special_tile.check_for_special_tile(board=game_board, character=character, boss=True):
                encountered_foe = manage_foes.create_foe(character=character, boss=True)
                print(f"\n\n\n{utilities.FINAL_EXAM_ASCII}")
                print(f"You (level {character['Level']}) have to complete a {encountered_foe['Name']} to pass "
                      f"the course (Difficulty level: {encountered_foe['Level']})!\n\n")

                try_play_sound.try_play_sound(filename="./sounds/boss.wav", action="Ominous sound of a final exam")

                if foe_combat.fight_foe(character=character, foe=encountered_foe):
                    print(f"You passed the class! See you in Term 2.")
                    try_play_sound.try_play_sound(filename="./sounds/win.wav",
                                                  action="Sound of you passing the Final exam")
                    break

            if manage_foes.check_for_foes():
                encountered_foe = manage_foes.create_foe(character=character, boss=False)
                print(f"\n\n\n{utilities.UPCOMING_DUE_DATE_ASCII}")
                print(f"You (level {character['Level']}) need to finish a {encountered_foe['Name']} "
                      f"(Difficulty level: {encountered_foe['Level']})!\n\n")

                try_to_escape = input(f"Type \"Y\" to make up an excuse to skip it "
                                      f"(or any other character to continue): ").upper()
                if try_to_escape == "Y" and manage_foes.escape_from_foe(character=character):
                    print(f"Your excused worked! Woo!")
                    try_play_sound.try_play_sound(filename="./sounds/woo.wav",
                                                  action="Sound of cheering")

                else:
                    print(f"Let's get to it, I guess...\n")
                    if foe_combat.fight_foe(character=character, foe=encountered_foe) and \
                            (random.random() * character["Luck"]) > 0.80:
                        print(f"Your answers were so good, you deserve a treat!", end=" ")
                        try_play_sound.try_play_sound(filename="./sounds/res.wav",
                                                      action="Sound of you finding a study resource")
                        character_level.apply_resource(character=character)
                        try_play_sound.try_play_sound(filename="./sounds/lev.wav",
                                                      action="Sound of you upgrading yourself")
                        print(f"end of combat: {[x[3] for x in inspect.stack()]}")

            print(f"end of loop: {[x[3] for x in inspect.stack()]}")

        else:
            print(f"You cannot go that way.")

    else:
        print(f"\n\n\n{utilities.YOU_FAILED_ASCII}")
        print(f"You run out of Reeses and pass out, not completing the class.\n\n"
              f"Summer's too hot to spend outside the classroom anyways...")
        try_play_sound.try_play_sound(filename="./sounds/lose.wav", action="Sound of you failing the class")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
