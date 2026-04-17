import string

print("Python Shell")
print("Type exit() to exit or type help() to get tips.")

symbols = string.punctuation

functions_names = ['print',]
functions_values = [['sep=\' \'','end=\'\\n\''],]
functions_do = [print,]

text = None
while text != "exit()":
    text = input(">>> ")
    part = []
    n = 0
    for i in text:
        if i in symbols:
            pass
