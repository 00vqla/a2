try:
    file = open("file_handling.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()
