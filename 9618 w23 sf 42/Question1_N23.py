StackVowel = []  # array of 100 elements
StackConsonant = []  # array of 100 elements

global VowelTop
global ConsonantTop
# declared as global variable
VowelTop = 0
ConsonantTop = 0


def PushData(val):
    global VowelTop
    global ConsonantTop
    vowel = "aiueo"
    if val in vowel:
        if VowelTop == 100:
            print("The vowel stack is full")
        else:
            StackVowel.append(val)
            VowelTop += 1
            '''print(StackVowel, VowelTop)'''
    else:
        if ConsonantTop == 100:
            print("The consonant stack is full")

        else:
            StackConsonant.append(val)
            ConsonantTop += 1
            '''print(StackConsonant, ConsonantTop)'''


def ReadData():
    try:
        f = open("StackData.txt", "r")
        for letter in f:
            PushData(letter.strip())
        f.close()
    except:
        print("File not found")


def PopVowel():
    global VowelTop
    if VowelTop - 1 >= 0:
        VowelTop -= 1
        ReturnData = StackVowel[VowelTop]
        del StackVowel[-1]
        return ReturnData
    else:
        print("No data")


def PopConsonant():
    global ConsonantTop
    if ConsonantTop == 0:
        print("No data")
    else:
        del StackConsonant[-1]
        ConsonantTop -= 1
        return StackConsonant[ConsonantTop - 1]


ReadData()
returndata = ""
for x in range(5):
    if VowelTop == 0:
        print("Vowel stack is empty")
    if ConsonantTop == 0:
        print("Consonant stack is empty")
    else:
        userinput = input("Enter vowel or consonant: ").lower()
        if userinput == "vowel":
            PopVowel()
            returnval = PopVowel()

            returndata += returnval

        elif userinput == "consonant":
            PopConsonant()
            returnval = PopConsonant()

            returndata += returnval
print(StackVowel)
print(StackConsonant)
print(returndata)
