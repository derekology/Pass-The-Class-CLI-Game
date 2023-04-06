"""
Derek Woo
A01351415
"""
from character_management import COORDINATE_CHANGE


def get_user_choice() -> str:
    """
    Capture the user's desired travel direction.

    A function that prompts the user to enter a direction and captures their input.

    :postcondition: prompts for user's desired travel direction as one of: "Up", "Right", "Down" or "Left"
    :postcondition: prints an informative message and re-issues prompt if user enters an invalid direction
    :return: the user's desired travel direction as a string
    """
    directions = {"W": "Up", "A": "Left", "S": "Down", "D": "Right"}

    next_movement = input("\nWhich direction would you like to travel in?\n(W) Up\n"
                          "(A) Left\n(S) Down\n(D) Right\n\n"
                          "Choose a direction: ").upper()

    while next_movement not in ["W", "A", "S", "D"]:
        print("Invalid direction entered.", end=" ")

        next_movement = input("\nWhich direction would you like to travel in?\n(W) Up\n"
                              "(A) Left\n(S) Down\n(D) Right\n\n"
                              "Choose a direction: ").upper()

    return directions[next_movement]


def validate_move(board: dict, character: dict, direction: str) -> bool:
    """
    Check that moving one space in the desired direction keeps character within bounds of the board.

    :param board: a dictionary representing a coordinate-based game board
    :param character: a dictionary representing the character's status
    :param direction: a string representing the user's desired travel direction
    :precondition: board must be a dictionary containing tuples of two positive integers as keys and strings as values
    :precondition: character must be a dictionary containing an "X-coordinate" key associated with an integer
    :precondition: character must be a dictionary containing a "Y-coordinate" key associated with an integer
    :precondition: values of "X-coordinate" and "Y-coordinate" keys in character must exist as coordinates in board
    :precondition: direction must be a non-empty string
    :precondition: direction must be one of: "Up", "Right", "Down", or "Left"
    :postcondition: checks that moving character one space in specified direction results in a valid position on board
    :return: whether moving character one space in specified direction results in a valid position on board as a boolean

    >>> test_board = {(0, 0): "Left room", (1, 0): "Right room"}
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> validate_move(board=test_board, character=test_character, direction="Right")
    True
    >>> test_board = {(0, 0): "Left room", (1, 0): "Right room"}
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> validate_move(board=test_board, character=test_character, direction="Left")
    False
    """
    maximum_values = {"Y-coordinate": max([y for (_, y) in board]), "X-coordinate": max([x for (x, _) in board])}

    intended_move = COORDINATE_CHANGE[direction]
    updated_coordinate = character[intended_move[0]] + intended_move[1]
    maximum_value_for_intended_move_axis = maximum_values[intended_move[0]]

    if updated_coordinate in range(maximum_value_for_intended_move_axis + 1):
        return True

    else:
        return False


def move_character(character: dict, direction: str) -> None:
    """
    Modify the character's location after moving one space in the desired direction.

    :param character: a dictionary representing the character's status
    :param direction: a string representing the user's desired travel direction
    :precondition: character must be a dictionary containing an "X-coordinate" key associated with an integer
    :precondition: character must be a dictionary containing a "Y-coordinate" key associated with an integer
    :precondition: values of "X-coordinate" and "Y-coordinate" keys in character must exist as coordinates in board
    :precondition: direction must be a non-empty string
    :precondition: direction must be one of: "Up", "Right", "Down", or "Left"
    :postcondition: modifies the character's coordinates by one space in the specified direction

    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> test_direction = "Down"
    >>> move_character(character=test_character, direction=test_direction)
    >>> test_character
    {'X-coordinate': 0, 'Y-coordinate': 1}
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> test_direction = "Right"
    >>> move_character(character=test_character, direction=test_direction)
    >>> test_character
    {'X-coordinate': 1, 'Y-coordinate': 0}
    """
    intended_move = COORDINATE_CHANGE[direction]
    intended_move_axis = intended_move[0]
    intended_move_direction = intended_move[1]

    character[intended_move_axis] += intended_move_direction


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
