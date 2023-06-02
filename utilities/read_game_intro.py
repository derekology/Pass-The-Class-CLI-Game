from time import sleep


def read_game_intro(filename: str) -> None:
    """
    Print each line of a plain text file with a two-second delay and line break between each.

    :param filename: a string representing the name of a plain text file
    :precondition: filename must be a string
    :precondition: filename must point to an existing plain text file
    :postcondition: prints each line of the specified file with a two-second delay and line break between each
    :raises FileNotFoundError: if file represented by filename does not exist
    """
    with open(file=filename, mode="r") as file_object:
        for line in file_object:
            print(f"\n{line}", end="")
            sleep(2)


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
