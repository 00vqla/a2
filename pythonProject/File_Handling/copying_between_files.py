with open("file_a.txt", "r") as file_a:
    line_of_text = file_a.read()

with open("file_b.txt", "a") as file_b:
    file_b.write(line_of_text)
