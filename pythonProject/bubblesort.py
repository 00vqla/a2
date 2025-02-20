# Sample data for student marks
StudentMark = [12, 12, 4, 93, 95, 43, 88, 100]

# initialize variables
First = 0
Last = len(StudentMark) - 1

# Bubble sort
while True:
    Swap = False
    for Counter in range(First, Last):
        if StudentMark[Counter] > StudentMark[Counter+1]:
    #Swapping
        Temp = StudentMark[Counter]
        StudentMark[Counter] = StudentMark[Counter+1]
        StudentMark[Counter+1] = Temp
        Swap = True
    Last -= 1 # reducing the range for each pass

    if not Swap or Last == 0:
        break

print("Sorted Student Marks:", StudentMark)
