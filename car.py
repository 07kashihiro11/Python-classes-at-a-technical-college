class Car:
    
    #属性(初期化)
    def __init__(self):
        print("必ず実行！")
        
    #メソッド
    def drive(self):
        print("ぶぅーーーん")
        
my_car = Car()


class Car:
    # 属性(初期化)
    def __init__(self):
      self.color = "Green"
    # メソッド
    def drive(self):
        print("ぶぅーーん")

my_car = Car()
print(my_car.color)

class Car:
    # 属性(初期化)
    def __init__(self, color):
      self.color = color
    # メソッド
    def drive(self):
        print("ぶぅーーん")

my_car = Car("Red")
print(my_car.color)
my_car.drive()


