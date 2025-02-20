def BinarySearch(array, target):
    low, high = 0, len(array)-1
    while low <= high:
        mid = (low+high)//2
        if array[mid] == target:
            return mid
        elif array[mid] >target:
            high = mid -1
        else:
            low = mid + 1
    return -1


array = [10, 20, 30, 40, 50]
target = 10

print(BinarySearch(array, target))
