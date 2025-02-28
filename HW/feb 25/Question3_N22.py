Queue = [0] * 100
head = 0
tail = 0


def Enqueue(value):
    global tail, Queue, head
    if tail < 100:
        Queue[tail] = value
        tail += 1
        head = value
        return True
    else:
        return False


for i in range(1, 21):
    Enqueue(i)
if Enqueue(i):
    print("Successful")
else:
    print("Unsuccessful")


def IterativeOutput(start):
    global head, tail, Queue
    total = 0
    if start == 0:
        return Queue[start]
    else:
        return total + IterativeOutput(start)

IterativeOutput(2)