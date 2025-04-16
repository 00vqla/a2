class Balloon:
    def __init__(self, item, col):
        self.__Health = 100  # INTEGER
        self.__Colour = col  # STRING
        self.__DefenceItem = item  # STRING

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self, val):
        self.__Health += val

    def ReturnHealth(self):
        return self.__Health

    def CheckHealth(self):
        if self.__Health < 0:
            return True
        else:
            return False


DIinput = input("Input defence item: ")
CInput = input("Input colour of balloon: ")
Balloon1 = Balloon(DIinput, CInput)


def Defend(PlayerBalloon):
    OppStrength = int(input("Input the strength of opponent: "))
    PlayerBalloon.ChangeHealth(-OppStrength)
    print(PlayerBalloon.GetDefenceItem())
    if not PlayerBalloon.CheckHealth():
        print(f"Balloon left with {PlayerBalloon.ReturnHealth()} HP")
    elif PlayerBalloon.CheckHealth():
        print("Balloon has no health left")


Defend(Balloon1)
