from turtle import Turtle, Screen
import random

is_game_on = False
colors = ["red", "blue", "orange", "violet", "green", "cyan"]
y_position = [-150, -100, -50, 00, 50, 100]

screen = Screen()
screen.setup(width= 550, height= 450)
users_choice = screen.textinput(title= "Choose your bet", prompt= "Who will win the race? Enter the color : ")

all_turtles = []
for turtle in range(0, 6):
    new_turtle = Turtle(shape= "turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x= -250, y= y_position[turtle])
    all_turtles.append(new_turtle)

if users_choice in colors:
    is_game_on = True

while is_game_on:

    for turtle in all_turtles:
        if turtle.xcor() > 255:
            is_game_on = False
            winning_color = turtle.pencolor()
            if users_choice == winning_color:
                print("You have own the game")
            else:
                print(f"Sorry you lose the game! The winner is {winning_color}")
            break

        turtle.forward(random.randint(0, 10))

screen.exitonclick()