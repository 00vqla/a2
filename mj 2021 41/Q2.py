arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]


def linearSearch(searchval):
    global arrayData
    for x in range(0, len(arrayData)):
        if int(arrayData[x]) == int(searchval):
            return True
    return False


userinput = input("input ur val: ")
if linearSearch(int(userinput)):
    print("the value is in array")
else:
    print("value not found")
theArray = []


def bubbleSort():
    temp = 0
    for x in range(0, 10):
        for y in range(0, 9):
            if theArray[y] > theArray[y + 1]:
                temp = theArray[y]
                theArray[y] = theArray[y + 1]
                theArray[y + 1] = temp


