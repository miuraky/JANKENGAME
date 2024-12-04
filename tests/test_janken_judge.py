import unittest
from source.janken_judge import judge

class TestJudge(unittest.TestCase):

    def test_judge_draw_gu(self):
        self.assertEqual(judge("グー", "グー"), "draw")

    def test_judge_draw_choki(self):
        self.assertEqual(judge("チョキ", "チョキ"), "draw")

    def test_judge_draw_pa(self):
        self.assertEqual(judge("パー", "パー"), "draw")

    def test_judge_player_win_gu_choki(self):
        self.assertEqual(judge("チョキ", "グー"), "player_win")

    def test_judge_player_win_choki_pa(self):
        self.assertEqual(judge("パー", "チョキ"), "player_win")

    def test_judge_player_win_pa_gu(self):
        self.assertEqual(judge("グー", "パー"), "player_win")

    def test_judge_computer_win_choki_gu(self):
        self.assertEqual(judge("グー", "チョキ"), "computer_win")

    def test_judge_computer_win_pa_choki(self):
        self.assertEqual(judge("チョキ", "パー"), "computer_win")

    def test_judge_computer_win_gu_pa(self):
        self.assertEqual(judge("パー", "グー"), "computer_win")

if __name__ == '__main__':
    unittest.main()
