from turtle import *
shape('turtle')
speed(-1)

for i in range(100):      #(1)lặp lại bao nhiêu lần? (2)những đoạn code nào cần phải lặp lại? vd mainloop không cần lặp lại (3)sau dấu : sẽ tự động thụt vào trong lề
    for i in range (7):
        forward(20)
        right(60)
        forward(50)
        left(10)
    right(7) #hình vuông thứ 2
    


mainloop()