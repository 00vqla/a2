list = [12, 13, 465, 65, 90]


def bubble_sort(list):
    while True:
        swapped = False
        for index in range(len(list) - 1):
            if list[index] > list[index + 1]:
                list[index], list[index + 1] = list[index + 1], list[index]
                swapped = True

        if not swapped:
            return


bubble_sort(list)

print(list)