import turtle

draw = turtle.Turtle()
draw.speed(100)
draw.fillcolor('#a91b60')

#flower start point
draw.up()
draw.fd(50)
draw.down()
draw.lt(45)

#flower petals
draw.begin_fill()
for flower in range(12):
    draw.lt(120)
    draw.circle(100, 90)
draw.rt(45)
draw.end_fill()

#flower stem
draw.up()
draw.color('#88ca5e')
draw.back(71)
draw.rt(90)
draw.fd(168)
draw.width(5)
draw.lt(180)
draw.down()
draw.fd(135)



turtle.done()