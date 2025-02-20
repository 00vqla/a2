ClassSize = 5
StudentMark = [10, 20, 30, 90, 100]
Total = 0

for Counter in range(ClassSize):
    Total += StudentMark[Counter]

avg = Total/ClassSize

print(avg)