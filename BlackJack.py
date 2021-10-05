import random

suits = ('Corazones', 'Diamantes', 'Picas', 'Treboles')
ranks = ('Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez', 'Jack', 'Queen', 'King', 'As')
values = {'Dos':2, 'Tres':3, 'Cuatro':4, 'Cinco':5, 'Seis':6, 'Siete':7, 'Ocho':8, 'Nueve':9, 'Diez':10, 'Jack':10,
         'Queen':10, 'King':10, 'As':11}

playing = True
global visible
#creando class tarjeta#

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' de ' + self.suit

#creating , shuffle function and single dealing#

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list#
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = '' #strating competition deck empty#
        for card in self.deck:
            deck_comp += '\n' + card.__str__() #add each card object;s strin#
        return 'The deck has' + deck_comp
            
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

#creating a hand#

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'As':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            
          


# taking hits#

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

#player to take hits or stand#

def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input("Tu quieres [S]olicitar carta, [P]lantarte? Ingrese 's' or 'p'")
        
        if x[0].lower() == 's':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 'p':
            print("El jugador planto!! EL repatidor esta jugando.")
            playing = False

        else:
            print("Lo siento, Intente Otra vez.")
            continue
        break

#functions to display cards#

def show_some(player,dealer):
    print("\nLa mano del repartidor")
    print("<carta oculta>")
    print(' ', dealer.cards[1])
    print("\nLa mano del jugador: ", *player.cards, sep= '\n')
    print("El jugador Tiene = ", player.value)

    
    
def show_all(player,dealer):
    print("\nLa mano del repartidor:", *dealer.cards, sep="\n")
    print("La mano del repartidor =",dealer.value)
    print("\nLa mano del jugador: ", *player.cards, sep= '\n')
    print("La mano del jugador = ", player.value)

    

#functions to handle game scenarios#

def player_busts(player,dealer):
    print("Lo siento. Te pasaste. Perdiste.\n")

def player_wins(player,dealer):
    print("Felicitaciones. Ganaste\n!")

def dealer_busts(player,dealer):
    print("El repartidor se paso. Tu ganas!\n")
    
def dealer_wins(player,dealer):
    print("Lo siento, perdiste. El repartidor gano!")
    
def push(player,dealer):
    print("Lo siento, empataron. El repartidor gano!") 

#NOW FOR THE GAME
class Started():
    
    def start(self,player,dealer,play):
        global playing
        global visible
        #print('Play!!! ',play)
        #if (play):
        while True:
            # Print an opening statement
            if (player==2 and dealer==2):
                print("Bienvenido a Blackjack U Distrital.")
                visible='visible'
                # Create & shuffle the deck, deal two cards to each player
                deck = Deck()
                deck.shuffle()
                
                player_hand = Hand()
                player_hand.add_card(deck.deal())
                player_hand.add_card(deck.deal())
                
                dealer_hand = Hand()
                dealer_hand.add_card(deck.deal())
                dealer_hand.add_card(deck.deal())
                
                # Show cards (but keep one dealer card hidden)
                show_some(player_hand, dealer_hand)
                #hiddenCard=dealer_hand.cards[0]
                #hiddenCard='Cuatro de Corazones'
                #print('hiddenCard=',hiddenCard)
                print('play=',play)
                if (play==False):
                    playing=False
                    return visible
                    #break 
                print('play=',play)   
                while playing:  # recall this variable from our hit_or_stand function
                    
                    # Prompt for Player to Hit or Stand
                    hit_or_stand(deck, player_hand)
                    
                    # Show cards (but keep one dealer card hidden)
                    show_some(player_hand,dealer_hand) 
                    
                    # If player's hand exceeds 21, run player_busts() and break out of loop
                    if player_hand.value >21:
                        player_busts(player_hand, dealer_hand)

                        break

                # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
                if player_hand.value <= 21:
                    
                    while dealer_hand.value <17:
                        hit(deck, dealer_hand)
                
                    # Show all cards
                    show_all(player_hand,dealer_hand)
                    
                    # Run different winning scenarios
                    if dealer_hand.value > 21:
                        dealer_busts(player_hand,dealer_hand)

                    elif dealer_hand.value > player_hand.value:
                        dealer_wins(player_hand,dealer_hand)

                    elif dealer_hand.value < player_hand.value:
                        player_wins(player_hand,dealer_hand)

                    else:
                        push(player_hand,dealer_hand) # Si quedan emptados
                # Ask to play again
                new_game = input("Quieres jugar de nuevo? Ingrese 's' or 'n'")
                if new_game[0].lower() == 's':
                    playing = True
                    continue
                else:
                    print('Gracias Por Jugar!!! ')
                    break
            elif (player==0 and dealer==2):
                visible='visible'
                return visible        
            elif (player==1 and dealer==2):
                visible='visible'
                return visible        
            elif (player==2 and dealer==1):
                visible='Not visible'
                return visible        
            elif (player==1 and dealer==0):
                visible='Not visible'
                return visible        
            elif (player==0 and dealer==0):
                visible='Not visible'
                return visible        

    def getVisible():
        return  visible     

#play=Started()
#play.start(True)

class Sum:
    def sumar(self,a,b):
        self.a=a
        self.b=b
        return a+b