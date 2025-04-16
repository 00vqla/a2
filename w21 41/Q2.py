class Picture:
    def __init__(self, desc, width, height, fcolour):
        self.__Description = desc
        self.__Width = width
        self.__Height = height
        self.__FrameColour = fcolour

    def GetDescription(self):
        return self.__Description

    def GetHeight(self):
        return self.__Height

    def GetWidth(self):
        return self.__Width

    def GetColour(self):
        return self.__FrameColour

    def SetDescription(self, newdesc):
        self.__Description = newdesc


PictureArray = []
for x in range(0, 100):
    PictureArray.append(Picture("", 0, 0, ""))

'''def ReadData1():
    global PictureArray
    try:
        f = open("Pictures.txt", "r")
        content = f.read().splitlines()
        count = 0
        for i in range(0, len(content)):
            desc = content[i]
            PictureArray[count] = Picture(content[i], content[i + 1], content[i + 2], content[i + 3])
            count += 1

    except IOError:
        print("File not found.")'''

count = 0


def ReadData():
    global PictureArray, count
    try:
        with open("Pictures.txt", "r") as f:
            Desc = f.readline().strip()
            while Desc != "":
                width = f.readline().strip()
                height = f.readline().strip()
                frame = f.readline().strip()
                PictureArray[count] = Picture(Desc, width, height, frame)
                Desc = f.readline().strip()
                count += 1
    except IOError:
        print("File not found")

    return count


ReadData()

framecolour = input("input of the frame: ").lower()
maxwidth = int(input("input maximum width: "))
maxheight = int(input("input maximum height: "))
for x in range(0, count):
    if int(PictureArray[x].GetWidth()) <= maxwidth and int(PictureArray[x].GetHeight()) <= maxheight and PictureArray[
        x].GetColour().lower() == framecolour:
        print(PictureArray[x].GetDescription(), PictureArray[x].GetWidth(), PictureArray[x].GetHeight())
        FoundStatus = True
        if not FoundStatus:
            print('pic not found')
