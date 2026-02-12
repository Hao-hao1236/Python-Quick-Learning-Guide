from time import sleep

def output(message, delay=2):
    print(message)
    sleep(delay)

output("欢迎来到Python编程世界！")
output("有关Python的更多信息，请访问官方网站：https://www.python.org/")
output("开始你的第一个Python项目吧！", delay=0)

output("要求：输出\"Hello, world!\"")
output("示例代码：\n    print(\"Hello, world!\")", delay=0)
output_possibility = ["print(\"Hello, world!\")",
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
string = input("试一试吧~\n1   ").strip()
while string not in output_possibility:
    string = input("输入错误，再试一次吧~\n1   ").strip()
output("=====RESTART: Python3 App=====\n" + \
       string[8 if string[5] == ' ' else 7:-2],
       delay=2)
output("恭喜你，完成了你的第一个Python程序！")
