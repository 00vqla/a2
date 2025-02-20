class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)


def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)


def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=", ")


root = TreeNode("R")
NodeA = TreeNode("A")
NodeB = TreeNode("B")
NodeC = TreeNode("C")
NodeD = TreeNode("D")
NodeE = TreeNode("E")
NodeF = TreeNode("F")
NodeG = TreeNode("G")

root.left = NodeA
root.right = NodeB

NodeA.left = NodeC
NodeA.right = NodeD

NodeB.left = NodeE
NodeB.right = NodeF

NodeF.left = NodeG

# print("root.right.left.data:", root.right.left.data)
postOrderTraversal(root)
