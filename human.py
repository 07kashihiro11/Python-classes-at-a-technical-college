#問題1
class Human:
    #属性(初期化）
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #メソッド
    def introduce(self):
        print(f"{self.name}は{self.age}歳です。")
       #print(self.name + "は" + str(self.age) + "歳です。")でもOK
    
#問題2
class Student(Human):
    def introduce(self):
        print("私は学生です。")
        
#問題3
class Teacher(Human):
    def introduce(self):
        print("私は教師です。")
        
#問題4
human = Human("太郎", 25)
student = Student("花子", 20)
teacher = Teacher("佐藤", 35)

human.introduce()
student.introduce()
teacher.introduce()

