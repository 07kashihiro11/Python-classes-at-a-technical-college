class Member:
    
    def __init__(self, student_number, name, age, grade):
        self.student_number = student_number
        self.name = name
        self.age = age
        self.grade = grade
        
    def self_introduction(self):
        return f"{self.name}は{self.grade}年生で{self.age}歳です。"
       #return self.name + "は" + self.grade + "年生で" + self.age + "歳です。"
        
# インスタンス化(自分の情報をセット）
my_info = Member(2402941, "岡島大樹", 19, 2)

# student_number(属性)をprint()で表示
print(my_info.student_number)

# インスタンスからself_introductionを実行して、戻り値をprint()で表示
# result = my_info.self_introduction()
# print(result)でもOK
print(my_info.self_introduction())
