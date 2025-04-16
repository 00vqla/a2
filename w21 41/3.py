ArrayNodes = [[0, 0, 0] for x in range(20)]
RootPointer = -1
FreeNode = 0


def AddNode(ArrayNodes, RootPointer, FreeNode):
    NodeData = int(input("Enter node data: "))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while not Placed:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode += + 1
    else:
        print("Tree is full")
    return ArrayNodes, RootPointer, FreeNode


def PrintAll(ArrayNodes):
    for x in range(0, 20):
        print(str(ArrayNodes[x][0]),str(ArrayNodes[x][1]),str(ArrayNodes[x][2]))


for x in range(10):
    ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes, RootPointer, FreeNode)

PrintAll(ArrayNodes)