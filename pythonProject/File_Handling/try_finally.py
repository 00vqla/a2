try:
    print(x)
except NameError:
    print("variable not defined")
except:
    print("some other error")

try:
    print("Hello")
except:
    print("error occurred")
else:
    print("no error")