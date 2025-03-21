class Character:
    def __init__(self, name, x, y):
        # self._name as string
        # self._x and self._y as integer
        self._name = name
        self._x = x
        self._y = y

    def GetXPosition(self):
        return self._x

    def GetYPosition(self):
        return self._y

    def SetXPosition(self, xinput):
        if xinput + self._x > 10000:
            self._x = 10000
        elif xinput + self._x < 0:
            self._x = 0
        else:
            self._x += xinput

    def SetYPosition(self, yinput):
        if yinput + self._y > 10000:
            self._y = 10000
        elif yinput + self._y < 0:
            self._y = 0
        else:
            self._y += yinput

    def Move(self, move):
            if move == "up":
                Character.SetYPosition(self, 10)
            elif move == "down":
                Character.SetYPosition(self, -10)
            elif move == "left":
                Character.SetXPosition(self, -10)
            elif move == "right":
                Character.SetXPosition(self, 10)


Jack = Character("Jack", 50, 50)


class BikeCharacter(Character):
    def __init__(self, name, x, y):
        super().__init__(name, x, y)

    def Move(self, move):
        if move == "up":
            super().SetYPosition(20)
        if move == "down":
            super().SetYPosition(-20)
        if move == "left":
            super().SetXPosition(-20)
        if move == "right":
            super().SetXPosition(20)



Karla = BikeCharacter("Karla", 200, 50)

UserCharacter = input("Enter the character to move: ")
UserMove = input("Enter direction to move: ")
if UserCharacter.lower() == "jack":
    Jack.Move(UserMove)
    print(f"Jack's new position is X = {Jack.GetXPosition()} Y = {Jack.GetYPosition()}")
elif UserCharacter.lower() == "karla":
    Karla.Move(UserMove)
    print(f"Karla's new position is X= {Karla.GetXPosition()} Y = {Karla.GetYPosition()}")




