global Queue, HeadPointer, TailPointer

Queue = []
HeadPointer = -1
TailPointer = 0


def Enqueue(item):
    global Queue, HeadPointer, TailPointer
    if len(Queue) == 50:
        print("Full queue")
    else:
        Queue.append(item)
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0


def Dequeue():
    global Queue, HeadPointer, TailPointer
    if HeadPointer == -1 or TailPointer == 0:
        print("Queue empty")
    else:
        HeadPointer += 1
        return Queue[HeadPointer - 1]


def ReadData():
    global Queue, HeadPointer, TailPointer
    try:
        with open("QueueData.txt", "r") as f:
            for line in f:
                Enqueue(int(line.strip()))
    except IOError:
        print("File couldn't be read")


class RecordData:

    # self.ID as string
    # self.Total as integer
    def __init__(self, ID, Total):
        self.ID = ID
        self.Total = Total

    def SetID(self, Value):
        self.ID = Value

    def GetID(self):
        return self.ID

    def SetTotal(self, Value):
        self.Total = Value

    def GetTotal(self):
        return self.Total


global Records
# Records as array of 50 elements of RecordData
Records = []
NumberRecords = 0


def TotalData():
    global RecordData, NumberRecords, Records
    Flag = False
    DataAccessed = Dequeue()

    if NumberRecords == 0:
        Records.append(RecordData(DataAccessed, 1))
        NumberRecords += 1
        Flag = True
    else:
        for x in range(0, NumberRecords):
            if Records[x].GetID() == DataAccessed:
                Records[x].SetTotal(Records[x].GetTotal() + 1)
                Flag = True
    if not Flag:
        Records.append(RecordData(DataAccessed, 1))
        NumberRecords += 1


def OutputRecords():
    for x in range(0, NumberRecords):
        print(f"ID {Records[x].GetID()} Total {Records[x].GetTotal()}")


ReadData()
while HeadPointer != TailPointer:
    TotalData()
    OutputRecords()