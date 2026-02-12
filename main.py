# 更多语法请访问：https://www.w3schools.com/python/
from time import sleep


def output(message, delay=2):
    print(message)
    sleep(delay)


# output("欢迎来到Python编程世界！")
# output("有关Python的更多信息，请访问官方网站：https://www.python.org/")
# output("开始你的第一个Python项目吧！", delay=0)


# output("要求：输出\"Hello, world!\"")
# output("示例代码：\n    print(\"Hello, world!\")", delay=0)

# output_possibility = ["print(\"Hello, world!\")",
#                      "print('Hello, world!')",
#                      "print(\"Hello world!\")",
#                      "print('Hello world!')",
#                      "print(\"Hello,world!\")",
#                      "print('Hello,world!')",
#                      "print (\"Hello, world!\")",
#                      "print ('Hello, world!')",
#                      "print (\"Hello world!\")",
#                      "print ('Hello world!')",
#                      "print (\"Hello,world!\")",
#                      "print ('Hello,world!')"]

# string = input("试一试吧~（尽量使用英文半角输入）\n1   ").strip()
# while string not in output_possibility:
#     string = input("输入错误，再试一次吧~\n1   ").strip()
# output("=====RESTART: Python3 App=====\n" + \
#        string[8 if string[5] == ' ' else 7:-2])

# output("恭喜你，完成了你的第一个Python程序！")
# output("----------------------------------", delay=5)


output("接下来，让我们了解一下Python的基本语法吧！")
output("1. 变量和数据类型")
output("在Python中，你可以使用变量来存储数据。Python支持多种数据类型，如整数(int)、浮点数(float)、字符串(str)和布尔值(bool)等等。")
output("示例代码：\n1   age = 25\n2   name = \"Alice\"\n3   is_student = True", delay=0)

string = input("试一试吧~\n1   ")
list = string.split('=')
while len(list) != 2 or list[0].strip() != 'age' or not list[1].strip().isdigit():
    string = input("输入错误，再试一次吧~\n1   ")
    list = string.split('=')

string = input("2   ")
list = string.split('=')
while len(list) != 2 or list[0].strip() != 'name' or \
      (not list[1].strip().startswith('"') or not list[1].strip().endswith('"')) and \
      (not list[1].strip().startswith("'") or not list[1].strip().endswith("'")):
    string = input("输入错误，再试一次吧~\n2   ")
    list = string.split('=')

string = input("3   ")
list = string.split('=')
while len(list) != 2 or list[0].strip() != 'is_student' or not list[1].strip().lower() in ['true', 'false']:
    string = input("输入错误，再试一次吧~\n3   ")
    list = string.split('=')

output("真棒！你已经学会了如何在Python中定义变量和使用基本数据类型。")
string = input("接下来试着用print()函数输出这些变量的值吧！（如果想要提示可直接按下回车键）\n4   ")

def check_input(var_name):
    if var_name == 'age':
        output(25, delay=0)
    elif var_name == 'name':
        output("Alice", delay=0)
    elif var_name == 'is_student':
        output(True, delay=0)
    else:
        output("变量不存在哦~", delay=0)

while True:  # 换种方法检查用户输入
    if string == "":
        output("示例代码：\n4   print(age)\n5   print(name)\n6   print(is_student)", delay=0)
        string = input("4   ")
        pass
    elif string[0:5] == "print" and string.count('(') == 1 and string.count(')') == 1 and \
        string.index(')') > string.index('(') + 1:
        var_name = string[string.index('(') + 1:string.index(')')].strip()
        check_input(var_name)
    else:
        string = input("输入错误，再试一次吧~\n4   ")