# 1. randomをインポートする
import random

# 辞書を定義して、じゃんけんの手とその対応する数値をマッピングする
choices = {"グー": 0, "チョキ": 1, "パー": 2}
computer_choice = random.randint(0, 2)
reverse_choices = {0: "グー", 1: "チョキ", 2: "パー"}

# 勝敗を判定する関数
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "あいこ"
    elif (user_choice - computer_choice + 3) % 3 == 2:
        return "あなたの勝ち"
    else:
        return "コンピューターの勝ち"

# じゃんけんゲームを実行する関数
def play_janken():
    while True:
        # 2. インプット関数で自分の入力値を変数に代入
        user_input = input("じゃんけんの手を入力してください（グー、チョキ、パー）：")
        user_choice = choices.get(user_input)
        
        # user_choiceがNoneなら無効な入力
        if user_choice is None:
            print("無効な入力です。もう一度入力してください。")
            continue

        # 3. コンピューターの出す整数をランダム(乱数)にする
        computer_choice = random.randint(0, 2)

        # 結果を判定
        result = determine_winner(user_choice, computer_choice)

        # 結果を表示
        print(f"あなたの手は {user_input} でした。")
        print(f"コンピューターの手は {reverse_choices[computer_choice]} でした。")
        print(result)

        # あいこの場合、再度じゃんけん
        if result == "あいこ":
            print("あいこで...")
        else:
            break

# じゃんけんゲームを開始
play_janken()