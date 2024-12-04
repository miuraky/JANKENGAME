import unittest
from unittest.mock import patch
from source.player import player_pon

class TestPlayerPon(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_player_pon_gu(self, mock_input):
        self.assertEqual(player_pon(), 'グー')

    @patch('builtins.input', side_effect=['2'])
    def test_player_pon_choki(self, mock_input):
        self.assertEqual(player_pon(), 'チョキ')

    @patch('builtins.input', side_effect=['3'])
    def test_player_pon_pa(self, mock_input):
        self.assertEqual(player_pon(), 'パー')

    @patch('builtins.input', side_effect=['0', '4'])
    def test_player_pon_invalid(self, mock_input):
        with patch('builtins.input', side_effect=['0', '4', '1']):
            self.assertEqual(player_pon(), 'グー')  # 最後に有効な入力を受け取るまでループする

if __name__ == '__main__':
    unittest.main()
