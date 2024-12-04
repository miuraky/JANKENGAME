import source.player
import source.computer
import source.janken_judge

def play_round(round):
    print(f"-----ラウンド {round} -----")
    computer_hand = source.computer.computer_pon()
    player_hand = source.player.player_pon()
    result = source.janken_judge.judge(computer_hand, player_hand)
    display_hands(player_hand, computer_hand)
    return result

def display_hands(player_hand, computer_hand):
    print(f"あなたの手: {player_hand}")
    print(f"コンピューターの手: {computer_hand}")
    print("")

def update_score(result, player_win, computer_win):
    if result == 'player_win':
        player_win += 1
        print("あなたの勝ちです！")
    elif result == 'computer_win':
        computer_win += 1
        print("コンピューターの勝ちです！")
    else:
        print("あいこです！ 再度対決！")
    return player_win, computer_win

def display_final_result(player_win, computer_win):
    print("【最終結果】")
    print(f"あなた: {player_win}勝")
    print(f"コンピュータ: {computer_win}勝")
    if player_win >= computer_win:
        print("あなたの総合勝利です！")
    else:
        print("コンピュータの総合勝利です！")

def main():
    player_win = 0
    computer_win = 0
    round = 1

    while round <= 3:
        result = play_round(round)
        if result != 'draw':
            round += 1
            player_win, computer_win = update_score(result, player_win, computer_win)
        print("")

    display_final_result(player_win, computer_win)

if __name__ == '__main__':
    main()
