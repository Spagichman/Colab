import turtle
import math
turtle.shape("turtle")
turtle.speed(0)

def gard_to_rad(inGRAD):
    return inGRAD*math.pi/180

def len_polygon(rad,auto_n):
    return (2*rad*math.sin(gard_to_rad(180/auto_n)))
    
def angle_polygon(auto_n):
    return 360/auto_n

def print_polygon(rad,auto_n):
    i=0
    turtle.left(-angle_polygon(auto_n)/2)
    for i in range(auto_n):
        turtle.left(angle_polygon(auto_n))
        turtle.forward(len_polygon(rad,auto_n))
    turtle.left(angle_polygon(auto_n)/2)
        
    
r = 15
n = 3
kr = 30
kn = 1

i = 0
for i in range(15):
    turtle.circle(r)
    print_polygon(r,n)
    turtle.up()
    turtle.left(-90)
    turtle.forward(kr)
    turtle.left(90)
    turtle.down()
    r += kr
    n += kn






    
