class Character:
    # Name as private string
    # XCoordinate and YCoordinate as private integer

    def __init__(self, Name, XCoordinate, YCoordinate):
        self.__Name = Name
        self.__XCoordinate = XCoordinate
        self.__YCoordinate = YCoordinate

    def GetName(self):
        return self.__Name

    def GetX(self):
        return self.__XCoordinate

    def GetY(self):
        return self.__YCoordinate

    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate += XChange
        self.__YCoordinate += YChange


Characters = []
TextFile = "Characters.txt"
try:
    File = open(TextFile, 'r')
    for X in range(0, 10):
        name = File.readline().strip()
        x = File.readline().strip()
        y = File.readline().strip()
        TempC = Character(name, int(x), int(y))
        Characters.append(TempC)
    File.close()
except:
    print("File not found")

index = -1

while index == -1:
    CharacterInput = input("Enter character to move: ").lower()
    for c in range(0, 10):
        Temp = str(Characters[c].GetName().lower())
        if Temp == CharacterInput:
            index = c
            # print(index)


while True:
    KeyInput = input("Enter a move: ").lower()
    if KeyInput == "a":
        Characters[index].ChangePosition(-1, 0)
        break
    elif KeyInput == "w":
        Characters[index].ChangePosition(-1, 0)
        break
    elif KeyInput == "s":
        Characters[index].ChangePosition(-1, 0)
        break
    elif KeyInput == "d":
        Characters[index].ChangePosition(-1, 0)
        break
    else:
        print("Invalid direction. Try again.")

print(f"{Characters[index].GetName()} has changed coordinate to x = {Characters[index].GetX()} and Y = {Characters[index].GetY()}")