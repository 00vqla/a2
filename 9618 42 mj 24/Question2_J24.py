class Node:
    def __init__(self, Data):
        self._LeftPointer = -1  # integer
        self._Data = Data
        self._RightPointer = -1  # integer

    def GetLeft(self):
        return self._LeftPointer

    def GetRight(self):
        return self._RightPointer

    def GetData(self):
        return self._Data

    def SetLeft(self, val):
        self._LeftPointer = val

    def SetRight(self, val):
        self._RightPointer = val

    def SetData(self, val):
        self._Data = val


class TreeClass:
    def __init__(self):
        self._FirstNode = -1
        self._NumberNodes = 0
        self._Tree = []
        for x in range(20):
            self._Tree.append(Node(-1))

    def InsertNode(self, NewNode):
        if self._NumberNodes == 0:
            self._Tree[self._NumberNodes] = NewNode
            self._NumberNodes += 1
            self._FirstNode = 0
        else:
            self._Tree[self._NumberNodes] = NewNode
            NodeAccess = self._FirstNode
            Direction = ""

            while NodeAccess != -1:
                Previous = NodeAccess
                if NewNode.GetData() < self._Tree[NodeAccess].GetData():
                    NodeAccess = self._Tree[NodeAccess].GetLeft()
                    Direction = "left"
                elif NewNode.GetData() > self._Tree[NodeAccess].GetData():
                    NodeAccess = self._Tree[NodeAccess].GetRight()
                    Direction = "right"

                if Direction == "left":
                    self._Tree[Previous].SetLeft(self._NumberNodes)
                if Direction == "right":
                    self._Tree[Previous].SetRight(self._NumberNodes)
                    self._NumberNodes += 1

    def OutputTree(self):
        if self._NumberNodes == 0:
            print("No nodes")
        else:
            for x in range(0, self._NumberNodes):
                print(self._Tree[x].GetLeft(), self._Tree[x].GetData(), self._Tree[x].GetRight())


TheTree = TreeClass()
TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))
TheTree.OutputTree()


