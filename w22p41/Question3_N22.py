ArrayNodes = [[-1 for index in range(3)] for index in range(20)]

ArrayNodes[0] = [1, 20, 5]
ArrayNodes[1] = [2, 15, -1]
ArrayNodes[2] = [-1, 3, 3]
ArrayNodes[3] = [-1, 9, 4]
ArrayNodes[4] = [-1, 10, -1]
ArrayNodes[5] = [-1, 58, -1]
ArrayNodes[6] = [-1, -1, -1]
FreeNodes = -6
RootPointer = 0

print(ArrayNodes)


def SearchValue(Root, ValueToFind):
    # if the root is -1, the value is not available in tree
    if Root == -1:
        return -1
    else:
        # if the node's value matches with the index value, return the root at its current
        if ArrayNodes[Root][1] == ValueToFind:
            return Root
        else:
            # invalid node
            if ArrayNodes[Root][1] == -1:
                return -1
    # if the current value is greater than the index value, recursively search on the left side
    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    # if the current value is smaller than the index value, recursively search on the right side
    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind)


def PostOrder(Root):
    if Root != -1:
        PostOrder(ArrayNodes[Root][0])
        PostOrder(ArrayNodes[Root][2])
        print(ArrayNodes[Root][1])


if SearchValue(RootPointer, 15) == -1:
    print("Not found")
else:
    print("Value found at ", str(SearchValue(RootPointer,  15)))
PostOrder(RootPointer)


