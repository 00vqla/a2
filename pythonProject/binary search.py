items = ["Alabama", "Cali", "Delaware", "Florida", "Georgia"]
item_to_find = input("Enter the state to find: ")

found = False
first = 0
last = len(items)-1

while first <= last and found == False:
    midpoint = (first+last)//2
    if items[midpoint] == item_to_find:
            found = True
    else:
            if items[midpoint] < item_to_find:
                first = midpoint+1
            else:
                last = midpoint-1

if found == True:
    print("Item found at position: ", midpoint+1)
else:
    print("Not found")