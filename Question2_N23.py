def IterativeCalculate(Number):
    ToFind = Number
    Total = 0
    while Number != 0:
        if divmod(ToFind, Number)[1] == 0:
            Total += Number
        Number -= 1

    return Total


print(IterativeCalculate(10))


def RecursiveValue(Number, ToFind):
    if Number == 0:
        return 0
    else:
        if divmod(ToFind, Number)[1] == 0:
            return Number + RecursiveValue(Number - 1, ToFind)
        else:
            return RecursiveValue(Number - 1, ToFind)


print(RecursiveValue(50, 50))
