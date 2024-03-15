import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_cars()
    car_manager.move()
    
    if player.ycor() > 280:
        scoreboard.level_up()
        car_manager.faster()
        player.reset_position()

    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            scoreboard.game_over()
            game_is_on = False
    
    
    

screen.exitonclick()
