Animal = []  # array of 20 elements of STRING
Colour = []  # array of 10 elements of STRING
AnimalTopPointer = 0
ColourTopPointer = 0


def PushAnimal(DataToPush):
    global AnimalTopPointer, Animal
    if AnimalTopPointer == 20:
        return False
    else:
        Animal.append(DataToPush)
        AnimalTopPointer += 1
        return True


def PopAnimal():
    global Animal, AnimalTopPointer
    ReturnData = ""
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData


def PushColour(DataToPush):
    global Colour, ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour.append(DataToPush)
        ColourTopPointer += 1
        return True


def PopColour():
    global Colour, ColourTopPointer
    ReturnData = ""
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData


def ReadData():
    try:
        f = open("AnimalData.txt", "r")
        for x in f:
            PushAnimal(x.split())
        f.close()
        f2 = open("ColourData.txt", "r")
        for x in f2:
            PushColour(x.split())
        f2.close()
    except IOError:
        print("File not found")


def OutputItem():
    global AnimalTopPointer, Animal, Colour, ColourTopPointer
    a = PopAnimal()
    c = PopColour()
    if c == "":
        PushAnimal(a)
        print("No colour")
    if a == "":
        PushColour(c)
        print("No Animal")
    else:
        newC = str(c).lstrip('[').rstrip(']').replace("'", "")
        newA = str(a).lstrip('[').rstrip(']').replace("'", "")
        print(newC, newA)


ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()
