from time import sleep

def output(message, delay=3):
    print(message)
    sleep(delay)

output("欢迎来到Python编程世界！")
output("有关Python的更多信息，请访问官方网站：https://www.python.org/")
output("开始你的第一个Python项目吧！", delay=0)

output("要求：输出\"Hello, world!\"")
output("示例代码：\n    print(\"Hello, world!\")", delay=0)
omput_possibility = ["print(\"Hello, world!\")",
                     "print('Hello, world!')",
                     "print(\"Hello world!\")",
                     "print('Hello world!')",
                     "print(\"Hello,world!\")",
                     "print('Hello,world!')",
                     "print (\"Hello, world!\")",
                     "print ('Hello, world!')",
                     "print (\"Hello world!\")",
                     "print ('Hello world!')",
                     "print (\"Hello,world!\")",
                     "print ('Hello,world!')"]
string = input("试一试吧~\n1   ")
while string not in omput_possibility:
    string = input("输入错误，再试一次吧~\n1   ")
output("恭喜你，完成了你的第一个Python程序！")