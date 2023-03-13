import turtle

draw = turtle.Turtle()

#draw start position
draw.speed(100)
draw.up()
draw.goto(-150,0)
draw.lt(90)
draw.down()

#draw left eye
draw.lt(210)
draw.fillcolor('purple')
draw.begin_fill()
draw.circle(20)
draw.end_fill()

for eye1 in range (20,60,10):
    draw.circle(eye1)

draw.up()
draw.rt(210)
draw.rt(90)
draw.forward(250)
draw.down()

#draw right eye
draw.lt(60)
draw.fillcolor('purple')
draw.begin_fill()
draw.circle(20)
draw.end_fill()

for eye2 in range (20,60,10):
    draw.circle(eye2)

#draw mouth
draw.up()
draw.rt(60)
draw.goto(-95,-100)
draw.down()

draw.fillcolor('red')
draw.rt(45)
draw.width(10)
draw.color('red')
draw.begin_fill()
draw.circle(100,90)
draw.lt(135)
draw.fd(140)
draw.end_fill()

#draw teeth
draw.color('white')
draw.fillcolor('white')

draw.lt(120)
draw.width(1)
draw.begin_fill()
for tot in range(9):
    draw.fd(15)
    draw.lt(120)
    draw.fd(15)
    draw.rt(120)
draw.lt(60)
draw.back(130)
draw.end_fill()

#draw nose
draw.color('black')
draw.up()
draw.goto(-23,-40)
draw.dot(50, 'red')
draw.down()

#draw head
draw.up()
draw.goto(-23,-190)
draw.down()
draw.circle(200)

#draw left hair
draw.up()
draw.goto(-210,70)

for hair1 in range(10):
    draw.dot(50,'orange')
    draw.fd(8)
    draw.lt(90)
    draw.fd(10)
    draw.rt(90)

#draw right hair
draw.goto(170,70)

draw.lt(180)
for hair1 in range(10):
    draw.dot(50,'orange')
    draw.fd(8)
    draw.rt(90)
    draw.fd(10)
    draw.lt(90)

#draw hat
draw.goto(-80,200)
draw.down()


draw.begin_fill()
draw.rt(120)
draw.forward(110)

draw.width(2)
draw.color('blue')
for sparky in range (18):
    draw.fd(20)
    draw.back(20)
    draw.rt(20)

draw.width(1)
draw.color('black')
draw.fillcolor('pink')
draw.rt(120)
draw.forward(110)
draw.end_fill()

turtle.done()