"""ex_8.py"""

#問題1
number = [1, 2, 3, 4, 5]
number.append(50)
number.pop(4)
print(number)

#問題2
list1 = [10, 20, 30, 40, 50]
list2= [100, 200, 300, 400, 500]
new_list = list1 + list2
#list1 += list2
print(new_list)

#問題3
#問題の指示では無い解き方
#new_list.sort()
#print(new_list[0])

min_value = min(new_list)
print(min_value)

#問題4
max_value = max(new_list)
print(max_value)

#問題5
total_value = sum(new_list)
print(total_value)

#問題6
print(total_value / len(new_list))

#問題7
num_list = list(range(5, 16))
print(num_list)

#問題8
odd_list = list(range(1, 22, 2))
print(odd_list)