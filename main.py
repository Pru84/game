
from turtle import Screen
from Snake import Snake
from Food import Food
from Score import Score 
import time


screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food)<15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280 :
        score.resetscore()
        snake.reset()

screen.exitonclick()