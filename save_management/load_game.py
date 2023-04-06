import json
import pathlib


def load_game() -> tuple:
    """
    Load a saved game file.

    :return: the character and board save state as a tuple
    """
    character_name = input("What is your character name?: ")

    while not pathlib.Path(f"savegames/{character_name}.save").is_file():
        character_name = input("Save not found. What is your saved character's name?: ")

    with open(f"savegames/{character_name}.save", "r") as save_file:
        data = save_file.read()

    loaded_data = json.loads(data)

    save_state = (loaded_data["character"], loaded_data["board"]["rows"],
                  loaded_data["board"]["columns"], loaded_data["board"]["resource"])

    return save_state


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
