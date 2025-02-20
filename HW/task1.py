class data:
    pass


def TooMany(Search, Max):
    Count = 0
    for i in range(1, 150):
        if data[i] == Search:
            Count += 1

    if Count > Max:
        return True
    else:
        return False

