## Bài 2 ##

sheep_list = [31, 33, 45, 6, 25, 10]
print('Cừu này dùng để bán', sheep_list)

for i in range(4):
    print('MONTH', i + 1)
    ## Tìm max bằng tay ##
    max_sheep = sheep_list[0]       #gán luôn là số lớn nhất
    for sheep in sheep_list:
        if sheep > max_sheep:       #lần lượt so sánh với các item còn lại
            max_sheep = sheep
    print(max_sheep)

    ## Xẻo lông ##
    max_index = sheep_list.index(max_sheep)
    sheep_list[max_index] = 8
    print(sheep_list)

    ## Cừu béo lên ##
    for index, sheep in enumerate(sheep_list):
        sheep_list[index] = sheep + 50
    print(sheep_list)

total_size = 0
for sheep in sheep_list:
    total_size = total_size + sheep
print(total_size)

total_money = total_size * 2
print("$", total_money)

# for i in range (1, 4):
#     print('MONTH', i)

#     ## Xẻo lông ##
#     max_value = max(sheep_list)
#     max_index = sheep_list.index(max_value)
#     print('Con này size', max_value, 'to nhất, xẻo được rồi')


#     ## Đàn mới ##
#     sheep_list[max_index] = 8
#     print('Xẻo con kia xong đàn mình còn những con size này:', sheep_list)

#     ## Upsize 1 tháng ##
#     for index, value in enumerate(sheep_list):
#         sheep_list[index] = value + 50
#     print('Sau 1 tháng nuôi được ngần này', sheep_list)
#     print('-----')


# print ('Tổng size cừu nhà mình là: ', sum(sheep_list))
# print ('Mình sẽ kiếm được số tiền là: $', sum(sheep_list)*2)