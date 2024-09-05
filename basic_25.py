# 例外処理の問題

# number = "a"
# result = 10 / number
# print(result)

try:
    #例外が発生する可能性のあるコード
    number = "a"
    result = 10 / number
    print(result)
except TypeError as e:
    #TypeErrorが発生した場合の処理
    print("TypeError出てるけど大丈夫？")
    print("エラーの内容:", e)
    
try:
    #例外が発生する可能性のあるコード
    number = 0
    result = 10 / number
    print(result)
# except TypeError as e:
#     #TypeErrorが発生した場合の処理
#     print("TypeError出てるけど大丈夫？")
#     print("エラーの内容:",e)
# except ZeroDivisionError as e:
#     print("0を使うとエラーになるよ")
#     print("エラーの内容:", e)
except Exception as e:
    print("エラーが出ています。なぜか分からんけど")

print("basic_25終了")