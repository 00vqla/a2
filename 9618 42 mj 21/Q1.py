class Node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode


linkedList = [Node(1, 1), Node(5, 4), Node(6, 7), Node(7, -1), Node(2, 2), Node(0, 6), Node(0, 8), Node(56, 3),
              Node(0, 9), Node(0, -1)]
startPointer = 0
emptyList = 5


def outputNodes(linkedList, startPointer):
    while startPointer != -1:
        print(linkedList[startPointer].data)
        startPointer = linkedList[startPointer].nextNode


outputNodes(linkedList, startPointer)


def addNode(linkedList, startPointer, emptyList):
    newdata = input("enter new data to be added: ")
    if emptyList < 0 or emptyList > 9:  # list full
        return False
    else:
        linkedList[emptyList].data = newdata

