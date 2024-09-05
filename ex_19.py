#問題１
def say_hello():
    print("Hello")
    
#問題2
def add_numbers(a,b):
    return(a + b)
    
result = add_numbers(3,5)
print(result)

#問題3
def get_length(text):
    return len(text)

result = get_length("Hello, World")
print(result)

#問題4
def email_address_validation(email):
    if "@" in email:
        return True
    else:
        return False
    
email1 = "abcd@aaa.com"
email2 = "xyz.ne.jp"
result1 = email_address_validation(email1)
result2 = email_address_validation(email2)

print(email1)
print(email2)

#問題5
def list_generate(start, end):
    list1 =[]
    for i in range(start, end):
        list1.append(i)
    return list1

result = list_generate(1, 6)
print(result)