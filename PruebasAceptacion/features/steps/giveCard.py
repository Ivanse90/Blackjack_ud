from behave import *
from BlackJack import Started


@given('the sum of the players cards is less or more {value}')
def step_imp(context,value):
    context.BlackJack= Started()
    context.BlackJack.historytwo('p',value)
    #context.values= values.split(',')
    #context.BlackJack= Sum()
    #context.values= values.split(',')

@when('the player requested the last card')
def step_imp(context):
    context.visible=context.BlackJack.start(2,2,True)
    context.hand_player=context.BlackJack.hand_player
    context.hand_dealer=context.BlackJack.hand_dealer
    #print('Valor de hiddenCard=',context.visible)
    #context.deck='None'
    #context.deck=context.BlackJack.getDeckHidden()
    #context.total=context.BlackJack.sumar(2,2,False)
    #context.total=4

@then('the player {statusplayer}')
def step_imp(context,statusplayer):
    #print('deck=',context.card)

    #deck=context.card
    #assert(deck==context.card)
    #deck='None'
    print('context.hand_player=',context.hand_player)
    if (int(context.hand_player)<21):
        assert(statusplayer=='next step')
    else:
        if (int(context.hand_player)==21):
            assert(statusplayer=='win')
        else:
            assert(statusplayer=='lose')    
#step_imp(context)
