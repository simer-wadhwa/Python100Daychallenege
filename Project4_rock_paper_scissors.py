'''
I learn to write list which removes the extra else if code
Secondly I learn to write condition(to apply logoic instrean of writting only else if statement
(Thinks in term of logic instead of only if else statement)
Thirdly write the print statement of list in one if else statement not  to write an extra code

Major Learning reckeck code  and see how you can reduce the number of lines to write the code
'''
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image=[rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors."))
print(f"user chose {user_choice}")

if user_choice < 0  or user_choice >= 3:
    print("Game Ends As you chose invalid number ")
else:
    print(game_image[user_choice])
    computer_choice = random.randint(0, 2)
    print(f"computer chose: {computer_choice}")
    print(game_image[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("Hurray!!!!!! you Win ")

    elif user_choice == 2 and computer_choice == 0:
        print(" You Lose ")

    elif computer_choice > user_choice:
        print("You Lose ")

    elif computer_choice == user_choice:
        print("Draw ")
    else:
        print("You Win")












