# y = a*x**2 + b*x + c = 0
import turtle

turtle.shape("turtle")
turtle.pu()
turtle.right(90)
turtle.forward(300)
turtle.left(90)
turtle.speed(10)
turtle.pd()

x = 6
s = 2.0
k = 0.0005
i = 0

for i in range(x * 360):
    turtle.left(1)
    turtle.forward(s)
    s-=k

##print("hello")
##input()
