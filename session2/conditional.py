#các điều kiện để máy tính tự chạy (vd kiểm tra username password...)

# age = 18
# if age < 18:
#     print('you are not allowed here')
# elif age < 20:
#     print('you wait here')
# else:
#     print('you can drink here')

#Sinh ra 1 số random 0-100 đo độ khó ở để in ra các câu khác nhau
# from random import *
# score = randrange(100)
# print('độ khó ở hôm nay của mẹ là', score)

# if score < 20:
#     print('ngày hôm nay ta có thể xin mẹ khoảng 2 tỷ để mua nhà')
# elif score < 50:
#     print('mình có thể về sau 23h mà chưa bị ăn chửi')
# elif score < 80:
#     print('hôm nay có lẽ mình nên rửa bát và nấu cơm')
# else:
#     print('dù có nín thở thì tối nay vẫn ăn chửi thôi')


# #tìm nghiệm tam thức bậc 2
# from random import randint
# a = randint(1,10)
# b = randint(1,20)
# c = randint(1,10)
# print (a, b, c)
# delta = (b**2) - (4*a*c)
# print('delta =', delta)

# if delta < 0:
#     print('vô nghiệm')
# elif delta == 0:
#     root = -b/(2*a)
#     print('phương trình có 1 nghiệm: ', root)
# else:
#     root1 = (-b + (delta**0.5))/(2*a)
#     root2 = (-b - (delta**0.5))/(2*a)
#     print('phương trình có 2 nghiệm:', root1, root2)


# vòng lặp vô hạn
account_username = 'quyensinh'
account_password = '1tydong'

running = True
while running:
    username = input('username: ')
    password = input('password: ')
    if username == account_username and password == account_password:
            print('Cho mày vào đấy')
            break
            # running = False
            print('aaaa')
            
    else:
        print('chim cút đi')
