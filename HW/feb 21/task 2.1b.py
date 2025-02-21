ArrayNodes = []


def SearchValue(root, ValueToFind):
    if root == -1:
        return -1
    elif ArrayNodes[root, 1] == ValueToFind:
        return root
    elif ArrayNodes[root, 1] == -1:
        return -1

    '''if ArrayNodes[root, 1] > ValueToFind:
        return SearchValue(ArrayNodes[root, 0], ValueToFind)

    if ArrayNodes[root, 1] < ValueToFind:
        return SearchValue(ArrayNodes[Root, 2], ValueToFind)'''
