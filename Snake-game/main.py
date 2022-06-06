from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score_Board
import time

screen = Screen()
screen.setup(width= 800, height= 500)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score_board = Score_Board()

screen.onkey(key= "Up", fun= snake.up)
screen.onkey(key= "Down", fun= snake.down)
screen.onkey(key= "Left", fun= snake.left)
screen.onkey(key= "Right", fun= snake.right)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.increase_length()
        score_board.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        is_game_on = False
        score_board.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.game_over()
            is_game_on = False











screen.exitonclick()