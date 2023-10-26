'''
Ameture code written by me
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

human = int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors."))
if human == 0:
    print(rock)
elif human == 1:
    print(paper)
elif human == 2:
    print(scissors)


computer = random.randint(0,2)
print(f"computer chose: {computer}")

if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)

if human == 0 and computer == 2:
    print("Hurrayyyyyy! you Win ")

elif human == 2 and computer == 1:
    print("Hurrayyyyyy! you Win ")

elif human == 1 and computer == 0:
    print("Hurrayyyyyy! you Win ")

else:
    print("GAme Ends YOu have invalid number")










