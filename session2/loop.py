#Vẽ hình vuông mỗi cạnh 1 màu khác nhau
# from turtle import *
# shape ("turtle")
# # speed(-1)
# pensize(4)

# for i in ["gold1", "DeepPink2", "DarkViolet", "MediumSeaGreen"]:
#     color(i)
#     forward(50)
#     left(90)
      
# mainloop()


# Vẽ hình theo số cạnh input vào
# sides = int(input("Hãy nhập một số bất kỳ vào đây: "))
# angle = 180 - ((sides-2)*180)/sides
# from turtle import *
# shape("turtle")

# for i in range(sides):
#     forward(100)
#     left(angle)
    
# mainloop()


#Vẽ hình từ tam giác đến đa giác n cạnh
# sides = int(input("Hãy nhập một số bất kỳ vào đây: "))
# from turtle import *
# shape("turtle")
# color("DarkGoldenrod4")
# speed(-1)

# for i in range (3, sides + 1):
#     for n in range(i):
#         forward(50)
#         left(360/i)

# mainloop()


#Tính tổng các số từ 0-5
total = 0
for i in range(5):
    # total = total + i
    total += i                  #Python hỗ trợ để gán luôn giá trị của total qua các loop

print(total)

#Tính tổng các chữ cái
# total = ''
# for i in ['a', 'b', 'c ']:
#     total += i

# print(total)