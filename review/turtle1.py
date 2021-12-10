import turtle
from random import *
from turtle import *
penup()
goto(-140,140)
for sp in range(15):
	speed(10)
	write(sp)
	right(90)
	forward(10)
	pendown()
	forward(150)
	penup()
	backward(160)
	left(90)
	forward(20)

richa = Turtle()
richa.color('red')
richa.shape('turtle')
richa.penup()
richa.goto(-160,100)
richa.pendown()


luci = Turtle()
luci.color('blue')
luci.shape('turtle')
luci.penup()
luci.goto(-160,80)
luci.pendown()


turtleVar = Turtle()
turtleVar.color('green')
turtleVar.shape('turtle')
turtleVar.penup()
turtleVar.goto(-160,60)
turtleVar.pendown()


ms = Turtle()
ms.color('yellow')
ms.shape('turtle')
ms.penup()
ms.goto(-160,40)
ms.pendown()

for turn in range(100):
	richa.forward(randint(1,5))
	luci.forward(randint(1,5))
	turtleVar.forward(randint(1,5))
	ms.forward(randint(1,5))
turtle.done()