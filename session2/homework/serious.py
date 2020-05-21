##BÀI 1 -- BMI
# height = int(input('Điền chiều cao của bạn (cm): '))
# weight = int(input('Điền cân nặng của bạn (kg): '))
# bmi = round(weight / ((height/100)**2),1)

# if bmi < 16:
#     print("BMI của bạn là", bmi, "và bạn trông như đầu lâu xương vắt chéo")
# elif bmi < 18.5:
#     print("BMI của bạn là", bmi, "và trông cũng mình hạc sương mai ra phết đấy")
# elif bmi < 30:
#     print("BMI của bạn là", bmi, "vừa vặn mỡ màng hơi bị được đấy")
# else:
#     print("BMI của bạn là", bmi, "béo phì cmnr ăn ít thôi")

##BÀI 2 -- Giai thừa
end_number = int(input('Điền số giai thừa bạn muốn vào đây: '))
factorial = 1
if end_number < 2:
    print(1)
else:
    for i in range(2, end_number+1):
        factorial *= i                  #dấu *= là i nhân với i tiếp theo
    print(factorial)


## BÀI 3 - a - i: in 20 số từ 0
# for i in range (21):
#     print(i, end = " ")

## BÀI 3 - a - ii:
# n = int(input("thử nghĩ 1 số thật to vào đây: "))
# for i in range (n+1):
#     print(i, end = " ")

## bài 3b i
# for i in range(20):
#     if i % 2 == 0:
#         print(1, end = " ")       # \n là tự động của lệnh print là xuống dòng. Ở đây để str = dấu cách để ký hiệu kết thúc lệnh print là dấu cách
#     else:
#         print(0, end = " ")      #2 lệnh print tự động tách ra thành 2 dòng khác nhau

## bài c i 
# xx = 11
# yy = 10
# for y in range (1, yy + 1):
#     for x in range(1, xx+1):
#         if x*y >= 10:
#             print(x*y, end = " ")
#         else:
#             print(x*y, end = "  ")
#     print()                             #do lệnh mặc định của print() là \n xuống dòng
    
## bài d i
# for y in range (1, 10):
#     for x in range(1, 10):
#         if x 