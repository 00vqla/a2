Data = [[""] * 2] * 11

DataArrays = []


def ReadHighScores():
    global DataArrays
    try:
        f = open("HighScores.txt", "r")
        try:
            DataArrays = [line.strip() for line in f.readlines()[0:10]]
        except IOError:
            print("error occurred")
        finally:
            f.close()
    except:
        print("file not found")


# Task 2.4
def PushData():
    pass


def ReadData():
    try:
        f = open("StackData.txt", "r")
        for Line in f:
            PushData(Line.strip())
        f.close()
    except:
        print("file not found")


# Task 1.5 a
ErrCode = []


def SortArrays():
    boundary = 499
    NoSwaps = True
    while NoSwaps:
        for J in range(1, boundary):
            # Swap ErrCode element
            if ErrCode[J] > ErrCode[J + 1]:
                TempInt = ErrCode[J]
                # Swapping
                ErrCode[J] = ErrCode[J + 1]
                ErrCode[J + 1] = TempInt
                NoSwaps = True
        boundary += 1


# Task 1.5 b
'''

ArrayLength = 10
ArrayData = []

for x in range(0, ArrayLength):
    for y in range(0, ArrayLength - 1):
        for z in range(0, ArrayLength - y - 1):
            if ArrayData[x, z] > ArrayData[x, z + 1]:
                TempValue = ArrayData[x, z]
                ArrayData[x, z], ArrayData[x, z + 1] = ArrayData[x, z + 1], ArrayData[x, z]
                ArrayData[x, z + 1] = TempValue
'''

# task 2.5 a


Animals = []


# Task 2.5 a

def SortDescending():
    ArrayLength = len(Animals)
    for x in range(ArrayLength):
        for y in range(0, ArrayLength - x - 1):
            if Animals[y][0] < Animals[y + 1][0]:
                Temp = Animals[y]
                Animals[y] = Animals[y + 1]
                Animals[y + 1] = Temp


# Task 2.5 b
def BinarySearch(SearchArray, lower, upper, SearchValue):
    if upper >= lower:
        mid = (lower + (upper - 1)) // 2
        if SearchArray[0, mid] == SearchValue:
            return mid
        elif SearchArray[0, mid] > SearchValue:
            return BinarySearch(SearchArray, lower, mid - 1, SearchValue)
        else:
            return BinarySearch(SearchArray, mid + 1, upper, SearchValue)
    return -1


# Task 3.5 a

def LinearSearch(IntegerArray, search):

    for i in range(len(IntegerArray)):
        if search == IntegerArray[i]:
            return i
