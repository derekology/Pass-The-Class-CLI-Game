from unittest import TestCase
from unittest.mock import patch
import io
from utilities.read_game_intro import read_game_intro


class TestReadGameIntro(TestCase):
    def test_read_game_intro_with_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            read_game_intro("nonexistent_file")

    @patch("utilities.read_game_intro.sleep", return_value=None)
    @patch("builtins.open", side_effect=[io.StringIO('')])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_read_game_intro_with_an_empty_file(self, mock_output, _, __):
        read_game_intro("test_read_game_intro.py")
        actual = mock_output.getvalue()
        expected = ""
        self.assertEqual(expected, actual)

    @patch("utilities.read_game_intro.sleep", return_value=None)
    @patch("builtins.open", side_effect=[io.StringIO('This is one line in my file.')])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_read_game_intro_with_a_one_line_file(self, mock_output, _, __):
        read_game_intro("test_read_game_intro.py")
        actual = mock_output.getvalue()
        expected = "\nThis is one line in my file."
        self.assertEqual(expected, actual)

    @patch("utilities.read_game_intro.sleep", return_value=None)
    @patch("builtins.open", side_effect=[io.StringIO('This is one line in my file.\n'
                                                     'This is a second line in my file.\n'
                                                     'This is a third line in my file.')])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_read_game_intro_with_a_file_with_more_than_one_line(self, mock_output, _, __):
        read_game_intro("test_read_game_intro.py")
        actual = mock_output.getvalue()
        expected = "\nThis is one line in my file.\n" \
                   "\nThis is a second line in my file.\n" \
                   "\nThis is a third line in my file."
        self.assertEqual(expected, actual)
