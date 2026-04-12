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
    for i in text:
        if i in symbols:
            n = text.index(i)
            part.append(text[:n])
            part.append(i)
            _text = text[n+1:]
            part.append(_text)
    