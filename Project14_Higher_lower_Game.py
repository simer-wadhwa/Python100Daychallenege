import random
from typing import List

from extra_files import art,game_data


def generate_data(player_list):
    while len(player_list) < 2:
        player_data = random.choice(game_data.data)
        if player_data not in player_list:
            player_list.append(player_data)



def play():
    print(art.high_lower_logo)
    """creating the list of player data for comparison"""
    player_list = []
    generate_data(player_list)
    """play till the game is not over"""
    is_game_over = False
    game_score = 0
    while not is_game_over:

        print(f"Compare A: {player_list[0]['name']}, a {player_list[0]['description']}, from {player_list[0]['country']}")
        print(art.vs)
        print(f"Against B: {player_list[1]['name']}, a {player_list[1]['description']}, from {player_list[1]['country']}")
        choice = input(f"Who has more followers? Type 'A' or 'B':")
        """Compare Score"""
        if player_list[0]['follower_count'] > player_list[1]['follower_count']:
            player = 'A'
        else:
            player = 'B'
        #print(f"player A:{player_list[0]['follower_count']} and player B {player_list[1]['follower_count']}")
        if choice == player:
            game_score = game_score+1
            print(f"You are right!!.Your current score is {game_score}")
            del player_list[0]
            generate_data(player_list)
        else:
            is_game_over = True
            print(f"Sorry that's wrong. Your final score is {game_score}")





if __name__=="__main__":
    play()