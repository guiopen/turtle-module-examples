import turtle

draw = turtle.Turtle()

draw.speed(20)
draw.color("orange")

#make a spiral with repeated "squares"
for spiral in range (50,294,2):
    draw.forward(spiral)
    draw.rt(91.5)

turtle.done()