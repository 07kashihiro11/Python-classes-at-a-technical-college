correct_password = "secret123"
user_input = " "

while user_input != correct_password:
    user_input = input("パスワードを入力してください: ")
    if user_input != correct_password:
        print("パスワードが間違っています。もう一度試してください。")
    else:
        print("ログインに成功しました。")