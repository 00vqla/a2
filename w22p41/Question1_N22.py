DA = [0] * 100


def ReadFile():
    global DA
    try:
        TextFile = "IntegerData.txt"
        with open(TextFile, "r") as File:
            Lines = File.readlines()
            for X in range(min(100, len(Lines))):
                DA[X] = int(Lines[X].strip())
    except IOError:
        print("Error occurred/file not found.")


def FindValues():
    global DA

    ToFind = -1

    while ToFind < 1 or ToFind > 100:
        ToFind = int(input("Enter a number between 1 to 100: "))
        Total = 0
        for x in range(100):
            if DA[x] == ToFind:
                Total += 1
        return Total

ReadFile()
print("The number appears " + str(FindValues()) + " times")

def BubbleSort():

    global DA

    N = 100
    for i in range(N-1):
        for j in range(0, N-i-1):
            if DA[j] > DA[j+1]:
                DA[j], DA[j+1] = DA[j+1], DA[j]
    print(DA)

BubbleSort()
