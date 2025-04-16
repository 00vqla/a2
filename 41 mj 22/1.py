global DataArray
DataArray = [[""] * 2 for i in range(11)]


def ReadHighScores():
    global DataArray
    try:
        f = open("HighScore.txt", "r")
        for x in range(0, 10):
            DataArray[x][0] = f.readline().lstrip('[').strip()
            DataArray[x][1] = f.readline().strip()
        f.close()
    except IOError:
        print('File not found')


ReadHighScores()


def OutputHighScores():
    global DataArray
    for x in range(0, 11):
        print(f"{DataArray[x][0]} {DataArray[x][1]}")


OutputHighScores()

PlayerValid = False
while not PlayerValid:
    PlayerName = input("Input 3 letter character name: ")
    if len(PlayerName) == 3:
        PlayerValid = True

ScoreValid = False
while not ScoreValid:
    Score = input("Input score between 1 and 100000: ")
    if 1 < int(Score) < 100000:
        ScoreValid = True

'''if ScoreValid and PlayerValid:
    for x in range(0, 10):
        pass'''


# Q1 e.ii skipped


def WriteTopTen():
    f = open("NewHighScore.txt", "w")
    for x in range(0, 10):
        f.writelines(DataArray[x][0] + "\n")
        f.writelines(DataArray[x][1] + "\n")


WriteTopTen()


