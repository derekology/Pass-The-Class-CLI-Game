"""
Derek Woo
A01351415
"""


import random


def guessing_game() -> bool:
    """
    Play a number guessing game.

    A function that generates an integer between 1 and 5 and prompts user to guess it correctly, or lose a reeses point.

    :postcondition: asks user for their guess
    :postcondition: check if user guesses correctly
    :postcondition: prints the outcome of this instance of the guessing game
    :return: whether the user guessed correctly as a boolean
    """
    number_to_guess = str(random.randint(1, 3))

    guess = input("(Choose a number between 1 and 3 inclusive): ")

    while not guess.isdigit() or int(guess) not in range(1, 4):
        guess = input(f"\nYour guess is not on the lock. Choose an integer between 1 and 3 inclusive: ")

    return number_to_guess == guess


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
