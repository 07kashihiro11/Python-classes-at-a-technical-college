# import random

# num = random.randrange(1, 10)
# print(num)

# my_list = (1, 30, "やっほー")
# print(random.choice(my_list))

# name = int(input("名前を入力してください"))
# print(name)
# print(type(int(name)))

import random

for i in range(1000):
    try:
        user = int(input("1:グー、2:チョキ、3:パー、なにだす？"))
        if user not in [1, 2, 3]:
            print("1~3までの数字を入力してください")
            continue
    except ValueError:
        print("失敗: 1か2か3を出してね")
        continue

    com = random.randint(1, 3)
    print(f"あなた: {user}")
    print(f"コンピュータ: {com}")

    if user == com:
        print("あいこ")
    elif user == 1 and com == 2:
        print("comはチョキ。あなたの勝ち")
        break
    elif user == 1 and com == 3:
        print("comはパー。あなたの負け")
        break
    elif user == 2 and com == 1:
        print("comはグー。あなたの勝ち")
        break
    elif user == 2 and com == 3:
        print("comはパー。あなたの負け")
        break
    elif user == 3 and com == 1:
        print("comはグー。あなたの勝ち")
        break
    elif user == 3 and com == 2:
        print("comはチョキ。あなたの負け")
        break
    