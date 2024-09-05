#練習問題
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number == 9:
        break
    if number % 2 == 0:
        print(number)
        
#練習問題別解
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number == 9:
        break
    if number % 2 == 0:
        continue #偶数をスキップして次の繰り返しに進む
    print(number)
else:
    print("9はリスト内に見つかりませんでした。")
