import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car=CarManager()
score=Scoreboard()

screen.listen()
screen.onkey(fun=player.go_up,key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car.create_car()
    car.move_cars()

    #Detect collision with car
    for i in car.all_cars:
        if i.distance(player)<20:  #our car is 20px in height by 40px in width
            game_is_on=False
            score.game_over()

    #Detect successful crossing 
    if player.is_at_finish_line():
        player.restart() #The player won the round and the new round starts
        car.level_up()
        score.increase_level()

screen.exitonclick()