import turtle

draw = turtle.Turtle()
draw.width(4)
draw.speed(10)

#clock main body
draw.up()
draw.rt(90)
draw.fd(150)
draw.lt(90)
draw.down()
draw.circle(200)
draw.up()
draw.lt(90)
draw.fd(385)

#clock dots
for doti in range(12):
    draw.dot(10)
    draw.goto(0,50)
    draw.lt(30)
    draw.fd(185)

draw.goto(0,50)
draw.down()

#clock hands
draw.lt(25)
draw.forward(170)
draw.goto(0,50)

draw.rt(233)
draw.width(6)
draw.fd(130)
draw.goto(0,50)

draw.rt(220)
draw.color('red')
draw.width(4)
draw.fd(140)




turtle.done()