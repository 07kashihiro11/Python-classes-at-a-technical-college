#関数の問題 Part３

#問題1
x = 10
def test():
    # x = 20
    print("xの値は:", x)
    
test()

#問題2
x = 10
def test():
    global x
    x = 20
    return x

# print(test())  
print(x)

