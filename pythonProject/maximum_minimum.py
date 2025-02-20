Max = 0
Min = 100
ClassSize = 5
StudentMark = [100, 12, 90, 48, 5]

for Counter in range(ClassSize):
    if StudentMark[Counter] > Max:
        Max = StudentMark[Counter]
    if StudentMark[Counter] < Min:
        Min = StudentMark[Counter]

print(Max, Min)