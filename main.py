# 更多语法请访问：https://www.w3schools.com/python/
from time import sleep


def output(message, delay=2):
    print(message)
    sleep(delay)


# output("欢迎来到Python编程世界！")
# output("有关Python的更多信息，请访问官方网站：https://www.python.org/")
# output("开始你的第一个Python项目吧！", delay=0)


# output("要求：输出\"Hello, world!\"")
# output("示例代码：\n1   print(\"Hello, world!\")", delay=0)

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
# output("=====RESTART: Python3 App running screen=====\n" + \
#        string[8 if string[5] == ' ' else 7:-2])

# output("恭喜你，完成了你的第一个Python程序！")
# output("----------------------------------", delay=5)


# output("接下来，让我们了解一下Python的基本语法吧！")
# output("1. 变量和数据类型")
# output("在Python中，你可以使用变量来存储数据。Python支持多种数据类型，如整数(int)、浮点数(float)、字符串(str)和布尔值(bool)等等。")
# output("示例代码：\n1   age = 25\n2   name = \"Alice\"\n3   is_student = True", delay=0)

# string = input("试一试吧~\n1   ")
# parts = string.split('=')
# while len(parts) != 2 or parts[0].strip() != 'age' or not parts[1].strip().isdigit():
#     string = input("输入错误，再试一次吧~\n1   ")
#     parts = string.split('=')

# string = input("2   ")
# parts = string.split('=')
# while len(parts) != 2 or parts[0].strip() != 'name' or \
#             (not parts[1].strip().startswith('"') or not parts[1].strip().endswith('"')) and \
#             (not parts[1].strip().startswith("'") or not parts[1].strip().endswith("'")):
#         string = input("输入错误，再试一次吧~\n2   ")
#         parts = string.split('=')

# string = input("3   ")
# parts = string.split('=')
# while len(parts) != 2 or parts[0].strip() != 'is_student' or not parts[1].strip().lower() in ['true', 'false']:
#     string = input("输入错误，再试一次吧~\n3   ")
#     parts = string.split('=')

# output("=====RESTART: Python3 App running screen=====\n")

# output("看起来并没有输出。")
string = input("接下来试着用print()函数输出这些变量的值吧！（如果想要提示可直接按下回车键）\n4   ")
var_list = ['age', 'name', 'is_student']

def check_input(line):
    global string, var_list
    while True:
        if string.strip() == "":
            output("示例代码：\n4   print(age)\n5   print(name)\n6   print(is_student)", delay=0)
        elif string[:6] == "print(" and string[-1] == ")":
            if string[6:-1].strip() in var_list:
                del var_list[var_list.index(string[6:-1].strip())]
                break
            else:
                string = input(f"输入错误，再试一次吧~\n{line}   ")
        else:
            string = input(f"输入错误，再试一次吧~\n{line}   ")

check_input(4)
check_input(5)
check_input(6)
