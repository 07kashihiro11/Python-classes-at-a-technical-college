# 関数の問題Part２

#問題1
def greet(name = "World"):
    print(f"Hello, {name}!")
greet()

#問題2
def make_coffee(size = "default size" ):
    print(f"Making acoffee of {size}.")
make_coffee()

#問題3
def introduce_myself(name, age, country="Japan"):
    print(f"My name is {name}, I am {age} years old, and I am from {country}.")
introduce_myself(name = "Mike", age = 22)
    
#問題4
def sum_numbers(*args):
    print(sum(args))

sum_numbers(1, 2, 3)

#問題5
def count_args(*args):
    print(len(args))

count_args(*"Hello!")

#問題6
def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
profile = {
    "name":"Mike", 
    "age": 22
}  
    
show_profile(**profile)
    

