ErrCode = [1,2,4,6,3,5]
ErrText = ["null","null","null","null","null","null"]


def SortArrays():
    Boundary = 499

    while NoSwaps == False:
        NoSwaps = True
        for J in range(1, Boundary):
            if ErrCode[J] > ErrCode[J+1]:
                TempInt = ErrCode[J]
                ErrCode[J] = ErrCode[J+1]
                ErrCode[J+1] = TempInt

                TempStr = ErrText[J]
                ErrText[J] = ErrText[J+1]
                ErrText[J+1] = TempStr
                NoSwaps = False
        Boundary -= 1
