# 問題1
print("こんにちは、{}さん".format("山田"))

# 問題2
print("こんにちは、{0}さん。{1}さんが呼んでいましたよ。".format("武田", "山田"))

# 問題3
mail_address = "abcd@co.jp"
mail_address_cor = mail_address.replace("@","アットマーク")
print(mail_address_cor)

#問題4
mail_address_false = "abcd@xyz@co.jp"
mail_address_false_cor = mail_address_false.replace("@","アットマーク",1)
print(mail_address_false_cor)

# 問題5
name = "山田"
print("{}さん、こんにちは！！".format(name))

# 問題6
word = "あしたははれますか？"
x = word.count("は")
print(x)

#問題7
str_number = "123456789"
idx = str_number.find("6")
print(idx)

#問題8
greeting = "Hi, My name is John."
re_greeting = greeting.upper()
print(re_greeting)

#問題9
rename = "NANCY"
re_rename = rename.lower()
print(re_rename)

mikejj = "mike**jj"
re_mikejj = mikejj.replace("**","")
print(re_mikejj)