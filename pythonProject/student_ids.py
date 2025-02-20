student_id = [1002, 1003, 1004, 1005, 1006]
Counter = 0
id_input = int(input("Enter ID: "))
Found = False
Size = len(student_id)

while not Found and Counter < Size:
    if id_input == student_id[Counter]:
        Found = True
    else:
        Counter += 1

if Found and Counter < Size:
    print("index: ", Counter+1)
else:
    print(-1)