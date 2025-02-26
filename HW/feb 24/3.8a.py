def RecursiveVowels(Value):
    # Declare Total and LengthString as Integer. FirstCharacter as Character.
    Total = 0
    FirstCharacter = None
    LengthString = len(Value)

    for x in range(0, LengthString):
        FirstCharacter = Value[0]
        vowels = "aeuio"
        if FirstCharacter in vowels:
            Total += 1
        Value = Value[1:LengthString]
    return Total

print(RecursiveVowels("apple"))


