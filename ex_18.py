#問題1 
numbers = [i+1 for i in range(-1,9)]
print(numbers)

#問題2
squares =[]
for i in range(1,11):
    squares.append(i**2)
print(squares)

squares = [i**2 for i in range(1,11)]
print(squares)

#問題3
even_numbers =[]
for i in range(1, 21):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)

even_numbers = [i for i in range(1,21) if i % 2 == 0]
print(even_numbers)