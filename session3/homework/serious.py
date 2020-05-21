## Bài 2 ##

sheep_list = [31, 33, 45, 6, 8, 10]
print('Cừu này dùng để bán', sheep_list)
value = sheep_list

for i in range (1, 4):
    print('Month', i)

    ## Xẻo lông ##
    max_value = max(sheep_list)
    max_index = sheep_list.index(max_value)
    print('Con này size', max_value, 'to nhất, xẻo được rồi')

    ## Đàn mới ##
    sheep_list[max_index] = 8
    print('Xẻo con kia xong đàn mình còn những con size này:', sheep_list)

    ## Upsize 1 tháng ##
    for index, value in enumerate(sheep_list):
        sheep_list[index] = value + 50
    print('Sau 1 tháng nuôi được ngần này', sheep_list)
    print('-----')


print ('Tổng size cừu nhà mình là: ', sum(sheep_list))
print ('Mình sẽ kiếm được số tiền là: $', sum(sheep_list)*2)