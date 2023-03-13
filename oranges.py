import turtle

draw = turtle.Turtle()

#oranges start position
draw.up()
draw.speed(50)
draw.back(430)

#make a lot of oranges that dont touch each other
for bola in range (40,140,10):
    draw.dot(bola,'orange')
    draw.forward(5 + bola)
    draw.left(90)
    draw.forward(5)
    draw.rt(90)

#show that oranges are aligned
draw.color('black')
draw.goto(-450,-20)
draw.down()
draw.width(3)
draw.fd(900)
  


turtle.done()
