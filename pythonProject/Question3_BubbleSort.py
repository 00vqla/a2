def BubbleSort(array):
    while True:
        swapped = False
        for index in range(len(array)-1):
            if list[index] > list[index+1]:
                list[index], list[index+1] = list[index+1], list[index]
                swapped = True
        if not swapped:
            return


array = [42, 23, 17, 13, 8]
BubbleSort(array)


