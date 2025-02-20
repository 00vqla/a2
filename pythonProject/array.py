# py program for lin search
# create array to store all the numbers
myList = [2, 312, 45, 51, 90]

# enter item to search for
item = int(input("Please enter item to be found: "))
found = False
for index in range(len(myList)):
    if(myList[index] == item):
        found = True
if(found):
    print("Item found.")
else:
    print("Not found.")