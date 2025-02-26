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
        Name = File.readline().strip()
        XCoord = File.readline().strip()
        YCoord = File.readline().strip()
        TempC = Character(Name, int(XCoord), int(YCoord))
        Characters.append(TempC)
    File.close()
except:
    print("File not found")