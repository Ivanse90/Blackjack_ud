import pytest
import random
from BlackJack import Card, hit_or_stand, Deck, Hand, dealer_wins, hit, hit_or_stand, show_some
from BlackJack import show_all, player_busts, player_wins, dealer_busts, dealer_wins, push

## pruebas para la clase Card()
@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        ("Dos","Corazones", "Dos de Corazones"),
        ("Tres","Diamantes", "Tres de Diamantes"),
        ("Queen","Picas", "Queen de Picas"),
        ("As","Treboles", "As de Treboles"),
    ]

)
def test_card(input_a,input_b,expected):
    
    assert str(Card(input_b,input_a)) == expected



## pruebas para la clase Deck()
@pytest.mark.parametrize(
    "input_a, expected",
    [
        (2, 2),
        (7,7),
        (8, 8),
        (12, 12),
    ]

)
def test_deck(input_a, expected):
    palos = ('Corazones', 'Diamantes', 'Picas', 'Treboles')
    pintas = ('Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez', 'Jack', 'Queen', 'King', 'As')
    baraja = []
    for i in palos:
        for j in pintas:
            baraja.append(j + ' de ' + i)
    carta = Deck()
    baraja2 = carta.deck
    aleatorio = random.randint(0,len(baraja2))
    
    assert str(baraja2[input_a]) == baraja[expected]

# pruebas para la clase Deck() Funion shuffle

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (0, 0),
        (15,15),
        (32, 32),
        (51, 51),
    ]

)
def test_deck_sh(input_n, expected):
    carta1 = Deck()
    inicial = str(carta1.deck[input_n])
    carta1.shuffle()
    carta1.shuffle()
    segundo = str(carta1.deck[expected])
    assert  segundo != inicial



# pruebas para la clase Deck() Funion deal
@pytest.mark.parametrize(
    "input_nd, expected",
    [
        (0, 52),
        (1,51),
        (52, 0),
        (51, 1),
        (11, 41),
        (37, 15),
    ]

)
def test_deck_dl(input_nd, expected):
    cartadl = Deck()
    for i in range(0,input_nd):
        cartadl.deal()
    assert len(cartadl.deck) == expected

##prueba para la clase Hand() Funcion add_card()
@pytest.mark.parametrize(
    "input_ha, expected",
    [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
    ]

)
def test_hand_add(input_ha, expected):
    cartadl = Deck()
    prime = Hand()
    for i in range(input_ha):
        cartadl.shuffle()
        asignada = cartadl.deal()
        prime.add_card(asignada)

    
    assert (len(prime.cards))  ==  expected


#prueba Clase Hand funcion adjust_for_ace()
@pytest.mark.parametrize(
    "input_adj, expected",
    [
        (1, 11),
        (2, 12),
        (3, 13),
        (4, 14),
        (5, 15),
        (0, 0),

    ]

)
def test_hand_adj(input_adj, expected):
    cartadl = Deck()
    prime = Hand()
    cartas_prueba = []
    for i in range(0,len(cartadl.deck)):
        if (str(cartadl.deck[i])[0]) == 'A':
            cartas_prueba.append(cartadl.deck[i])

    for h in range(input_adj):
        asignada = random.choice(cartas_prueba)
        prime.add_card(asignada)

    prime.adjust_for_ace()
    
    assert prime.value  ==  expected



#Prueba  para la funcion show_some
def test_show_some():
    deck = Deck()
    deck.shuffle()
    
    jugadoruno = Hand()
    jugadoruno.add_card(deck.deal())
    jugadoruno.add_card(deck.deal())
    
    jugadordos = Hand()
    jugadordos.add_card(deck.deal())
    jugadordos.add_card(deck.deal())
    
    assert show_some(jugadoruno,jugadordos) == "Jugando!"


#Prueba  para la funcion show_all
def test_show_all():
    deck = Deck()
    deck.shuffle()
    
    jugadoruno = Hand()
    jugadoruno.add_card(deck.deal())
    jugadoruno.add_card(deck.deal())
    
    jugadordos = Hand()
    jugadordos.add_card(deck.deal())
    jugadordos.add_card(deck.deal())
    
    assert show_all(jugadoruno,jugadordos) == "****"


#Prueba  para la funcion player_busts
def test_player_busts():
    deck = Deck()
    deck.shuffle()
    
    jugadoruno = Hand()
    jugadoruno.add_card(deck.deal())
    jugadoruno.add_card(deck.deal())
    
    jugadordos = Hand()
    jugadordos.add_card(deck.deal())
    jugadordos.add_card(deck.deal())
    
    assert player_busts(jugadoruno,jugadordos) == "Lo siento. Te pasaste. Perdiste.\n"




#Prueba  para la funcion player_wins
def test_player_wins():
    deck = Deck()
    deck.shuffle()
    
    jugadoruno = Hand()
    jugadoruno.add_card(deck.deal())
    jugadoruno.add_card(deck.deal())
    
    jugadordos = Hand()
    jugadordos.add_card(deck.deal())
    jugadordos.add_card(deck.deal())
    
    assert player_wins(jugadoruno,jugadordos) == "Felicitaciones. Ganaste\n!"

#Prueba  para la funcion dealer_busts
def test_dealer_busts():
    deck = Deck()
    deck.shuffle()
    
    jugadoruno = Hand()
    jugadoruno.add_card(deck.deal())
    jugadoruno.add_card(deck.deal())
    
    jugadordos = Hand()
    jugadordos.add_card(deck.deal())
    jugadordos.add_card(deck.deal())
    
    assert dealer_busts(jugadoruno,jugadordos) == "El repartidor se paso. Tu ganas!\n"



#Prueba  para la funcion dealer_wins
def test_dealer_wins():
    deck = Deck()
    deck.shuffle()
    
    jugadoruno = Hand()
    jugadoruno.add_card(deck.deal())
    jugadoruno.add_card(deck.deal())
    
    jugadordos = Hand()
    jugadordos.add_card(deck.deal())
    jugadordos.add_card(deck.deal())
    
    assert dealer_wins(jugadoruno,jugadordos) == "Lo siento, perdiste. El repartidor gano!"



# Prueba  para la funcion dealer_wins
def test_push():
    deck = Deck()
    deck.shuffle()
    
    jugadoruno = Hand()
    jugadoruno.add_card(deck.deal())
    jugadoruno.add_card(deck.deal())
    
    jugadordos = Hand()
    jugadordos.add_card(deck.deal())
    jugadordos.add_card(deck.deal())
    
    assert push(jugadoruno,jugadordos) == "Lo siento, empataron. El repartidor gano!"


