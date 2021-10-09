Feature: History 2

Scenario Outline: As a dealer I want to define who won the game
Given the sum of the players cards is less or more <value>
When the player requested the last card
Then the player <statusplayer>
   Examples: values
    |   value    |   statusplayer        |
    |   22       |      lose             |
    |   23       |      lose             |
    |   19       |      next step        |
    |   21       |      win              |
