# Blackjack
import random
import os
from art import logo

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def deal_card():
    """Returns random card from the list """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    # blackjack check
    if len(cards) == 2 and sum(cards) == 21:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(player_score, computer_score):
    if (player_score == computer_score):
        return "It's a DRAW!"
    elif computer_score == 0:
        return "Computer has BlackJack, you lose!"
    elif player_score == 0:
        return "You have BlackJack, you win!"
    elif player_score > 21:
        return "Player went over 21. Computer wins!"
    elif computer_score > 21:
        return "Computer went over 21. Player wins!"
    elif player_score > computer_score:
        return "Player has the highest score. Player wins!"
    else:
        return "Computer has the highest score. Computer wins!"

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_game():
    player_cards = []
    player_score = 0

    computer_cards = []
    computer_score = 0

    game_over = False

    print(logo)

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Player cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            deal_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if deal_another_card == "y":
                player_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Player's final hand: {player_cards}, final score: {calculate_score(player_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
    print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? 'y' or 'n'? ").lower() == "y":
    clear_console()
    start_game()