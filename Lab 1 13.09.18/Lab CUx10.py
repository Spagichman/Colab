# y = a*x**2 + b*x + c = 0
import turtle

turtle.shape("turtle")
turtle.speed("fast")
turtle.pu()
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.right(180)
turtle.pd()

y = 10
x = 300
i=0
for i in range(10):
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    x-=y*2
    
    turtle.pu()
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(y)
    turtle.right(90)
    turtle.pd()
    

##print("hello")
##input()
