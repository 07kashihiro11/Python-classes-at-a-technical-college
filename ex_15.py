# 問題1
person = {
    'name': 'Alice',
    'age': 25,
    'city': 'Tokyo'
}

items = person.items()
print(items)

#問題2
student_scores = {
    "Mike": 85,
    "Emily": 92,
    "John": 78,
    "Sarah": 95
}
del student_scores["Mike"]
print(student_scores)

#問題3
products = {
    "orange": 20,
    "apple": 32,
    "banana": 9
}

if "apple" in products:
    pieces = products["apple"]
    print(f"{pieces}個あります")
else:
    print("ありません")
    
#問題4
product_prices = {
    "apple": 100,
    "banana": 180,
    "orange": 200,
    "grape": 600
}

for value in product_prices.values():
    print(value)
    
#問題5
for name, score in student_scores.items():
    print(f"{name}さんは{score}点でした")
    
# 問題5別解
# for key in student_scores.keys():
    # print(f"{key}さんは{student_scores[key]}点でした")
    
#問題6
students = {
    "Alice":{
        "age": 20,
        "nationality": "USA"
    },
    "Bob":{
        "age": 22,
        "nationality": "UK"
    },
    "Catherine":{
        "age": 19,
        "nationality": "Canada"
    }
}

Bob_age = students["Bob"]["age"]
print(f"Bobの年齢は{Bob_age}歳です")
print(Bob_age)

#問題7
for name, info in students.items():
    if info["age"] >=20:
        print(name)