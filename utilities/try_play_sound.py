"""
Derek Woo
A01351415
"""


from playsound import playsound
from playsound import PlaysoundException


def try_play_sound(filename: str, action: str = "a sound playing") -> None:
    """
    Try to play a sound file, and print action if an error is raised.

    :param filename: a string representing the full filename of a .wav audio file
    :param action: a string representing the action in the sound
    :precondition: file represented by filename must point to an existing .wav audio file
    :precondition: action must be a string
    :precondition: action must contain a present participle
    :postcondition: plays the audio file pointed to by parameter filename
    :postcondition: prints a text representation of the sound based on the action parameter if it fails
    """
    try:
        playsound(filename)

    except PlaysoundException:
        print(f"*{action}*")
