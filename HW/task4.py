# Task 1.6a
Animal = []
Colour = []
AnimalTopPointer = 0
ColourTopPointer = 0


def PushAnimal(DataToPush):
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer += 1
        return True


# Task 1.6b
def PopAnimal():
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData.append(Animal[AnimalTopPointer - 1])
        AnimalTopPointer -= 1
        return ReturnData


# Task 1.6c
VPointer = 0
CPointer = 0
StackVowel = []
StackConsonant = []


def PushData(letter):
    global StackVowel
    global StackConsonant
    global VPointer
    global CPointer
    v = 'aiueo'
    if letter in v:
        if VPointer == 50:  # VStack full
            print("Stack is full")
        else:
            StackVowel.append(letter)
            VPointer += 1
    else:
        if CPointer == 50:  # CStack full
            print("Stack if full")
        else:
            StackConsonant.append(letter)
            CPointer += 1

# Task 1.6d


def PopVowel():
    global VPointer
    global StackVowel
    if VPointer == 0:
        return "No Data"
    else:
        VPointer -= 1
        StackVowel.pop()
        return StackVowel[VPointer]


def PopConsonant():
    global CPointer
    global StackConsonant
    if CPointer == 0:
        return "No Data"
    else:
        CPointer -= 1
        StackConsonant.pop()
        return StackConsonant[VPointer]

# Task 2.6 a


Queue = []  # array of 50 strings
HeadPointer = -1
TailPointer = 0


def Enqueue(string):
    global Queue, HeadPointer, TailPointer

    # queue full?
    if TailPointer >= 50:
        print("Queue is full")
    else:  # insert string
        Queue[HeadPointer] = string
        HeadPointer += 1
        if HeadPointer == -1:  # the queue is empty
            HeadPointer = 0


def Dequeue(string):
    global Queue, HeadPointer, TailPointer

    if HeadPointer == -1 or TailPointer:
        print("Queue empty")
        return "Empty"
    else:
        HeadPointer += 1  # popping by incrementing the HP, ignores the original 1st
        return Queue[HeadPointer]


