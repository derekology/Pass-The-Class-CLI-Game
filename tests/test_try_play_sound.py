"""
Derek Woo
A01351415
"""


from unittest import TestCase
from unittest.mock import patch
import io
from utilities.try_play_sound import try_play_sound


class TestTryPlaySound(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_try_play_sound_with_nonexistent_file_with_short_action(self, mock_output):
        try_play_sound("nonexistent.wav", "A")
        expected = "*A*\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_try_play_sound_with_nonexistent_file_with_longer_action(self, mock_output):
        try_play_sound("nonexistent.wav", "A nonexistent sound playing")
        expected = "*A nonexistent sound playing*\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_try_play_sound_with_existing_file(self, mock_output):
        try_play_sound("../sounds/res.wav", "A nonexistent sound playing")
        expected = ""
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
