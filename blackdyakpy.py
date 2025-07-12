
import random
import sys

class Player:
    
    def __init__(self, name):
        self.name = name
        self.cards = []
        #idk if putting cards.sum here would update along with the cards.
    #def draw(self):
    #I mean, we don't have to make another instance of this
    def calculate(self, amount=0):
        #calculate the total score based on the hand cards
        #we set 0 total so we calculate from scartch
        self.total = 0
        if amount==0: #then calculte everything
            for card in self.cards:
                if card[1:].isdigit():
                    self.total += int(card[1:])
                else: #it's a human, so 10
                    self.total += 10
        else: #we could put this as a cleaner way in the future
            for card in self.cards[:amount]:
                if card[1:].isdigit():
                    self.total += int(card[1:])
                else: #it's a human, so 10
                    self.total += 10
        return self.total
    
    def show_cards(self, amount=5):
        #dealer always has 5 minimum revealed, or 1 in vanilla blackjack
        return_me = self.cards[:amount]
        [return_me.append("X") for x in range((len(self.cards) - amount))]
        return return_me

    def addcards(self, cards):
        #ex
        #dealer.addcards(deck.draw(5))
        #cards would be an array
        [self.cards.append(x) for x in cards]

class Deck:

    def __init__(self):
        """
        initialize the instance to generate cards
        """
        #populate the deck first
        self.cards = []
        suites = ["\u2660", "\u2665","\u2666","\u2663"]
        hoomans = ["KANG", "QUEEN", "JACK", "ACE"]
        [self.cards.append(x+str(y)) for x in suites for y in range(1,11)]
        [self.cards.append(x+str(y)) for x in suites for y in hoomans]

    def draw(self, amount):
        #mayeb we should just let draw return a card, one at a time and iterate the amount 
        #through the main logic
        #someday
        print("Drawing {} cards".format(amount))
        #you can go all freedom mode and just draw as much as you want boo :*
        card_drawn = []
        #pop cards from deck with how much amount
        #[card_drawn.append(self.cards.pop(random.randrange(len(self.cards))) for x in range(amount))]
        for x in range(amount):
            card_drawn.append(self.cards.pop(random.randrange(len(self.cards))))
        return card_drawn

def rolldice():
    return (random.randint(1,6))

def clear():
    #ctrl L os independent clear screen
    sys.stdout.write("\033[H\033[2J")

def main():
    #i couldhave put the draw cards on a method, it wouldhave been nice
    #I could have put show cards as a method in player as well lol
    print("\nWelcome to revamped blackjack!!\nA minimalist blackjack game to sham " \
    "around your work area :)) ")
    print("Unlike a traditonal blackjack, the goal of this one is to reach or get close to 69\n")
    #i knew printing it on one docstring would mess it up
    print("""Rules:\nDealer initial 5 cards first, which he reveals """)
    print("Player would then, draw 5 cards,")
    print("Dealer would then draw the 4 remianing hidden cards")
    print("Player can throw a dice, and draw the amount of cards as a result.")
    print("As a reward, player can reveal two of the dealers cards, but only once")
    print("Player can draw as much cards as he like depending on how much guts he has, but if you go over 69")
    print("The game would automatically show hands and if both of you bust")
    print("Dealer automatically wins if you bust")

    #future versions would include an actual bet lol

    #reading some articles, the Europeans do not have a hole card
    #dealer draws that hole card after everyone else gets their card or something
    #but we're merican's so we go by our rules as what the founding fathers intended
    score = 0
    dscore= 0
    playername = 'aa'#str(input("What should we call you? "))

    input("Press any key to start the game!")
    #this would be the main loop
    while True:
    #start intializing game environment
        #we initialize variables again
        reveal_card = 5
        player = Player(name=playername)
        dealer = Player(name="Dealer")
        deck = Deck()
     
        clear()
        #first initial dealer draw
        print("Inital dealer draw...")   
        dealer.addcards(deck.draw(5))
        print("Dealer cards {}: {} Total:{}".format(len(dealer.cards),dealer.cards, dealer.calculate()))
        
        #initial player draw
        print("Initial player draw...")
        player.addcards(deck.draw(5))
        print("Player cards {}: {} Total:{}".format(len(player.cards), player.cards, player.calculate()) )
        
        #dealer final draw
        print("Dealer draws remaining cards") 
        dealer.addcards(deck.draw(5))
    #end of initial game phase
        
        while True:
            if (player.calculate() > 69):
                clear()
                print("You busted! {}\nGrand Total of:{}".format(player.show_cards(amount=len(player.cards))  ,player.calculate(amount=len(player.cards))))
                print("Dealer cards {}: {} Total:{}".format(len(dealer.cards),dealer.show_cards(amount=len(dealer.cards)), dealer.calculate(amount=len(dealer.cards))))
                dscore += 1
                print("Score: Player:{}\t Dealer:{}".format(str(score), str(dscore)))
                input("Press any key to continue:")
                break
        #start game
            clear()
            print("Dealer cards {}: {} Total:{}".format(len(dealer.cards),dealer.show_cards(amount=reveal_card), dealer.calculate(amount=reveal_card)))
            print("Your cards {}: {} Total:{}".format(len(player.cards),player.show_cards(len(player.cards)), player.calculate()))

            while True:
            #start get input loop
                try:
                    decision = int(input("\nWhat would be your move? \n1. Draw a card. \n2. Roll the dice. \n3. Show hands. \n99. to exit:"))
                    clear()
                    break
                except ValueError:
                    print("Invalid choice, please enter 1, 2, or 3, or 99")
                except KeyboardInterrupt:
                    print("\nThanks for playing! :**")
                    exit()
            #end get input loop
            match decision:
                case 1:
                    print("Drawing ONE card...")
                    #[player.cards.append(x) for x in deck.draw(1)]
                    player.addcards(deck.draw(1))
                case 2:
                    diceroll = rolldice()
                    print("Rolling dice!...{}!".format(diceroll))
                    #[player.cards.append(x) for x in deck.draw(diceroll)]
                    player.addcards(deck.draw(diceroll))
                    reveal_card = 7
                case 3: 
                    print("Dealer cards {}: {} Total:{}".format(len(dealer.cards),dealer.show_cards(amount=len(dealer.cards)), dealer.calculate(amount=len(dealer.cards))))
                    print("Your cards {}: {} Total:{}".format(len(player.cards),player.show_cards(len(player.cards)), player.calculate()))
                    if (dealer.calculate() > 69):
                        print("You caught the dealer busting!")
                        print("You won!")
                        score += 1
                    elif (player.calculate() > dealer.calculate()):
                        print("You won!")
                        score += 1
                    else:
                        print("You lose!")
                        dscore += 1
                    print("Score: Player:{}\t Dealer:{}".format(str(score), str(dscore)))
                    input("Press any key to continue")
                    break
                case 99:
                    print("Thanks for playing :**")
                    exit()
        
        #endgame loop

if __name__ == "__main__":
    main()