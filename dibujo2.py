from turtle import *
import random
    
colors = ["red","cyan","yellow","gray","orange","blue"]
bgcolor = "black"

speed(100)

for x in range(200):
    aleatorio = random.randrange(0,6)
    pencolor(colors[aleatorio])
    width(x/50+1)#
    forward(x)#???
    left(12)#
hideturtle()
done()