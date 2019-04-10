import random


class Card:
    """
    Card Object

    Contains the Face, Suit, and Value of a Card
    """
    value_map = list(range(2, 11))+["Jack", "Queen", "King", "Ace"]
  
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        self.value = self.value_map.index(face)
  
    def __str__(self):
        return str(self.face) + " of " + self.suit


def main():
    player1, player2 = (lambda deck:
                        (deck[:len(deck) // 2], deck[len(deck) // 2:])
                        )((lambda deck:
                           random.sample(deck, len(deck)))(
        [Card(face, suit)
         for suit in ["Diamonds", "Spades", "Clubs", "Hearts"]
         for face in list(range(2, 11)) + ["Jack", "Queen", "King", "Ace"]]))

    def battle():
        print("Both players declare war!\n")
        down1, down2 = [], []

        while (len(down1) is 0 and len(down2) is 0) or down1[0].value == down2[0].value:
            for x in range(4):
                down1.insert(0, player1.pop(0))
                down2.insert(0, player2.pop(0))

                if len(player1) < 1 or len(player2) < 1:
                    return True

            print("Player1: " + str(down1[0]))
            print("Player2: " + str(down2[0]))

        if down1[0].value > down2[0].value:
            player1.extend(down1)
            player1.extend(down2)
            print("Player 1 won the war\n")

        elif down1[0].value < down2[0].value:
            player2.extend(down1)
            player2.extend(down2)
            print("Player 2 won the war\n")

        return False

    temp = input("\nPress enter to start war")
    while len(player1) > 0 and len(player2) > 0:

        print("Player 1: "+str(player1[0]))
        print("Player 2: "+str(player2[0]))

        if player1[0].value > player2[0].value:
            print("Both players draw, but Player 1 has taken Player 2's card\n")
            player1.append(player2.pop(0))
            player1.append(player1.pop(0))

        elif player1[0].value < player2[0].value:
            print("Both players draw, but Player 2 has taken Player 1's card\n")
            player2.append(player1.pop(0))
            player2.append(player2.pop(0))

        elif player1[0].value == player2[0].value:
            if battle():
                break

        if temp is not "fast":
            input("Press enter to view the next duel")

    print(f"Player {'1' if len(player2) < 1 else '2'} has won")

    input("Press enter to finish")
