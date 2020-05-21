from turtle import *
import random
shape ("turtle")
speed(-1)
pensize(2)
color_list = ['chocolate1', 'DeepPink', 'dark sea green', 'olive', 'turquoise2', 'aquamarine4', 'dark red', 'dark orange' ]


for i in range(5):
    color(random.choice(color_list))
    begin_fill()
    forward(60)
    left(90)
    forward(80)
    left(90)
    forward(60)
    left(90)
    forward(80)
    left(90)
    forward(60)
    end_fill()

mainloop()  