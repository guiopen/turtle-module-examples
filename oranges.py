import turtle

draw = turtle.Turtle()

#oranges start position
draw.up()
draw.back(430)

#make a lot of oranges thar dont touch each other
for bola in range (40,140,10):
    draw.dot(bola,'orange')
    draw.forward(10 + bola)
  


turtle.done()