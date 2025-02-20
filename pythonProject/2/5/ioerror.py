try:
    with open("not_here.txt", "r") as f:
        f.write("hello world")
except IOError as e:
    print("An error occurred:", e)

try:
    f = open("myfile.txt", "w")
    f.write("monkey")
except IOError as e:
    print("error", IOError)
finally:
    print("monkey")