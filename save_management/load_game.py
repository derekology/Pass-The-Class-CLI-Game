import json
import pathlib


def load_game() -> tuple:
    """
    Load a saved game file.

    :postcondition: asks user for name of saved character
    :postcondition: prompts use for another name if save data not found
    :postcondition: opens saved character file and parses data into game variables
    :return: the character and board save state as a tuple
    """
    character_name = input(f"What is your saved character's name?: ")

    while not pathlib.Path(f"savegames/{character_name}.save").is_file():
        character_name = input(f"Save not found. What is your saved character's name?: ")

    with open(f"savegames/{character_name}.save", "r") as save_file:
        data = save_file.read()

    try:
        loaded_data = json.loads(data)

        save_state = (loaded_data["character"], loaded_data["board"]["rows"], loaded_data["board"]["columns"],
                      loaded_data["board"]["resource"], loaded_data["board"]["boss"], loaded_data["week"])

    except ValueError:
        print("Unable to load save data. Please ensure that your file is a Pass the Class save game.")

    except KeyError:
        print("Unable to load save data. Please ensure that your file is not corrupted.")

    else:
        return save_state


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
