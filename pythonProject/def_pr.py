DataArray = [1, 4, 5]


def PrintArray(DataArray):
    Array_in_line = ""
    for i in range(len(DataArray)):
        Array_in_line = Array_in_line + str(DataArray[i]) + " "
    print(Array_in_line)


PrintArray(DataArray)