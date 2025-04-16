DataArray = []

try:
    f = open("Data.txt", "r")
    for line in f:
        DataArray.append(line.strip())
except IOError:
    print('file not found')


def PrintArray(Array):
    newline = ""
    for x in range(0, len(Array)):
        newline += str(DataArray[x]) + " "
    print(newline)


PrintArray(DataArray)


def LinearSearch(Array, Search):
    count = 0
    for x in range(0, len(Array)):
        if int(Array[x]) == Search:
            count += 1
    return count


Valid = False
while Valid == False:
    a = input("input number between 0 and 100: ")
    if int(a) < 100 and int(a) > 0:
        Valid = True

c = LinearSearch(DataArray, int(a))

print(f"The number {a} is found {c} times")
