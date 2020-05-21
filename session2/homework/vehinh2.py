from turtle import *
shape ("turtle")
speed(-1)
pensize(2)

sides = 10             
for i in range (3, sides + 1):      #i xác định hình đó là hình số mấy
    for n in range(i):
        if i % 2 == 0:
            color('royal blue')
        else:
            color('MistyRose1')
        forward(80)
        left(360/i)

mainloop()  