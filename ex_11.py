#問題1
fruits = ["apple", "banana", "grape"]
for i in fruits:
    print(i)
    
#問題2
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i,end="")
print()
    
#問題3
for i in range(1,11):
    print(i)
    
#問題4
for i in range(1,6,2):
    print(i)
    
#問題5
shopping_list  = ["apple", "banana", "orange", "milk"]
for i, item in enumerate(shopping_list, 1):
    print(f"{i}番に{item}を買います")
    
#問題5別解
shopping_list  = ["apple", "banana", "orange", "milk"]
for i in range(len(shopping_list)):
    print(f"{i+1}番に{shopping_list[i]}を買います")
    
#問題6
names = ["Alice", "Bob", "David"]
for i in names:
    print(i)
else:
    print("以上です")
    
#問題7
numbers = [1, 2, 3, 4, 5]
for i in range(6,11):
    numbers.append(i)
print(numbers)

#問題8
double_numbers =[]
for i in numbers:
    double_numbers.append(i * 2)
print(double_numbers)

#問題9
lower_char_list = ["a", "b", "c"]
upper_char_list = ["A", "B", "C"]

for l, u in zip(lower_char_list,upper_char_list):
    print(l + u)
    
#問題10
for i in range(len(lower_char_list)):
    lower_char = lower_char_list[i]
    upper_char = upper_char_list[i]
    print(lower_char + upper_char)
    
#問題10の別解
for i, lower_char in enumerate(lower_char_list):
    lower_char = lower_char_list[i]
    upper_char = upper_char_list[i]
    print(lower_char + upper_char)  
