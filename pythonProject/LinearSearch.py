def LinearSearch(array, target):

    for index in range(len(array)):

        if array[index] == target:
            return index
    else:
        return -1

print(LinearSearch([15, 25, 35, 45, 55], 35))
print(LinearSearch([15, 25, 35, 45, 55], 100))
