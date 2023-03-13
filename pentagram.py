import turtle
draw = turtle.Turtle()

draw.speed(10)
draw.color("orange")

#draw the pentagram, angles different from 144 will generate different results
for spiral in range (5):
    draw.forward(200)
    draw.rt(144)

turtle.done()