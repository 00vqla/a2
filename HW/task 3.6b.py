class node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode


linkedList = [node(1,1), node(5, 4), node(6,7), node(7, -1), node(2,2), node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]
startPointer = 0
emptyList = 5


def outputNodes(linkedList, startPointer):
    while startPointer != -1:
        print(str(linkedList[startPointer].data))
        startPointer = linkedList[startPointer].nextNode


outputNodes(linkedList, startPointer)


def addNode(linkedList, startPointer, emptyList):
    newData = input("Enter the data to add: ")
    if emptyList < 0 or emptyList > 9:
        return False
    else:
        newNode = node(int(newData), -1)
        linkedList[emptyList] = (newNode)

        prevPointer = 0
        while startPointer != -1:
            prevPointer = startPointer
            startPointer = linkedList[startPointer].nextNode
        linkedList[prevPointer].nextNode = emptyList
        emptyList = linkedList[emptyList].nextNode

        return True

addNode(linkedList, startPointer, emptyList)
outputNodes(linkedList, startPointer)