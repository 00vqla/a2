
PerfectMark = 0
ClassSize = 10
StudentMark = [60, 70, 65, 70, 75, 80, 85, 100, 95, 100]

for Counter in range(ClassSize):
    if StudentMark[Counter] == 100:
        PerfectMark += 1

print("Perfect Mark:", PerfectMark)