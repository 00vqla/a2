DA = [0 for i in range(100)]

def ReadFile():
    global DA:
    try:
        TextFile = "IntegerData.txt"
        with open(TextFile, "r") as F
            Lines = F.readlines()
            for x in range

def BubbleSort():

    global DA
    for i in range(99):
        for j in range(0, 99-i):
            if DA[j] > DA[j+1]:
                DA[j], DA[j+1] = DA[j+1], DA[j]
    print(DA)