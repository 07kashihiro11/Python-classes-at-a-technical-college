for i in [1, 2, 3, 4, 5]:
    print(i)
    
for char_text in "abcdef":
    print(char_text)
    print("for-end")
    
#if True:

for i in [1,2,3]:
    pass
    
for i in range(5):
    print(i)
    
    for i in range(5):
        print(i)
        
numbers = [10,20,30]
for i in numbers:
    print(i)
    
numbers2 = [1,2,3,4,5]
for i in range(2, len(numbers2)):
    print(numbers2[i])
    
for i in range(2,11):
    print(i)
    
numbers = [1,2,3,4,5]
double_numbers =[]

for i in [1,2,3,4,5]:
    double_numbers.append(i * 2)
print(double_numbers)

runner_list =  ["Aさん", "Bさん", "Cさん"]
for index, person in enumerate(runner_list):
    print(f"{person}のインデックスは{index}です")
    
posts = ["部長", "課長", "係長"]
names = ["芥川龍之介", "司馬遼太郎", "谷崎潤一郎"]
for posts, names in zip(posts,names):
    print(names + posts)
    print(f"{names}は{posts}です")
    
    
for i in range(1,5):
    print(i)
else:
    print("いたずら完了")