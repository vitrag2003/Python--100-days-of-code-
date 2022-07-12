import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Turtle,Screen

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")

game_is_on=True 
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.snake_move()

    #Detect collision with food    
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.reset_scoreboard()
        snake.reset_game()

    #Detect collision with own tail ~ if head collides with any other segment of the snake then game over 
    for segment in snake.segments[1:]:  #[1:] is slicing concep~ the entire snake's segment is going to get iterated from the second index and not the 0th index 
        # if segment==snake.head: #in the start the head will collide with other segments so thats why this if statement is there
        #     pass
        if snake.head.distance(segment)<10:
            scoreboard.reset_scoreboard()
            snake.reset_game()

screen.exitonclick() 