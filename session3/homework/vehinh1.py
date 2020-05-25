from turtle import *
import random
shape ("turtle")
speed(-1)
pensize(2)
color_list = ['MediumBlue', 'chocolate1', 'DeepPink', 'dark sea green', 'AliceBlue', 'turquoise2']

sides = 5            
for i in range (3, sides + 1):                  #i xác định hình đó là hình số mấy
    color(random.choice(color_list))            #để chọn color ở ngoài loop n thì toàn bộ hình thứ tự i sẽ mang 1 màu
    for n in range(i):
        forward(80)
        left(360/i)

mainloop()  