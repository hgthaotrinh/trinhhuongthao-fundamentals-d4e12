from turtle import *
shape ('turtle')
speed(-1)
pensize(1)
color ('maroon4')
number_squares = 20

## BÀI HÌNH NÓN ##
# for i in range(number_squares):
#     for i in range(4):
#         forward (100)
#         left (90)
#     right (360/number_squares)


## BÀI CON ỐC ##
for i in range(number_squares):
    len_side = 150 - 5*i
    for i in range(4):
        forward (len_side)
        left (90)
    right (10)                                  
    

mainloop()