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
# while len(parts) != 2 or parts[0].strip() != \
#                       'is_student' or not parts[1].strip().lower() in ['true', 'false']:
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
# output("格式：\nif 条件:\n    代码块\n")
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
# output("代码说明：\n1. 定义了一个变量age并赋值为20。\n2. 使用if语句检查age是否大于或等于18。" + \
#        "\n3. 如果条件为真，执行print语句输出\"You are an adult!\"。")
# output("恭喜你，掌握了if条件语句！")
# output("----------------------------------", delay=5)

# output("2-2. if-else条件语句")
# output("if-else条件语句用于在条件为假时执行另一个代码块。")
# output("格式：\nif 条件:\n    代码块1\nelse:\n    代码块2\n")
# output("示例代码：\n1   age = 20\n2   if age >= 18:\n3       print(\"You are an adult!\")" + \
#        "\n4   else:\n5       print(\"You are a minor!\")", delay=0)
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
# output("----------------------------------", delay=5)

# output("2-3. if-elif-else条件语句")
# output("if-elif-else条件语句用于检查多个条件，并根据第一个满足条件的代码块执行。")
# output("格式：\nif 条件1:\n    代码块1\nelif 条件2:\n    代码块2\nelse:\n    代码块3\n")
# output("示例代码：\n1   age = 20\n2   if age < 13:\n3       print(\"You are a child!\")\n" + \
#        "4   elif age < 18:\n5       print(\"You are a teenager!\")\n" + \
#        "6   else:\n7       print(\"You are an adult!\")", delay=0)
# string = input("试一试吧~\n1   ")
# while string.strip() != "age = 20" and string.strip() != "age=20":
#     string = input("输入错误，再试一次吧~\n1   ")
# string = input("2   ")
# while string.strip() != "if age < 13:" and string.strip() != "if age<13:":
#     string = input("输入错误，再试一次吧~\n2   ")
# string = input("3   ")
# while string != "    print(\"You are a child!\")" and string.strip() != "    print('You are a child!')":
#     string = input("输入错误，再试一次吧~\n3   ")
# string = input("4   ")
# while string.strip() != "elif age < 18:" and string.strip() != "elif age<18:":
#     string = input("输入错误，再试一次吧~\n4   ")
# string = input("5   ")
# while string != "    print(\"You are a teenager!\")" and string.strip() != "    print('You are a teenager!')":
#     string = input("输入错误，再试一次吧~\n5   ")
# string = input("6   ")
# while string.strip() != "else:":
#     string = input("输入错误，再试一次吧~\n6   ")
# string = input("7   ")
# while string != "    print(\"You are an adult!\")" and string.strip() != "    print('You are an adult!')":
#     string = input("输入错误，再试一次吧~\n7   ")
# output("=====RESTART: Python3 App running screen=====\nYou are an adult!\n")
# output("代码说明：\n1. 定义了一个变量age并赋值为20。\n2. 使用if语句检查age是否小于13。\n" + \
#        "3. 如果条件为真，执行print语句输出\"You are a child!\"。\n4. 使用elif语句检查age是否小于18。\n" + \
#        "5. 如果条件为真，执行print语句输出\"You are a teenager!\"。\n" + \
#        "6. 如果前面的条件都不满足，执行else块中的print语句输出\"You are an adult!\"。")
# output("恭喜你，掌握了if-elif-else条件语句！")
# output("----------------------------------", delay=5)

# output("2-4. for循环语句")
# output("for循环语句用于遍历序列（如列表、字符串等）或者可迭代对象。")
# output("格式：\nfor 循环变量 in 循环序列:\n    代码块\n")
# output("2.4.1. 次数循环")
# output("示例代码：\n1   for i in range(5):\n2       print(i)", delay=0)
# string = input("试一试吧~\n1   ")
# while string.strip() != "for i in range(5):":
#     string = input("输入错误，再试一次吧~\n1   ")
# string = input("2   ")
# while string != "    print(i)" and string.strip() != "    print(i)":
#     string = input("输入错误，再试一次吧~\n2   ")
# output("=====RESTART: Python3 App running screen=====\n0\n1\n2\n3\n4\n")
# output("代码说明：\n1. 使用for循环和range函数创建一个循环，循环变量i从0到4。\n" + \
#        "2. 在每次循环中，使用print函数输出当前的循环变量i的值。")
# output("----------------------------------", delay=5)

# output("2.4.2. 序列循环")
# output("示例代码：\n1   fruits = [\"apple\", \"banana\", \"cherry\"]\n2   for fruit in fruits:\n3       print(fruit)", delay=0)
# string = input("试一试吧~\n1   ")
# # build a list of acceptable input variants to simplify the logic
# valid_options = [
#     'fruits = ["apple", "banana", "cherry"]',
#     'fruits=["apple", "banana", "cherry"]',
#     "fruits = ['apple', 'banana', 'cherry']",
#     "fruits=['apple', 'banana', 'cherry']",
#     'fruits=["apple",\n"banana",\n"cherry"]',
#     "fruits=['apple',\n'banana',\n'cherry']",
#     'fruits=["apple", "banana",\n"cherry"]',
#     "fruits=['apple', 'banana',\n'cherry']",
# ]

# while string.strip() not in valid_options:
#     string = input("输入错误，再试一次吧~\n1   ")
# string = input("2   ")
# while string.strip() != "for fruit in fruits:":
#     string = input("输入错误，再试一次吧~\n2   ")
# string = input("3   ")
# while string != "    print(fruit)" and string != "    print(fruit)":
#     string = input("输入错误，再试一次吧~\n3   ")
# output("=====RESTART: Python3 App running screen=====\napple\nbanana\ncherry\n")
# output("代码说明：\n1. 定义了一个列表fruits，包含三个字符串元素\"apple\"、\"banana\"和\"cherry\"。\n" + \
#        "2. 使用for循环遍历列表fruits，每次循环将当前元素赋值给变量fruit。\n" + \
#        "3. 在每次循环中，使用print函数输出当前的变量fruit的值。")
# output("恭喜你，掌握了for循环语句！")
# output("----------------------------------", delay=5)

output("2-5. while循环语句")
output("while循环语句用于在条件为真时重复执行代码块。")
output("格式：\nwhile 条件:\n    代码块\n")
output("示例代码：\n1   count = 0\n2   while count < 5:\n3       print(count)\n4       count += 1", delay=0)
string = input("试一试吧~\n1   ")
while string.strip() != "count = 0" and string.strip() != "count=0":
    string = input("输入错误，再试一次吧~\n1   ")
string = input("2   ")
while string.strip() != "while count < 5:" and string.strip() != "while count<5:":
    string = input("输入错误，再试一次吧~\n2   ")
string = input("3   ")
while string != "    print(count)" and string.strip() != "    print(count)":
    string = input("输入错误，再试一次吧~\n3   ")
string = input("4   ")
while string.strip() != "count += 1" and string.strip() != "count+=1":
    string = input("输入错误，再试一次吧~\n4   ")
output("=====RESTART: Python3 App running screen=====\n0\n1\n2\n3\n4\n")
output("代码说明：\n1. 定义了一个变量count并赋值为0。\n2. 使用while循环检查count是否小于5。\n" + \
       "3. 如果条件为真，执行循环体中的代码块：输出当前的count值，并将count的值增加1。\n4. 当count的值达到5时，条件变为假，循环结束。")
output("恭喜你，掌握了while循环语句！")
output("----------------------------------", delay=5)