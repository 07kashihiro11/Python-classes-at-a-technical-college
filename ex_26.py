
#問題1
# file = open("test1.txt", "w")
# file.write("Hello, World!")
# file.close()

with open("test1.txt", "w") as file:
    file.write("こんにちは!")

#問題2   
with open("test1.txt", "r") as file:
    #ファイルの内容を読み取る
    content = file.read()
    print(content)
    
    
#問題3
with open("test1.txt", "a") as file:
    file.write("今日は暑いですね。")
