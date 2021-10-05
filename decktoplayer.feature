Feature: BlackJack

Scenario Outline: Supply two cards and validate the value of the hidden card
Given the player wants to begin a game, the dealer and the player will take <values> cards
When the dealer gets two cards
Then a of these deck should <visible> to the player

    Examples: values
    |   values |   visible              |  
    |   2,2   |   visible               | 
    |   0,2   |   visible               |      
    |   1,2   |   visible               |           
    |   2,1   |   Not visible           |           
    |   1,0   |   Not visible           |           
    |   0,0   |   Not visible           |                  
