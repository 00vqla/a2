class Card:
    def __init__(self, Number, Colour):
        # Number declared as integer
        # Colour declared as string
        self.__Number = Number
        self.__Colour = Colour
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour




Red1 = Card(1, "red")
Red2 = Card(2, "red")
Red3 = Card(3, "red")
Red4 = Card(4, "red")
Red5 = Card(5, "red")

Blue1 = Card(1, "blue")
Blue2 = Card(2, "blue")
Blue3 = Card(3, "blue")
Blue4 = Card(4, "blue")
Blue5 = Card(5, "blue")

Yellow1 = Card(1, "yellow")
Yellow2 = Card(2, "yellow")
Yellow3 = Card(3, "yellow")
Yellow4 = Card(4, "yellow")
Yellow5 = Card(5, "yellow")


class Hand:
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        # FirstCard and NumberCards declared as Integer
        # Cards[10] as Card

        self.__Cards = [Card1, Card2, Card3, Card4, Card5]
        self.__FirstCard = 0
        self.__NumberCards = 5

    def GetCard(self, index):
        return self.__Cards[index]


player1 = Hand(Red1, Red2, Red3, Red4, Yellow1)
player2 = Hand(Yellow2, Yellow3, Yellow4, Yellow5, Blue1)


def CalculateValue(Player):
    score = 0
    for i in range(5):
        current_card = Player.GetCard(i)
        if current_card.GetColour() == "red":
            score += 5
        elif current_card.GetColour() == "blue":
            score += 10
        elif current_card.GetColour() == "yellow":
            score += 15
        score += current_card.GetNumber()
    return score


Score1 = CalculateValue(player1)
Score2 = CalculateValue(player2)

if Score1 > Score2:
    print("Player 1 won", Score1)
elif Score1 < Score2:
    print("Player 2 won", Score2)
else:
    print("tie")
