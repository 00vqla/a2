QueueArray = ["" for x in range(10)]
HeadPointer = 0
TailPointer = 0
NumberOfItems = 0


def Enqueue(Queue, Head, Tail, NumItems, InputData):
    if NumItems >= 10:
        return False, Queue, Head, Tail, NumItems  # queue full
    Queue[Tail] = InputData
    if Tail >= 9:
        Tail = 0
    else:
        Tail += 1
    NumItems += 1
    return True, Queue, Head, Tail, NumItems


def Dequeue(Queue, Head, Tail, NumItems):
    if NumItems == 0:
        return False, Queue, Head, Tail, NumItems
    else:
        ReturnValue = Queue(Head)
        Head += 1
        if Head >= 9:
            Head = 0
        NumItems -= 1
        return ReturnValue, Queue, Head, Tail, NumItems


for x in range(11):
    a = input("Enter string value: ")
    Enqueue(QueueArray, HeadPointer, TailPointer, NumberOfItems, a)
    if not Enqueue(QueueArray, HeadPointer, TailPointer, NumberOfItems, a):
        print("Addition was unsuccessful")
    else:
        print("Addition was successful")
Dequeue(QueueArray, HeadPointer, TailPointer, NumberOfItems)
print(QueueArray[HeadPointer])
Dequeue(QueueArray, HeadPointer, TailPointer, NumberOfItems)
print(QueueArray[HeadPointer])
print(QueueArray)