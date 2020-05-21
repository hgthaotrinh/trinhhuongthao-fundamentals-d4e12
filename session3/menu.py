mon_an = ['bụng cá hồi', 'hàu Nhật Bản', 'mắm tôm', 'tôm hùm nướng phô mai bơ tỏi', "da vịt quay giòn cuốn bánh đa Quảng Đông", "bún đậu mắm tôm"]
# for i in range (len(mon_an)):
#     print(mon_an[i])                #READ

# name = "tóp mỡ"             #có thể để user input
# mon_an.append(name)         #CREATE
# mon_an[2] = 'mỳ vịt tiềm'   #UPDATE
# print(mon_an)             #print duy nhất 1 biến nên là hàng ngang

# for value in mon_an:
#     print(value)            #từng lệnh print một nên xuống dòng được

#_____________________________
### BÀI TẬP 1 (chọn 1 món trong menu và sửa)

# for i in range (len(mon_an)):             #cách 1 lấy số thứ tự

    # print(i+1, ".", mon_an[i])      

# for index, value in enumerate(mon_an):      #cách 2 lấy số thứ tự
#     print(index + 1, value)

# index = int(input("Thứ tự món ăn muốn sửa: ")) - 1      #phải trừ đi 1, vì index vẫn bắt đầu bằng 0
# value = input("Tên mới của món ăn: ")
# mon_an[index] = value
# for index, value in enumerate(mon_an):
#     print(index + 1, value)

#khi nào hiện ra trước mắt người dùng thì +1, khi người ta input vào thì phải -1, đảm bảo index bắt đầu bằng 0



#_______________________________________
###LẤY INDEX TỪ TÊN VALUE
# old_value = input("Món muốn thay: ")
# value = input("Đổi tên thành: ")
# index = mon_an.index(old_value)
# mon_an[index] = value
# for index, value in enumerate(mon_an):
#     print(index + 1, value)


#_______________________________________
mon_an = ['bụng cá hồi', 'hàu Nhật Bản', 'mắm tôm', 'tôm hùm nướng phô mai bơ tỏi', "da vịt quay giòn cuốn bánh đa Quảng Đông", "bún đậu mắm tôm"]
deleted_item = mon_an.pop()
print(deleted_item)