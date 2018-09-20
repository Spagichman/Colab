import turtle
import math
turtle.shape("turtle")
turtle.speed(0)

d =300

turtle.color("black", "yellow")
turtle.begin_fill()
turtle.circle(d/2)
turtle.end_fill()

turtle.pu()
turtle.left(90)
turtle.forward(d*0.71)
turtle.left(-90)
turtle.forward(d*0.20)
turtle.pd()

turtle.color("black", "blue")
turtle.begin_fill()
turtle.circle(d/12)
turtle.end_fill()

turtle.pu()
turtle.left(180)
turtle.forward(d*0.20*2)
turtle.left(180)
turtle.pd()

turtle.color("black", "blue")
turtle.begin_fill()
turtle.circle(d/12)
turtle.end_fill()

turtle.pu()
turtle.forward(d*0.20)
turtle.left(-90)
turtle.forward(d*0.1)
turtle.pd()

turtle.width(d/5)
turtle.forward(d*0.1)

turtle.pu()
turtle.forward(d*0.20)
turtle.left(-90)
turtle.forward(d*0.22)
turtle.left(90)
turtle.pd()

turtle.width(20)
turtle.pencolor("red")
turtle.circle(d/2*0.45,180)

















