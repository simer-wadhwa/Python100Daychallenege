import random
from extra_files import art


"""Amature code"""
# def computer_play(cards,computer_cards, computer_score,user_score):
#     if computer_score < 16 and computer_score > user_score:
#         while computer_score < 17:
#
#             computer_cards.append(add_cards(cards,"computer"))
#             print(f"Computer cards : {computer_cards}")
#             computer_score = sum(computer_cards)
#
#
#
#     if computer_score > 21:
#         print(f"computer_score ={computer_score}")
#         return 1
#     else:
#         print(f"user score = {user_score}")
#         if user_score > computer_score:
#             print("You Win")
#             return 1
#         elif user_score < computer_score:
#             print("You Lose")
#             return 0
#         else:
#             print("Draw")
#             return 2

# def compute_score(user_cards,computer_cards):
#     print(f"Computer cards is :{computer_cards}")
#     print(f"User cards is :{user_cards}")
#     user_score = sum(user_cards)
#     computer_score = sum(computer_cards)
#     if user_score == 21:
#         print("User has Blackjack")
#         return 1
#     elif computer_score == 21:
#         print("Computer has Blackjack")
#         return 0
#     else:
#
#         if 11 in user_cards and user_score>21:
#             user_score = user_score - 10
#
#         if user_score > 21 :
#             print("You Lose")
#             return 0
#         elif user_score < 21:
#             play = input("If want to  'Hit' card or 'Stand' !!!")
#             if play.lower() == 'hit':
#                 user_cards.append(add_cards("user"))
#                 compute_score(user_cards,computer_cards)
#             elif play.lower() == 'stand':
#                 answer = computer_play(computer_cards,computer_score,user_score)
#                 print(f"Ans:{answer}")
#                 return answer
#             else:
#                 return -1


def add_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    card_choice = random.choice(cards)
    return card_choice


def compute_score(cards):
    """Take a list of cards return thr score calculated from the cards"""

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(21)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(art.blackjack_logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        # user_cards.append(add_cards(cards))
        user_cards.append((add_cards()))
        # computer_cards.append((add_cards(cards)))
        computer_cards.append((add_cards()))

    while not is_game_over:
        user_score = compute_score(user_cards)
        computer_score = compute_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            play = input(
                "If want to get another card type 'Hit' card or type 'Stand'  to pass!!!"
            )
            if play.lower() == "hit":
                user_cards.append(add_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(add_cards())

        computer_score = sum(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    # answer = compute_score(user_cards,computer_cards)
    # print(f"Answer is:{answer}")

if __name__ == "__main__":
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        play_game()
