import random

for i in range(1000):
  user = int(input("1:グー、2:チョキ、3:パー、なにだす？？"))
  com = random.randint(1, 3)

  print(user)
  print(com)
  if user == com:
    print("あいこー")
  elif user == 1 and com == 2:
    print("comはチョキ。あなたの勝ちです!")
    break
  elif user == 1 and com == 3:
    print("comはパー、まけー")
    break
  elif user == 2 and com == 1:
    break
    pass
  elif user == 2 and com == 3:
    break
    pass
  elif user == 3 and com == 1:
    break
    pass
  elif user == 3 and com == 2:
    break
    pass
  else:
    print("1~3の数字を入力してください")