Data = []

def TooMany(Search, Max):
    Count = 0
    for index in range(150):
        if Data[index] == Search:
            Count += 1
        if Count>Max:
            return True
        else:
            return False

