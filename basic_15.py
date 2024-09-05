student = {
    "name": "John",
    "age": 20,
    "grade": "A",    
}

keys = student.keys()
print(keys)

for key in keys:
    print(student[key])
    
    
    
print(student.get("address"))
print(student["address"])