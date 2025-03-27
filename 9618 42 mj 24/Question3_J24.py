NumberArray = [100, 85, 644, 22, 15, 8, 1]


def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements - 1)
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2
    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    elif IntegerArray[CheckItem] < LastItem:
        LoopAgain = False
    while LoopAgain:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem -= 1
        if CheckItem < 0:
            LoopAgain = False
    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray


result = RecursiveInsertion(NumberArray, 7)
print("Recursive", result)


def IterativeInsertion(IntegerArray, NumberElements):
    while NumberElements > 0:
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2
        LoopAgain = True
        if CheckItem < 0:
            LoopAgain = False
        elif IntegerArray[CheckItem] < LastItem:
            LoopAgain = False
        while LoopAgain:
            IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
            CheckItem -= 1
            if CheckItem < 0:
                LoopAgain = False
            IntegerArray[CheckItem + 1] = LastItem
            NumberElements -= 1
        return IntegerArray


IterativeResult = IterativeInsertion(NumberArray, 7)
print("Iterative", IterativeResult)


def BinarySearch(IntegerArray, First, Last, ToFind):
    if First > Last:
        return -1
    mid = int((First + Last) / 2)
    if IntegerArray[mid] == ToFind:
        return mid
    elif IntegerArray[mid] > ToFind:  # ToFind is in the first half of the array
        BinarySearch(IntegerArray, First, mid, ToFind)
    else:  # ToFind is in the second half
        BinarySearch(IntegerArray, mid, Last, ToFind)
    if IntegerArray[mid] != ToFind:
        return -1


'''Bin = BinarySearch(RecursiveInsertion(NumberArray, 7), 1, 7, 644)
if Bin == -1:
    print("Not found")
else:
    print(Bin)'''

print("6")

