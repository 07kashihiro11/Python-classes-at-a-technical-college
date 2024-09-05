import random

hands = ['グー', 'チョキ', 'パー']

while True:
    try:
        user_hand = int(input('グー(0), チョキ(1), パー(2): '))
        if user_hand < 0 or user_hand > 2:
            raise ValueError
        break
    except ValueError:
        print('0〜2の整数を入力してください')

computer_hand = random.randint(0, 2)

print(f'あなた: {hands[user_hand]}, コンピュータ: {hands[computer_hand]}')

if user_hand == computer_hand:
    print('あいこ')
elif (user_hand - computer_hand + 3) % 3 == 1:
    print('負け')
else:
    print('勝ち')
