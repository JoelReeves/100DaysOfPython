import art
import random
import os
from game_data import data

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_player(player_name, dictionary):
    name = dictionary["name"]
    description = dictionary["description"]
    country = dictionary["country"]
    player_prefix = "Compare"
    if player_name == "b".lower():
        player_prefix = "Against"
    print(f"{player_prefix} {player_name}: {name}, a {description}, from {country}")
    print(dictionary["follower_count"])

def get_players(a_player, b_player):
    print(art.logo)
    if (final_score > 0):
        print(f"Correct! Current score {final_score}")
    print_player("A".lower(), a_player)

    print(art.vs)
    while a_player == b_player:
        b_player = random.choice(list(data))
    print_player("B".lower(), b_player)

final_score = 0
game_over = False
player_b = random.choice(list(data))

while not game_over:
    if final_score > 0:
        player_a = player_b
    else:
        player_a = random.choice(list(data))
    player_b = random.choice(list(data))
    get_players(player_a, player_b)

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    player_a_count = player_a["follower_count"]
    player_b_count = player_b["follower_count"]

    if guess == "a" and player_a_count > player_b_count:
        final_score = final_score + 1
        clear_console()
    elif guess == "b" and player_b_count > player_a_count:
        final_score = final_score + 1
        clear_console()
    else:
        print(f"Sorry, that's wrong. Final score: {final_score}")
        game_over = True
