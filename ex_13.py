#問題1
x = -1
if x > 0:
    print("正の数です")
elif x < 0:
    print("負の数です")
else:
    print("ゼロです")
    
#問題2は問題1の出力確認
x = 0
if x > 0:
    print("正の数です")
elif x < 0:
    print("負の数です")
else:
    print("ゼロです")
    
#問題3は問題1の出力確認
x = 6
if x > 0:
    print("正の数です")
elif x < 0:
    print("負の数です")
else:
    print("ゼロです")
    
#問題4
y = 50
if y >= 0 and y <= 100:
    print("範囲内です")
else:
    print("範囲外です")
    
#問題5
y = 200
if y >= 0 and y <= 100:
    print("範囲内です")
else:
    print("範囲外です")
    
#問題6
shopping_list = ["apple", "cake", "carrot", "water"]
for fruit in shopping_list:
    if fruit == "apple":
        print("フルーツです")
    elif fruit == "carrot":
        print("野菜です")
    else:
        print("不明です")
        
#問題7
number_list = [1, 2, 3, 4, 5, 6]
for x in number_list:
    if x % 2 == 0 and x % 3 == 0:
        print("2と3の公倍数です")
    elif x % 2 == 0 and x % 3 != 0:
        print("2の倍数です")
    elif x % 2 != 0 and x % 3 == 0:
        print("3の倍数です")
    else:
        print("それ以外です")