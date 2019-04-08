import random
faces = list(range(2, 11))+["Jack", "Queen", "King", "Ace"]


class Card:
    """
    Card Object

    Contains the Face, Suit, and Value of a Card
    """
  
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        self.value = faces.index(face)
  
    def __str__(self):
        return str(self.face) + " of " + self.suit


cards = [Card(face, suit)
         for suit in ["Diamonds", "Spades", "Clubs", "Hearts"]
         for face in faces]


random.shuffle(cards)
player1, player2 = [], []

testing = False

for i in range(int(len(cards)/2)):
    player1.append(cards.pop(0))
    player2.append(cards.pop(0))


def war():
    print("Both players declare war!\n")
    down1, down2 = [], []

    while (len(down1) is 0 and len(down2) is 0) or down1[0].value == down2[0].value:
        for x in range(4):
            if len(player1) < 1:
                return True

            if len(player2) < 1:
                return True

            down1.insert(0, player1.pop(0))
            down2.insert(0, player2.pop(0))

        print("Player1: " + str(down1[0]))
        print("Player2: " + str(down2[0]))

    if len(player1) < 1 or len(player2) < 1:
        return True

    if down1[0].value > down2[0].value:
        player1.extend(down1)
        player1.extend(down2)
        print("Player 1 won the war\n")
        return False

    elif down1[0].value < down2[0].value:
        player2.extend(down1)
        player2.extend(down2)
        print("Player 2 won the war\n")
        return False


input("\nPress enter to start war")
while len(player1) > 0 and len(player2) > 0:
  
    print("Player1: "+str(player1[0]))
    print("Player2: "+str(player2[0]))

    if player1[0].value > player2[0].value:
        print("Both players draw, but player one has taken player two's card\n")
        player1.append(player2.pop(0))
        player1.append(player1.pop(0))

    elif player1[0].value < player2[0].value:
        print("Both players draw, but player two has taken player one's card\n")
        player2.append(player1.pop(0))
        player2.append(player2.pop(0))

    elif player1[0].value == player2[0].value:
        if war() is True:
            break

    if testing is not True:
        input("Press enter to view the next duel")

if len(player2) < 1:
    print("Player 1 has won")

else:
    print("Player 2 has won")

input("Press enter to finish")
