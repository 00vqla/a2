def bsearch(my_list, low, high, elem):
    if high >= low:
        mid = (high + low) // 2
        if my_list[mid] == elem:
            return mid
        elif my_list[mid] > elem:
            return bsearch(my_list, low, mid - 1, elem)
        else:
            return bsearch(my_list, mid + 1, high, elem)
    else:
        return -1


my_list = [5, 12, 23, 45, 49, 67, 71, 77, 82]
num = 67
print("The list is")
print(my_list)
print("Check for number:", num)
my_result = bsearch(my_list, 0, len(my_list) - 1, num)

if my_result != -1:
    print("Element found at index ", str(my_result))
else:
    print("Element not found!")
