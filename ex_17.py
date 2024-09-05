#問題1
i = 1

while i <= 10:
    if i % 3 == 0:
        print(i)
    i += 1

#問題2
i = 1
total = 0

while i <=20:
    total += i
    i += 1
    
print(total)

#問題3
i = 1

while i <=10:
    
    if i == 7:
        break
    
    print(i)
    
    i += 1
    
#問題4
my_list = [10, 20, 30, 40, 50]

i = 0
while i <len(my_list):
    print(my_list[i])
    i += 1
    
#追加課題
# 次の実行結果になるようにプログラムを作成しなさい
# 1:海鮮丼,２:カツ丼, 3:牛丼
# 入力:(2,3,2,3,1)
# 出力:海鮮丼1票,カツ丼２票,牛丼２票

menu = {1: "海鮮丼", 2: "カツ丼", 3: "牛丼"}

votes = (2, 3, 2, 3, 1)

vote_count = {1: 0, 2: 0, 3: 0}

index = 0
while index < len(votes):
    vote = votes[index]
    if vote in vote_count:
        vote_count[vote] += 1
    index += 1

# 結果を表示　
results = [f"{menu[key]}{value}票" for key, value in vote_count.items()]
print(",".join(results))
