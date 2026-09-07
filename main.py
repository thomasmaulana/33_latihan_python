import turtle
import math

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("white")

screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.color("#dd2c2c")

for scale in range(11, 17):
    for i in range(170):
        angel = i * (math.pi * 2) / 170
        x = scale * math.sin(angel) * math.cos(angel) * 10
        y = scale * (math.sin(angel) ** 2) * 10
        t.goto(x, y)
t.penup()
t.goto(0, -50)
t.color("#e6186d")

t.write("happy birthday", align="center", font=("arial", 16, "bold"))

screen.update()

screen.mainloop()
