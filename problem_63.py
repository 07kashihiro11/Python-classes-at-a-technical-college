def divide_numbers():
    try:
        num1 = float(input("1つ目の数字を入力してください: "))
        num2 = float(input("2つ目の数字を入力してください: "))
        
        result = num1 / num2
        print(f"結果: {result}")
    
    except ValueError:
        print("有効な数字を入力してください。")
    
    except ZeroDivisionError:
        print("ゼロで割ることはできません。")

# 関数を実行
divide_numbers()