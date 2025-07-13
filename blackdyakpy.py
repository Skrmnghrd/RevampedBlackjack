import random
import sys

class Player:
    """A player class in revamped blackjack"""
    def __init__(self, name) -> "Player":
        self.name = name
        self.cards = []
        self.total = 0
    def calculate(self, amount=0) -> int:
        """Calculates the player's hand by amount. 

        Args:
            amount (int, optional): If 0, it will calculate everything. Defaults to 0.

        Returns:
            int: self.total:  total points of the player
        """
        self.total = 0
        human_value = 10
        calculate_these_cards = self.cards

        if amount != 0:
            calculate_these_cards = self.cards[:amount]
        for card in calculate_these_cards:
            if card[1:].isdigit():
                self.total += int(card[1:])
            else:
                self.total += human_value

        return self.total
    def show_cards(self, amount=5) -> list:
        """Show's the player's hand by amount

        Args:
            amount (int, optional): Minimum amount is 5. Defaults to 5.

        Returns:
            list: self.cards: 
        """
        if amount != 0:
            player_cards = self.cards[:amount]

        [player_cards.append("X") for hidden_cards in range((len(self.cards) - amount))]
        return player_cards
    def add_cards(self, cards_drawn: list) -> None:
        """Adds cards to hand, drawn from Deck.draw() -> list

        Args:
            cards_drawn: list: 
        """
        #pylint cries [self.cards.append(x) for x in cards_drawn]
        for x in cards_drawn:
            self.cards.append(x)

class Deck:
    """Simulates a Deck of playing cards
    """
    def __init__(self):
        """Initializing an object would populate the Deck with playing cards
        """
        self.cards = []
        suites = ["\u2660", "\u2665","\u2666","\u2663"]
        hoomans = ["KANG", "QUEEN", "JACK", "ACE"]
        [self.cards.append(x+str(y)) for x in suites for y in range(1,11)]
        [self.cards.append(x+str(y)) for x in suites for y in hoomans]

    def draw(self, amount: int):
        """Method to simulate drawing a card from the deck

        Args:
            amount (int): the amount of cards to be drawn

        Returns:
            list: an array of drawn cards from the deck
        """
        print("Drawing {} cards".format(str(amount)))
        card_drawn = []
        for x in range(amount):
            card_drawn.append(self.cards.pop(random.randrange(len(self.cards))))
        return card_drawn

def roll_dice():
    """PYLINT, THIS ROLLS THE DICE

    Returns:
        int: simulated dice throw
    """
    return random.randint(1,6)
def clear():
    """Pylint, this just clears the terminal screen
    """
    #ctrl L os independent clear screen
    sys.stdout.write("\033[H\033[2J")
def main():
    """Pylint, this is main, main this is pylint
    """
    print("""Welcome to Revamped Blackjack!

    A minimalist blackjack game to sham around your work area :)) 

    Unlike traditional blackjack, the goal of this one is to reach — or get close to — 69.

    Rules:
    - The dealer draws 5 cards first and reveals them.
    - The player then draws 5 cards.
    - The dealer follows by drawing the 4 remaining hidden cards.
    - The player may throw a dice to determine how many additional cards to draw.
    - As a reward, the player can reveal two of the dealer’s hidden cards — but only once.
    - The player may draw as many cards as they dare, based on how gutsy they feel.
    - If the player goes over 69, the game will automatically reveal both hands.
    - If both the player and the dealer bust, the dealer automatically wins.
    """)

    playername = input("What should we call you?:")

    input("Press any key to start the game!")
    dscore = 0
    score = 0
    while True:
    #start intializing game environment
        reveal_card = 5
        initial_draw = 5
        player = Player(name=playername)
        dealer = Player(name="Dealer")
        deck = Deck()

        clear()
        print("Inital dealer draw...")
        dealer.add_cards(deck.draw(initial_draw))
        print("Dealer cards {}: {} Total:{}".format(len(dealer.cards),\
        dealer.cards, dealer.calculate()))
        dealer.show_cards()
        print("Initial player draw...")
        player.add_cards(deck.draw(initial_draw))
        print("Player cards {}: {} Total:{}".format(len(player.cards),\
        player.cards, player.calculate()) )
        print("Dealer draws remaining cards")
        dealer.add_cards(deck.draw(5))
    #end of initial game phase
        while True:
        #main loop
            if player.calculate() > 69:
                clear()
                print("You busted! {}\nGrand Total of:{}".format(player.show_cards(),\
                player.calculate(amount=len(player.cards))))
                print("Dealer cards {}: {} Total:{}".format(len(dealer.cards), \
                dealer.show_cards(), dealer.calculate(amount=len(dealer.cards))))
                dscore += 1
                print("Score: Player:{}\t Dealer:{}".format(str(score), str(dscore)))
                input("Press any key to continue:")
                break
        
            clear()
            print("Dealer cards {}: {} Total:{}".format(len(dealer.cards),\
            dealer.show_cards(amount=reveal_card), dealer.calculate(amount=reveal_card)))
            print("Your cards {}: {} Total:{}".format(len(player.cards),\
            player.show_cards(len(player.cards)), player.calculate()))

            while True:
            #start get input loop
                try:
                    decision = int(input("\nWhat would be your move?\n1. Draw a card." \
                    "\n2. Roll the dice. \n3. Show hands. \n99. to exit:"))
                    clear()
                    break
                except ValueError:
                    print("Invalid choice, please enter 1, 2, or 3, or 99")
                except KeyboardInterrupt:
                    print("\nThanks for playing! :**")
                    sys.exit()
            #end get input loop
            match decision:
                case 1:
                    print("Drawing ONE card...")
                    player.add_cards(deck.draw(1))
                case 2:
                    diceroll = roll_dice()
                    print("Rolling dice!...{}!".format(diceroll))
                    player.add_cards(deck.draw(diceroll))
                    reveal_card = 7
                case 3:
                    print("Dealer cards {}: {} Total:{}".format(\
                    len(dealer.cards),\
                    dealer.show_cards(),\
                    dealer.calculate(amount=len(dealer.cards))))

                    print("Your cards {}: {} Total:{}".format(len(player.cards),\
                    player.show_cards(), player.calculate()))

                    if dealer.calculate() > 69:
                        print("You caught the dealer busting!")
                        print("You won!")
                        score += 1
                    elif (player.calculate() > dealer.calculate()):
                        print("You won!")
                        score += 1
                    else:
                        print("You lose!")
                        dscore += 1
                    print("Score: Player:{}\t Dealer:{}".format(str(score),\
                    str(dscore)))
                    input("Press any key to continue")
                    break
                case 99:
                    print("Thanks for playing :**")
                    sys.exit()
        #end main loop

if __name__ == "__main__":
    main()
