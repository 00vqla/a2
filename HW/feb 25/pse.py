def GetStat():
    pass


Flag = GetStat()

while Flag = False:
    for Port in range(3):
        Reset(Port)
    Flag = GetStat()

