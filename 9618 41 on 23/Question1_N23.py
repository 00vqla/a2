def IterativeVowels(Value):
    Total = 0
    LengthString = len(Value)
    for x in range(0, LengthString - 1):
        FirstCharacter = Value[0]
        if FirstCharacter == "a" or FirstCharacter == "e" or FirstCharacter == "i" or FirstCharacter == "o" or FirstCharacter == "u":
            Total += 1

        Value = Value[1:LengthString - 1]

    return Total


print(IterativeVowels("house"))  # returns 2


def RecursiveVowels(Value):
    if len(Value) == 0:
        return 0
    else:
        First = Value[0]
        Vowels = "aiueo"
        if First in Vowels:
            return 1 + RecursiveVowels(Value[1:len(Value)])
        else:
            return RecursiveVowels(Value[1:len(Value)])


print(RecursiveVowels("imagine"))
