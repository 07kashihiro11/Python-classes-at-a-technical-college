#idは「9999」,パスワードは「kkkk」
#inputでidとパスワードを入力
#idとパスワードを使ってログイン成功orログイン失敗かをprint()で出力する関数を作りましょう
#引数(仮引数）には、「id」「pw」をとります。

# correct_id = "9999"
# correct_pw = "kkkk"

# input_id = input("idを入力してください")
# input_pw = input("パスワードを入力してください")

# def check_login(id, pw):
#     if id == correct_id and pw == correct_pw:
#         print("ログイン成功")
#     else:
#         print("ログイン失敗")
        
# check_login(input_id, input_pw)


amount = 10000

#amountに1.1をかけて税込にする関数を作ってください。
#returnで値を返してください。
#関数名は「add_tax」にする。

# input()で「テイクアウト」か「イートイン」入力
# テイクアウトなら*1.08
# イートインなら*1.1

# amount = 10000
input_order = input("「テイクアウト」か「イートイン」を入力してください")
input_pay = int(input("いくら払いますか？"))
#resultよりもinput_payが小さかったら「足りません」　←print()
#「お釣りは〇〇円です」←print()
#関数名は「bill」にしてください

def add_tax(amount):
    if input_order == "テイクアウト":
        return amount * 1.08
    if input_order == "イートイン":
        return amount * 1.1
    
result = add_tax(amount)
    
def bill(total_amount, input_pay):
    if total_amount > input_pay:
        print("お金が足りません")
    else:
        print(f"お釣りは{input_pay - total_amount}円です。")

bill(result, input_pay)