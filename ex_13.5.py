import random

num = random.randrange(1, 10)
print(num)

my_list = (1, 30, "やっほー")
print(random.choice(my_list))

name = input("名前を入力してください: ")
print(name)



##じゃんけんの条件:グーは1,チョキは2,パーは3

#1. randomをインポートする

#2. インプット関数で自分の入力値を変数に代入

#3. コンピューターの出す整数をランダム(乱数)にする

#4. もし、自分の入力値とコンピュータの生成した乱数が同じなら「あいこ」

#5.　もし、自分の入力値が1で、コンピュータが2の場合「勝ち」

