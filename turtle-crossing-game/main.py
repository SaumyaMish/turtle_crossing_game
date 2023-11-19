import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

# creating player
player1 = Player()
screen.listen()
screen.onkey(fun=player1.up, key='Up')
screen.onkey(fun=player1.down,key="Down")

# for scoreboard
scores = Scoreboard()

# for cars
car = CarManager()

count=0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Action on the scrren when Turtle reaches the  levels finish line
    if player1.ycor() > 280 :
        player1.set_pos()
        scores.increase_level()

    # generating random  cars "in the gap of every 6 loop terms"
    car.generate_car()
    car.move_car()

    # game over condition
    for c in car.all_cars:
        if c.distance(player1) < 20:
            scores.game_over()
            game_is_on = False

    #when turtle rached at the finish line
    if player1.is_at_finish_line() :
        car.level_up()

screen.exitonclick()