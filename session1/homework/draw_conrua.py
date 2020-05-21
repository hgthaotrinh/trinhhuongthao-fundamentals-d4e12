from turtle import *
shape("turtle")
speed(-1)
pensize(3)
color("DarkOliveGreen")
fillcolor("DarkOliveGreen1")

begin_fill()                #để begin_fill() ra ngoài loop
for i in range (4):    
    forward(80)
    left(90)
end_fill()

forward(100)                 #chuyển sang hình tam giác

begin_fill()
for n in range (3):
    forward(80)
    left(120)
end_fill()

mainloop()