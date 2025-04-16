class TreasureChest:
    def __init__(self, q, ans, pts):
        self.__question = q  # STRING
        self.__answer = ans  # INTEGER
        self.__points = pts  # INTEGER

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, userans):
        if int(self.__answer) == userans:
            return True
        else:
            return False

    def getPoints(self, att):
        if att == 1:
            return self.__points
        elif att == 2:
            return self.__points // 2
        elif att == 3 or att == 4:
            return self.__points // 4
        else:
            return 0


arrayTreasure = []


def readData():
    try:
        f = open("TreasureChestData.txt", "r")
        line = f.readline().strip()
        while line != "":
            q = line
            ans = f.readline().strip()
            pts = f.readline().strip()
            arrayTreasure.append((TreasureChest(str(q), int(ans), int(pts))))
            line = f.readline().strip()
        f.close()
    except IOError:
        print("file not found")


readData()
qnum = int(input("Enter a question number, 1~5: "))
print(f"{arrayTreasure[qnum - 1].getQuestion()}")
correct = False
global atts
atts = 1
while not correct:
    useranswer = int(input("enter your answer: "))
    if arrayTreasure[qnum - 1].checkAnswer(useranswer):
        correct = True
    else:
        atts += 1
        correct = False

print(arrayTreasure[qnum - 1].getPoints(atts))
