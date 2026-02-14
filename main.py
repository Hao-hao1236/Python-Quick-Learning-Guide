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
# var_list = ['age', 'name', 'is_student']

# output("接下来试着用print()函数输出这些变量的值吧！（如果想要提示可直接按下回车键）")

# def check_input(line):
#     global var_list
#     while True:
#         string = input(f"{line}   ")
#         if string.strip() == "":
#             output("示例代码：\n4   print(age)\n5   print(name)\n6   print(is_student)\n再试试看~", delay=0)
#         elif string[:6] == "print(" and string[-1] == ")":
#             if string[6:-1].strip() in var_list:
#                 del var_list[var_list.index(string[6:-1].strip())]
#                 break
#             else:
#                 print("输入错误，再试一次吧~")
#         else:
#             print("输入错误，再试一次吧~")

# check_input(4)
# check_input(5)
# check_input(6)

# output("=====RESTART: Python3 App running screen=====\n25\nAlice\nTrue\n")

# output("恭喜你，掌握了Python的变量和数据类型！")
# output("----------------------------------", delay=5)

# output("2. 控制结构")
# output("控制结构用于控制代码的执行流程。常见的控制结构包括条件语句（if、elif、else）和循环语句（for、while）。")

# output("2-1. if条件语句")
# output("if条件语句用于根据条件的真假来执行不同的代码块。")
# output("示例代码：\n1   age = 20\n2   if age >= 18:\n3       print(\"You are an adult!\")", delay=0)
# string = input("试一试吧~\n1   ")
# while string.strip() != "age = 20":
#     string = input("输入错误，再试一次吧~\n1   ")
# string = input("2   ")
# while string.strip() != "if age >= 18:" and string.strip() != "if age>=18:":
#     string = input("输入错误，再试一次吧~\n2   ")
# string = input("3   ")
# while string != "    print(\"You are an adult!\")" and string.strip() != "    print('You are an adult!')":
#     string = input("输入错误，再试一次吧~\n3   ")
# output("=====RESTART: Python3 App running screen=====\nYou are an adult!\n")
# output("代码说明：\n1. 定义了一个变量age并赋值为20。\n2. 使用if语句检查age是否大于或等于18。\n3. 如果条件为真，执行print语句输出\"You are an adult!\"。")
# output("恭喜你，掌握了if条件语句！")

# output("2-2. if-else条件语句")
# output("if-else条件语句用于在条件为假时执行另一个代码块。")
# output("示例代码：\n1   age = 20\n2   if age >= 18:\n3       print(\"You are an adult!\")\n4   else:\n5       print(\"You are a minor!\")", delay=0)
# string = input("试一试吧~\n1   ")
# while string.strip() != "age = 20":
#     string = input("输入错误，再试一次吧~\n1   ")
# string = input("2   ")
# while string.strip() != "if age >= 18:" and string.strip() != "if age>=18:":
#     string = input("输入错误，再试一次吧~\n2   ")
# string = input("3   ")
# while string != "    print(\"You are an adult!\")" and string.strip() != "    print('You are an adult!')":
#     string = input("输入错误，再试一次吧~\n3   ")
# string = input("4   ")
# while string.strip() != "else:":
#     string = input("输入错误，再试一次吧~\n4   ")
# string = input("5   ")
# while string != "    print(\"print('You are a minor!')\")" and string.strip() != "    print('You are a minor!')":
#     string = input("输入错误，再试一次吧~\n5   ")

# output("=====RESTART: Python3 App running screen=====\nYou are an adult!\n")
# output("代码说明：\n1. 定义了一个变量age并赋值为20。\n2. 使用if语句检查age是否大于或等于18。\n3. 如果条件为真，执行print语句输出\"You are an adult!\"。\n4. 如果条件为假，执行else块中的print语句输出\"You are a minor!\"。")
# output("恭喜你，掌握了if-else条件语句！")