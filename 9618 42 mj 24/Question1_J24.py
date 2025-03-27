def Play():
    global WordArray, NumberWords
    print(f"The main word is {WordArray[0]} and there are {NumberWords - 1} answers")
    answer = None
    answerfound = 0
    while answer != "no":
        answer = input("Enter a word or no to quit the game: ").lower()
        FoundStatus = False
        if answer != "no":
            for x in range(NumberWords):
                if answer == WordArray[x]:
                    WordArray[x] = ""
                    answerfound += 1
                    print(f"Correct, {answerfound} answer so far")
                    FoundStatus = True
        if not FoundStatus:
            print("Incorrect")
    if answer == "no":
        percentagefound = answerfound / (NumberWords - 1) * 100
        print(f"You have found {percentagefound}% of the words")
        if percentagefound < 100:
            print("Answer missed: ")
            for x in range(NumberWords):
                if WordArray[x] != "":
                    print(WordArray[x])


def ReadWords(file):
    global WordArray, NumberWords
    try:
        with open(file, "r") as f:
            Words = f.read().strip()
            WordArray = Words.split()
            NumberWords = len(WordArray)
            Play()
    except IOError:
        print("Error occurred/file not found.")


File = input("Enter difficulty: ").lower()
FirstChar = File[0]
NewPrompt = FirstChar.upper() + File[1:len(File)] + ".txt"
ReadWords(NewPrompt)

