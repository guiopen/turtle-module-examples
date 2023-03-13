import turtle
import math

draw = turtle.Turtle()


#centralize house
draw.up()
draw.back(75)
draw.rt(90)
draw.back(50)
draw.lt(90)
draw.down()

#house base 
draw.fillcolor('#F5F5F5')
draw.begin_fill()
for i in range(2):
    draw.fd(150)
    draw.rt(90)
    draw.fd(200)
    draw.rt(90)
draw.end_fill()

#roof
draw.fillcolor('#800000')
draw.begin_fill()
draw.lt(45)
draw.fd(150 * math.cos(math.radians(45)))
draw.rt(90)
draw.fd(150 * math.cos(math.radians(45)))
draw.end_fill()

#door
draw.fillcolor('#A0522D')
draw.up()
draw.rt(45)
draw.fd(200)
draw.rt(90)
draw.fd(50)
draw.down()
draw.begin_fill()
draw.rt(90)
draw.fd(75)
draw.lt(90)
draw.fd(50)
draw.lt(90)
draw.fd(75)
draw.end_fill()

#window
draw.fillcolor('#b3cee5')
draw.up()
draw.rt(180)
draw.fd(120)
draw.rt(90)
draw.fd(30)
draw.down()
draw.begin_fill()
draw.fd(60)
draw.lt(90)
draw.fd(35)
draw.lt(90)
draw.fd(60)
draw.lt(90)
draw.fd(35)
draw.end_fill()
draw.up()
draw.lt(90)
draw.fd(30)
draw.lt(90)
draw.down()
draw.fd(35)
draw.up()
draw.lt(90)
draw.fd(30)
draw.lt(90)
draw.fd(17.5)
draw.lt(90)
draw.down()
draw.fd(60)

turtle.done()
