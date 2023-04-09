import json


def save_game(character: dict, board: dict) -> None:
    """
    Save character and board state as an external JSON-formatted .save file in the savegame folder.

    :param character: a dictionary representing the character's current status
    :param board: a dictionary representing a coordinate-based game board
    :precondition: character must be a dictionary
    :precondition: character must be a dictionary containing an "X-coordinate" key associated with an integer
    :precondition: character must be a dictionary containing a "Y-coordinate" key associated with an integer
    :precondition: board must be a dictionary containing tuples of two positive integers as keys and strings as values
    :precondition: board must have zero or more resource tiles marked with cyan "['L']" as its coordinate's value
    :precondition: board must have zero or more resource tiles marked with red "['E']" as its coordinate's value
    :postcondition: saves character state and location of resources as a JSON-formatted file
    :postcondition: creates or overwrites file at savegame/{character_name}.save
    :postcondition: prints an informative message if game state is successfully saved
    """
    character_name = character["Name"]
    character_data = character
    board_resources = [coordinate for coordinate, space in board.items() if space == "[\x1b[36m'L'\x1b[0m]"]
    board_bosses = [coordinate for coordinate, space in board.items() if space == "[\x1b[31m'E'\x1b[0m]"]
    board_data = {"rows": max(coordinates[0] for coordinates in board.keys()) + 1,
                  "columns": max(coordinates[1] for coordinates in board.keys()) + 1,
                  "resource": board_resources,
                  "boss": board_bosses}

    save_data = {"character": character_data, "board": board_data}

    with open(f"savegames/{character_name}.save", "w") as save_file:
        json.dump(save_data, save_file)

    print(f"Game successfully saved.")


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
