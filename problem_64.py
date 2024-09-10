def get_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        print(f"エラー: インデックス {index} は範囲外です。")
    except Exception as e:
        print(f"予期しないエラー: {e}")

result = get_element([1, 2, 3], 1)  
if result is not None:
    print(result)

result = get_element([1, 2, 3], 5)  
if result is not None:
    print(result)

result = get_element([], 0)  
if result is not None:
    print(result)