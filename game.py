"""
Derek Woo
A01351415
"""


import random
from board_management import manage_board, manage_locations
from character_management import manage_character, character_movement, character_level
from combat_management import manage_foes, foe_combat
from save_management import save_game, load_game
from utilities import try_play_sound, check_for_special_tile, guessing_game, read_game_intro
from utilities import TITLE_SCREEN_ASCII, LOCKER_FOUND_ASCII, YOU_FAILED_ASCII, UPCOMING_DUE_DATE_ASCII, FINAL_ASCII


def game():
    """
    Run the game.
    """
    print(f"\n\n\n{TITLE_SCREEN_ASCII}")

    should_load_game = input(f"\nType 'Y' to load an existing game save (or any other character to continue): ").upper()

    if should_load_game == "Y":
        loaded_data = load_game.load_game()

        while not loaded_data:
            loaded_data = load_game.load_game()

        character = loaded_data[0]
        rows = loaded_data[1]
        columns = loaded_data[2]
        week = loaded_data[5]

        game_board = manage_board.make_board(rows=rows, columns=columns)

        for coordinate in loaded_data[3]:
            game_board[tuple(coordinate)] = "[\x1b[36m'L'\x1b[0m]"

        for coordinate in loaded_data[4]:
            game_board[tuple(coordinate)] = "[\x1b[31m'E'\x1b[0m]"

        print(f"\nSave loaded. Welcome back to Pass the Class, {character['Name']}!")

    else:
        rows = 5
        columns = 5
        week = 0
        game_board = manage_board.make_board(rows=rows, columns=columns)
        character = manage_character.make_character()
        manage_locations.find_special_tiles(board=game_board, character=character)

        try:
            read_game_intro.read_game_intro(filename="utilities/narrative")

        except FileNotFoundError:
            print(f"\nWelcome to Pass the Class!")

    while manage_character.is_alive(character=character):
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

                print(f"\n\n\n{FINAL_ASCII}")
                print(f"You have to complete a {encountered_foe['Name']} to pass "
                      f"the course (Question(s): {encountered_foe['Reeses']})!\n\nNo escaping from this one...\n")

                try_play_sound.try_play_sound(filename="./sounds/boss.wav", action="Ominous sound of an exam")

                if foe_combat.fight_foe(character=character, foe=encountered_foe):
                    print(f"You passed the class! See you in Term 2.")
                    try_play_sound.try_play_sound(filename="./sounds/win.wav", action="Sound of you passing the exam")
                    break

            elif check_for_special_tile.check_for_special_tile(board=game_board, character=character, boss=False):
                print(f"\n\n\n{LOCKER_FOUND_ASCII}")
                print(f"\nYou find a locker! What's the combinations, though?", end=" ")

                if guessing_game.guessing_game():
                    print(f"The locker opens! What would you like to take?", end=" ")
                    character_level.apply_resource(character=character)

                else:
                    print(f"Incorrect combination. The secret is lost forever...")
                    try_play_sound.try_play_sound(filename="./sounds/wrong.wav", action="Sad sound effect")

                game_board[(character["X-coordinate"], character["Y-coordinate"])] = "[   ]"

            elif manage_foes.check_for_foes():
                encountered_foe = manage_foes.create_foe(character=character, boss=False)

                print(f"\n\n\n{UPCOMING_DUE_DATE_ASCII}")
                print(f"You need to finish a {encountered_foe['Name']} (Question(s): {encountered_foe['Reeses']})!\n\n")

                try_to_escape = input(f"Type \"Y\" to try and skip it (or any other character to continue): ").upper()

                if try_to_escape == "Y" and manage_foes.escape_from_foe(character=character):
                    print(f"Your excuse worked and you skip the deliverable! Woo!")
                    try_play_sound.try_play_sound(filename="./sounds/woo.wav", action="Sound of cheering")

                else:
                    print(f"Let's get to it, I guess...\n")

                    if foe_combat.fight_foe(character=character, foe=encountered_foe) and \
                            (random.random() * character["Luck"]) > 0.80:
                        print(f"Your answers were so good, you got a prize! It's not a LEGO though...\n")
                        character_level.apply_resource(character=character)

            else:
                print("\nThings are strangely calm as you go about your day...")

            if [space for space in game_board.values()].count("[\x1b[36m'L'\x1b[0m]") == 0:
                resource_count = max(0, 4 - character["Level"]) + random.randint(1, 2)
                game_board = manage_board.make_board(rows=rows, columns=columns)
                manage_locations.find_special_tiles(board=game_board, character=character,
                                                    resource_tiles=resource_count)
                week += 1

                print(f"\nYou finished a week of classes! Let's enjoy the weekend...")

                should_save_game = input(f"\nType 'Y' to save your game (or any other character to continue): ").upper()
                if should_save_game == "Y":
                    save_game.save_game(character=character, board=game_board, week=week)

                print(f"\nJokes... what is a weekend anyways? Let's move onto week {week}...")

        else:
            print(f"You cannot go that way.")

    else:
        print(f"\n\n\n{YOU_FAILED_ASCII}")
        print(f"You run out of Reeses and pass out mid-semester.\n\nSummer's too hot to spend off campus anyways...")
        try_play_sound.try_play_sound(filename="./sounds/lose.wav", action="Sound of you failing the class")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
