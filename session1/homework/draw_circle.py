#bài vẽ hình tròn
from turtle import *
shape("turtle")
speed(-1)

begin_fill()
r1 = 50
circle(r1)

color("white")
forward(200)

color("dark olive green")
for i in range (20):
    r2 = 80
    circle(r2)
    left(20)

mainloop()