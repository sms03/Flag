import turtle
import time
turtle.title("India")
t = turtle.Turtle()

t.penup()
t.goto(-250, 150)
t.pendown()
t.begin_fill()
t.fillcolor('#FBB917')
t.forward(475)
t.left(-90)
t.forward(80)
t.left(-90)
t.forward(475)
t.left(-90)
t.forward(80)
t.end_fill()

t.penup()
t.goto(-250, 70)
t.pendown()
t.begin_fill()
t.fillcolor('white')
t.left(-180)
t.forward(80)
t.left(90)
t.forward(475)
t.left(90)
t.forward(80)
t.end_fill()

t.penup()
t.goto(-250, -10)
t.pendown()
t.begin_fill()
t.fillcolor('green')
t.left(-180)
t.forward(80)
t.left(90)
t.forward(475)
t.left(90)
t.forward(80)
t.end_fill()


t.color("Indigo")
t.penup()
t.goto(20, 30)
t.pendown()
t.pensize(2)
t.circle(35)



for i in range(24):
   t.penup()
   t.goto(-17, 32)
   t.setheading(15*i)
   t.pendown()
   t.forward(32)


t.hideturtle()

t = turtle.Turtle()
colors = ["purple","pink", "maroon", "magenta", "light slate blue",  "violet", "dark salmon"]

for color in colors:
    t.screen.bgcolor(color)
    time.sleep(1)


turtle.exitonclick()