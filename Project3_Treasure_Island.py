print("Welcome to Treasure Iasland. Your mission is to find the treasure :) ")

dir = input("Where  as you want to go Left or Right?....Wow choose Carefully it goona decide end or Start!!!!!!")

if dir.lower() == "right":
    print("Ooops you lost game over!!!!!!!!!!!")

elif dir.lower() == "left" :
    step = input("Now what you wannna do Swim or Wait???????")
    if step.lower() == "wait":
        door = input("Hmmm to close to the gold, which color door leads to the Gold, Red , Blue or Yellow!!!! Choose Carefully")
        if door.lower() == "red":
            print("You got burned by Fire...Game Over")
        elif door.lower() == "blue":
            print ("You got eaten by the booo!!! GAme Over")
        elif door.lower() == "Yellow":
            print("You got the bag full of coins, Congratulations you win the game")
        else :
            print("you did not choose Y,R and B So you lose the game!!!!!!!!Game Over")
    else:
        print("Attacked by trouts GAme Over")
else:
    print("GAme over You need to choose left or right")