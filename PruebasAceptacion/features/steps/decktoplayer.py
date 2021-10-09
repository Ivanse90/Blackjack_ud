from behave import *
from BlackJack import Started


@given('the player wants to begin a game, the dealer and the player will take {values} cards')
def step_imp(context,values):
    context.BlackJack= Started()
    context.values= values.split(',')
    #context.BlackJack= Sum()
    #context.values= values.split(',')

@when('the dealer gets two cards')
def step_imp(context):
    context.visible=context.BlackJack.start(int(context.values[0]),int(context.values[1]),False)
    #context.visible=context.BlackJack.visible
    #print('Valor de hiddenCard=',context.visible)
    #context.deck='None'
    #context.deck=context.BlackJack.getDeckHidden()
    #context.total=context.BlackJack.sumar(2,2,False)
    #context.total=4

@then('a of these deck should {visible} to the player')
def step_imp(context,visible):
    #print('deck=',context.card)

    #deck=context.card
    #assert(deck==context.card)
    #deck='None'
    #print('Valor de hiddenCard=',context.visible)
    assert(visible==context.visible)
#step_imp(context)
