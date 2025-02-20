Name = input("Enter name: ")
Found = False
Counter = 0
ClassSize = 7
StudentName = ["Ali", "Zak", "Bb", "k", "ZZ", "Ji", "Lyn"]

while not Found and Counter > ClassSize:
    if Name == StudentName[Counter]:
        Found = True
    else:
        Counter += 1

if Found:
    print(Name, "found at position", Counter+1, "in the line.")
else:
    print(Name, "not found.")
