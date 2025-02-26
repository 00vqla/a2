# ArrayNodes = [[-1, -1, -1]]*20
ArrayNodes = [[1, 20, 5], [2, 15, -1], [-1, 3, 9], [-1, 9, 4], [-1, 10, -1], [-1, 58, -1], [-1, -1, -1]]
FreeNodes = -6
RootPointer = 0


def SearchValue(Root, ValueToFind):
    global ArrayNodes

    if Root == -1:
        return -1
    elif ArrayNodes[Root][1] == ValueToFind:
        return Root
    elif ArrayNodes[Root][1] == -1:
        return -1

    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind)

