#問題1
try:
    name = "Nancy"
    age = 32
    print(name + "は" + age + "才です")
# except Exception as e:
#     print("エラーが出たみたい")
except TypeError:
    print("エラーが出たみたい")
    
#問題2
try:
    name = "Nancy"
    age = 32
    print(name + "は" + age + "才です")
except Exception as e:
    print("エラーが出たみたい")
    print(e)


