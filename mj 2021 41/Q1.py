class node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode


linkedList = []
linkedList.append(node(1, 1))
linkedList.append(node(5, 4))
linkedList.append(node(6, 7))
linkedList.append(node(7, -1))
linkedList.append(node(2, 2))
linkedList.append(node(0, 6))
linkedList.append(node(0, 8))
linkedList.append(node(56, 3))
linkedList.append(node(0, 9))
linkedList.append(node(0, -1))
startPointer = 0
emptyList = 5


def outputNodes(array, pointer):
    while pointer != -1:
        print(array[pointer].data)
        pointer = array[pointer].nextNode


outputNodes(linkedList, startPointer)


def addNode(array, pointer, emptyList):
    newdata = input("input the data to be added to the end: ")
    if emptyList < 0 or emptyList > 9:
        return False
    else:
        newnode = node(int(newdata), -1)
        array[emptyList] = newnode

        emptyList = linkedList[emptyList].nextNode

        return True


outputNodes(linkedList, startPointer)
if addNode(linkedList, startPointer, emptyList):
    print("new data added")
else:
    print("list full")
outputNodes(linkedList, startPointer)
