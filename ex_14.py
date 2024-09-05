#問題1
product = {
    'id':'P001',
    'name':'iphone',
    'price': 99900,
    'brand': 'Apple'
}
print(product['brand'])

#問題2
print(len(product))

#問題3
vantan = {
    '月曜日':'デザインシンキング',
    '火曜日':'Python',
    '水曜日':'Webデザイン'
}
print(vantan)

#問題4
population = {
    'Tokyo': 13929286,
    'Osaka': 8839469,
    'Nagoya':2378140,
    'Fukuoka':1559971
}

population['Osaka'] = 200
print(population)

#問題5
del population['Fukuoka']
print(population)


#問題6
students = {
    'student1':{'name':'Alice', 'age':18, 'grade': 'A'},
    'student2':{'name':'Bob', 'age':17, 'grade': 'B'},
    'student3':{'name':'Charlie', 'age':16, 'grade': 'C'}
}
print(f"{students['student2']['name']}の年齢は{students['student3']['age']}歳です。")

#問題7
words = {
    "b":"びー",
    "c":"しー",
    "a":"えー",
}

sorted_words = sorted(words)

for key in sorted_words:
    print(key, words[key])