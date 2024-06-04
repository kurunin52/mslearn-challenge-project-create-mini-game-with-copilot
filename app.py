import random

win = 0
lose = 0
draw = 0

# ユーザに入力を求める。小文字化した値が「rock」「scissors」「paper」のどれでもない場合は再入力を求める
while True:
    user = input('rock, scissors, paper?')
    # userを小文字にする
    user = user.lower()
    if user not in ['rock', 'scissors', 'paper']:
        print('Please input rock, scissors, or paper')
        continue
    else:
        # 「rock」「scissors」「paper」のうち、ランダムでどれかを変数に含める
        computer = random.choice(['rock', 'scissors', 'paper'])
        print('computer:', computer)
        if user == computer:
            print('Draw')
            draw += 1
        elif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
            print('You Win!')
            win += 1
        else:
            print('You Lose!')
            lose += 1

        # もう一度プレイするかをユーザに尋ねる
        play_again = input('Play again? (yes/no)')
        if play_again != 'yes':
            # ここまでの勝敗を表示
            print('Win:', win, 'Lose:', lose, 'Draw:', draw)
            break
        else:
            continue