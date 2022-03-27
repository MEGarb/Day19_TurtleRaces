from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

turt = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for _ in range(6):
    turt.append(Turtle(shape="turtle"))
    turt[_].penup()
    turt[_].speed("normal")
    turt[_].color(colors[_])
    turt[_].goto(x=-230, y=(125 - (50 * _)))


bet = screen.textinput(title="Make your bet", prompt="Which tutle will win the race?  Enter a color:  ").lower()
while bet not in colors:
    bet = screen.textinput(title="Make your bet", prompt="Which tutle will win the race?  Enter a color:  ")

race_is_on = True
winner = 0
while race_is_on:
    for turtle in turt:
        if turtle.xcor() > 230 and winner == 0:
            winner = turtle.pencolor()
            race_is_on = False
        else:
            turtle.forward(random.randint(1, 10))

if bet == winner:
    print(f"Who needs horse racing?  You can bet the turtles!  {winner.capitalize()} won!")
else:
    print(f"Stick to betting the ponies.  {winner.capitalize()} lost.")

screen.exitonclick()
