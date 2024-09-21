import random


def shuffle(shuffle_cards):
    new_cards = random.shuffle(shuffle_cards)
    return new_cards

def deal():
    '''A function that will give each player 7 cards from the deck'''
    # 1. get 7 cards from deck and give it to player, get 7 cards from deck and give it to computer.
    # 2. place one card in discard pile.
    # 3. show player their cards and the top card (in the discard pile)
    return

def draw():
    '''A function that will get the top card in the deck'''
    # get top card from draw pile.
    return

def users_turn():
    '''A function that handles the user's turn'''
    # 1. show user list of options:
    #  - a. play, b. draw
    # if play, check if allowed play. 
    # if draw, give them top card in draw pile.


def computer_turn():
    '''A function that handles the computer's turn'''
    # 1. make computer look for the top discard card in their cards.
    # 2. if found, play it.
    # 3. if not found, draw from deck.
    return

def check_for_winner():
    '''A function that checks if anyone has won the game'''
    #  whoever has zero cards first is the winner.

def check_draw_pile():
    '''A function that chacks that the draw pile still has cards, if no mor cards, replenishes it'''
    # 1. check if draw pile still has cards.
    # 2. if no more cards, take all the cards, except teh top card, from the discard pile and put it in the draw pile.
    # 3. shuffle the draw pile.




# Game Logic goes here
deck = (0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9)
draw_pile = []
discard_pile = []
player_cards = []
computer_cards = []
game_over = False

# 1. Shuffle the deck.
# 2. deal the cards.
# 3. while no winner
    #  - player's turn
    #  - check for winner 
    #  - check draw pile
    #  - computer's turn 
    #  - check for winner
    #  - check draw pile
    



