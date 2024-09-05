
#問題1,問題2
class User:
    #属性（初期化）
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # メソッド
    def get_name(self):
        print(self.name) 
    
    def get_age(self):
        print(self.age) 

#問題3:　インスタンス化し、get_name() と get_age() メソッドを呼び出す
my_user = User("山田", 22)
name = my_user.get_name()
age = my_user.get_age()

#問題4
print(my_user.name)
print(my_user.age)