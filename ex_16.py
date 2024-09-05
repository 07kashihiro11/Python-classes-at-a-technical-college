#問題1
list1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
convert_to_list1 = set(list1)
print(convert_to_list1)

#問題2
students = {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}
students.remove("David")
print(students)

#問題3
math_students = {'ALice', 'Bob', 'Charlie'}
english_students = {'Bob', 'David', 'Eve'}

only_math_students = math_students.difference(english_students)
print(only_math_students)

#問題4
both_students = math_students.intersection(english_students)
print(both_students)

#問題5
symmetric_students = math_students.symmetric_difference(english_students)
print(symmetric_students)

#問題6
math_students.add("Frank")
print(math_students)

#問題7
last_users = {"Aさん", "Bさん", "Cさん"}
this_users = {"Aさん", "Dさん", "Eさん"}

only_last_users = last_users.difference(this_users)

print(only_last_users)