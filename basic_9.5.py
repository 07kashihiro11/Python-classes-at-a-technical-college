"""basic_10.py
・ミュータブル
・イミュータブル
・タプル
"""

for i in [1, 2, 3, 4, 5]:
    print(i)
    
for i in range(2,11):
    print(i)

runner_list = ["Aさん", "Bさん", "Cさん"]
for index,value in enumerate(runner_list):
    print(f"{value}のインデックスは{index}です")

numbers = [1, 2, 3, 4, 5]
for i in range(2,len(numbers)):
    print(numbers[i])
    
r = range(0, 10)
print(r[5])

mylist = list(range(10))
n = mylist[7]
print(n)

l = [30, 50, 10, 40, 20]
print(l.index(30))
print(l.index(20))

personal_data_list = ["Mike", 20, "student", "Osaka"]
personal_data_list[3] = "Wakayama"
print(personal_data_list)



my_tuple = ("Mike", 20, "student", "Osaka")

print("my_tuple:",my_tuple)
print("my_tupleのデータ型 :",type(my_tuple))

#my_tuple[3] = "Wakayama"
#print(my_tuple)

base_list = [1, 2, 3, 4]
make_tuple = list(base_list)
print(type(make_tuple))
make_tuple[3]= 5
print(make_tuple)

id = [1234, "名前"]
id = (1234, "名前")