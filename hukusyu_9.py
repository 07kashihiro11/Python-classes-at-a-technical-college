#リストの問題　メソッド
#問題1
fruits = ["apple", "banana", "grape"]
fruits.append("orange")
print(fruits)

#問題2
numbers = [1, 2, 3, 4, 5]
numbers.insert(0,0)
print(numbers)

#問題3
colors = ["red", "blue", "green", "yellow"]
print(colors.index("green"))

#問題4
languages = ["Java", "C", "Python", "Ruby"] 
print(languages.index("Python"))

#問題5
shopping_list  = ["apple", "banana", "orange", "milk"]
removed_item = shopping_list.pop()
print(removed_item)

#問題6
names = ["Alice", "Bob", "Charlie", "David"] 
names.pop(2)
print(names)

#問題7
numbers = [5, 2, 8, 1, 9] 
numbers.sort()
print(numbers)

#問題8
alphabets  = ["c", "a", "b", "f", "d"]
alphabets.sort(reverse = True)
print(alphabets)

#問題9
original = ["one", "two", "three"]
copied = original.copy()
print(copied)
copied[0] = "Updated" 
print(copied)

#問題10
numbers = [1, 3, 5, 2, 5, 4, 5, 5] 
print(numbers.count(5))

#問題11
print(3 + 3)

print(5 - 2)

print(10 / 3)

print(3 * 5)

print(10 // 3)

print(10 % 3)

print(5**2)