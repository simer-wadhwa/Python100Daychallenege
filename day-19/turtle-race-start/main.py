from turtle import Turtle, Screen
import random
start_game = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput("choose the winner", "Name of  color of turtle to win:")

# tim = Turtle(shape="turtle")
# tim.penup()
colours = ["pink", "linen", "Red", "Yellow", "Cyan", "Firebrick", "blue"]
y_distance = [-20, -50, -80, 70, 100, 130]

turtle_list = []
for turtle_index in range(6):

    # turtle_list.append(Turtle(shape="turtle"))
    # turtle_list[i].color((colours[i]))
    # turtle_list[i].penup()
    # turtle_list[i].goto(x=-230, y= y_distance[i])
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_distance[turtle_index])
    turtle_list.append(new_turtle)


if user_input:
    start_game = True

while start_game:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            start_game = False
            winner_color = turtle.pencolor()
            if winner_color == user_input:
                print(f"You won! the winning color is {user_input}")
            else:
                print(f"You lost! the winning color is {winner_color}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
