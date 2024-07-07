#card class
# Suit,Rank,Value
import random
suits = ('Hearts','Diamond','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight',
        'Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,
          'Seven':7,'Eight':8,'Nine':9,'Ten':10,
          'Jack':11,'Queen':12,'King':13,'Ace':14}
playing = True

class Card:
    def __init__(self,suit,rank):

        self.suit = suit
        self.rank = rank
        

    def __str__(self):
        return self.rank  +  " of "  +  self.suit
    
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp =''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: "+deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        #card passed in 
        #frim Deck.deal()
        self.cards.append(card)
        self.value += values[card.rank]

        #track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        #if total value > 21 and I still have an ace
        #then change my ace to be a instead have an ace
        while self.value > 21 and self.aces>0:
            self.value -= 10
            self.aces -= 1
        

class Chips:

    def __init__(self,total=100):
        self.total = total
        self.bet =0
    
    def win_bet(self):
        self.total += self.bet

    def loose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except:
            print("Sorry Please Provide an Integer!")

        else:
            if chips.bet > chips.total:
                print('Sorry,you do not have enuough chips! You have:{}'.format(chips.total))
            else: 
                break 

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input('Hit or Stand? Enter h or s')

        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("Player Stands Dealer's turn")
            playing = False

        else:
            print("Sorry, I did not understand that,Please enter h or s")
            continue

        break

def show_some(player,dealer):
    #dealer's cards[1]
    #show only one of the dealers cards
    print("\n Dealer's Hand: ")
    print("First card hidden")
    print(dealer.cards[1])

    #Show all of the (2 Cards) of the players hand/cards
    print("\n Player's Hand")
    for card in player.cards:
        print(card)


def show_all(player,dealer):
    #show all the dealers cards

    print("\n Dealer's Hand")
    for card in dealer.cards:
        print(card)
    #calculate and display value
    print(f"Value of Dealer's hand is : {dealer.value}")

    #show all the players cards
    print("\n Player's Hand")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is : {player.value}")


def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.loose_bet()
def player_wins(player,dealer,chips):
    print('PLAYER WINS!')
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print('PLAYER WINS DEALER BUSTED!')
    chips.win_bet()
def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()
def push(player,dealer):
    print('Dealer and Player tie! PUSH')



while True:
    #Print an operating statement
    print('WELCOME TO BLACKJACK')
    #Create & Shuffle the deck,deal two cards to each other
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #Setup the PLayer's chips
    player_chips = Chips()


    #Prompt the Player for their bet
    take_bet(player_chips)



    # Show Cards(but keep one dealers card hidden)
    show_some(player_hand,dealer_hand)

    while playing: #recall this variable from our hit_or_stand function

        #Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)


        #Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)


        #If player's hand exceeds 21, run player_busts() and break out of the loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

        # If player hasn't busted, play Dealer's hand until Dealer reaches 17
        
    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
                hit(deck,dealer_hand)        
            #Show all cards
        show_all(player_hand,dealer_hand)


            # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)

         
    #Inform Player of their chips total
    print('\n Player total chips are at:{}'.format(player_chips.total))
    

             
    #Ask to play again
    new_game = input("Would you like to play another hand?  y/n ")
    if new_game[0].lower()=='y':
        playing = True
        continue
    else:
        print("Thank You For Playing")
        break


















    break

            

































