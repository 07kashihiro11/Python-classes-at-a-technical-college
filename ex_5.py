# 問題１
x = "あいうえお"
print(len(x))

#問題２
first_name = "やまだ"
last_name = "たろう"
print(len(first_name))
print(len(last_name))

#問題3
print(len(first_name) + len(first_name))

# 問題4
str_number = "123456789"
print(str_number[0])

# 問題5
print(str_number[-1])

#問題6
print(str_number[1:4])

# 問題7
print(str_number[-3:])

# 問題8
half_length = len(str_number) // 2
print(str_number[half_length])

#別解(こっちの方が良かったな〜)
print(str_number[len(str_number) // 2])

# 問題9
# print('This is Tom's pen')のクオーテーションを変更する
print("This is Tom's pen")

#print('My son's pen')にエスケープシーケンスを使用
print('My son\'spen')