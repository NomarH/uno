import random


def shuffle(shuffle_cards):
    new_cards = random.shuffle(shuffle_cards)
    return new_cards

def deal():
    '''A function that will give each player 7 cards from the deck'''
    for i in range(7):
        card = random.choice(deck)
        player_cards.append(card)
        deck.remove(card)

    for i in range(7):
        card = random.choice(deck)
        computer_cards.append(card)
        deck.remove(card)

deal()

def draw():
    '''A function that will get the top card in the deck'''
    return deck[-1]


def top_card():
    deck.random 
    return top_card

def player_turn():
    '''A function that handles the user's turn'''
    print(player_cards)
    play_card = input("Enter card would you like to play: ")
    print(play_card)
    while play_card == top_card:
        play_card.append(top_card)



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
    



