class Vehicle:
    def __init__(self, id, max, inc):
        self._ID = id  # STRING
        self._MaxSpeed = max  # INTEGER
        self._IncreaseAmount = inc  # INTEGER
        self._HorizontalPosition = 0
        self._CurrentSpeed = 0

    def GetCurrentSpeed(self):
        return self._CurrentSpeed

    def GetIncreaseAmount(self):
        return self._IncreaseAmount

    def GetMaxSpeed(self):
        return self._MaxSpeed

    def GetHorizontalPosition(self):
        return self._HorizontalPosition

    def SetCurrentSpeed(self, newS):
        self._CurrentSpeed = newS

    def SetHorizontalPosition(self, newH):
        self._HorizontalPosition = newH

    def IncreaseSpeed(self):
        self._CurrentSpeed += self._IncreaseAmount
        self._HorizontalPosition += self._CurrentSpeed

    def Output(self):
        print(f"Current position: {self._HorizontalPosition}")
        print(f"Current speed: {self._CurrentSpeed}")


class Helicopter(Vehicle):
    def __init__(self, id, max, inc, vertchange, maxheight):
        self._VerticalPosition = 0  # INTEGER
        self._VerticalChange = vertchange  # INTEGER
        self._MaxHeight = maxheight  # INTEGER
        super().__init__(id, max, inc)

    def IncreaseSpeed(self):
        self._VerticalPosition += self._VerticalChange
        self._CurrentSpeed += self._IncreaseAmount
        self._HorizontalPosition += self._CurrentSpeed

    def Output(self):
        print(f"Current horizontal position: {self._HorizontalPosition}")
        print(f"Current vertical position: {self._VerticalPosition}")
        print(f"Current speed: {self._CurrentSpeed}")


Tiger = Vehicle("Tiger", 100, 20)
Lion = Helicopter("Lion", 350, 40, 3, 100)
Tiger.IncreaseSpeed()
Tiger.IncreaseSpeed()
Tiger.Output()
print("")
Lion.IncreaseSpeed()
Lion.IncreaseSpeed()
Lion.Output()
