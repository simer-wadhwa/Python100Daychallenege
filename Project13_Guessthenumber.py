import random
from extra_files import art

EASY_LEVEL = 10
HARD_LEVEL = 5


def choose_difficulty():
    # choose = True
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard'")
        if level.lower() == "easy":
            return EASY_LEVEL
        elif level.lower() == "hard":
            return HARD_LEVEL
        else:
            print("You didn't choose correct option. Choose Again")


def play_game(level, number):
    while level:
        print(f"You have {level} attempts remaining to guess the number.")
        guess = int(input("Make a guess"))
        if guess < number:
            print("To low")
            print("Guess Again")
        elif guess > number:
            print("To High")
            print("Guess Again")
        else:
            print(f"You got it! The answer was {number}")
            break
        level = level - 1
    if level == 0:
        print("You lose 😤")
    else:
        print("You win 😃")


def game():
    print(art.guess_logo)
    print("Welcome to the number Guessing Game !")
    print("I am thinking of a number between 1 to 100 ")
    number = random.randint(1, 100)

    turns = choose_difficulty()
    # level = input("Choose a difficulty. Type 'easy' or 'hard'")
    # if level.lower() == "easy":
    #     play_game(EASY_LEVEL,number)
    # elif level.lower() == "hard":
    #     play_game(HARD_LEVEL,number)
    # else:
    #     print("You didn't choose correct option")
    play_game(turns, number)


if __name__ == "__main__":
    game()
