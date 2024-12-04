import unittest
from unittest.mock import patch
from tests.test_janken import play_round, display_hands, update_score, display_final_result

class TestJankenGame(unittest.TestCase):

    @patch('source.player.player_pon', return_value='グー')
    @patch('source.computer.computer_pon', return_value='チョキ')
    def test_play_round(self, mock_computer, mock_player):
        with patch('builtins.print'):
            result = play_round(1)
        self.assertEqual(result, 'player_win')

    def test_display_hands(self):
        with patch('builtins.print') as mocked_print:
            display_hands('グー', 'チョキ')
            mocked_print.assert_any_call("あなたの手: グー")
            mocked_print.assert_any_call("コンピューターの手: チョキ")
            mocked_print.assert_any_call("")

    def test_update_score_player_win(self):
        with patch('builtins.print'):
            player_win, computer_win = update_score('player_win', 0, 0)
        self.assertEqual(player_win, 1)
        self.assertEqual(computer_win, 0)

    def test_update_score_computer_win(self):
        with patch('builtins.print'):
            player_win, computer_win = update_score('computer_win', 0, 0)
        self.assertEqual(player_win, 0)
        self.assertEqual(computer_win, 1)

    def test_update_score_draw(self):
        with patch('builtins.print'):
            player_win, computer_win = update_score('draw', 0, 0)
        self.assertEqual(player_win, 0)
        self.assertEqual(computer_win, 0)

    def test_display_final_result(self):
        with patch('builtins.print') as mocked_print:
            display_final_result(2, 1)
            mocked_print.assert_any_call("【最終結果】")
            mocked_print.assert_any_call("あなた: 2勝")
            mocked_print.assert_any_call("コンピュータ: 1勝")
            mocked_print.assert_any_call("あなたの総合勝利です！")

if __name__ == '__main__':
    unittest.main()
