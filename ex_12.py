#問題1
score = 90
if score >= 90:
    print("合格です")
    
#問題2
age = 20
if age >= 10 and age<= 30:
    print("青年期です")
    
#問題3
day="土曜日"

if day == "土曜日" or day == "日曜日":
    print("週末です")
    
#問題4
fruits = ["りんご", "みかん", "ぶどう"]
fruit ="りんご"
if fruit in fruits:
    print("とても美味しいです")
    
#問題5
temperature = 25
border = 22
if temperature > border:
    print("暑いです")
    
#問題6
gender = "男性"
age = 22
if gender == "男性" and age >= 20:
    print("成人男性です")

#問題7
current_month = 5
if current_month == "5月" or current_month == "6月":
    print("比較的過ごしやすい時期です")

#問題8
favorite_fruit = "りんご"
selling_fruit = "バナナ"
if favorite_fruit != selling_fruit:
    print("他の果物を買いたいです")
    
#問題9
num = 7
if num > 0:
    print(num*2)
    
#問題10
username = "岡島大樹"
if username:
    print("ユーザー名が設定されています")
    
#問題11
users = ["AAA", "BBB", "CCC"]

if "CCC" in users:
    index = users.index("CCC")
    print(f"CCCは登録されています")
else:
    print("CCCは登録されていません")