## Bài 2 ##

sheep_list = [31, 33, 45, 6, 8, 10]
print('Cừu này dùng để bán', sheep_list)
month = 4
value = sheep_list
index = sheep_list.index()

for month in range(4):

    print('MONTH', month+1)

    ## Xẻo lông ##
    max_value = max(sheep_list)
    max_index = sheep_list.index(max_value)
    print('Con này size',max_value, 'to nhất, xẻo được rồi')

    ## Đàn mới ##
    sheep_list[max_index] = 8
    print('Xẻo con kia xong đàn mình còn những con size này:', sheep_list)

    ## Upsize 1 tháng ##
    sheep_list[int(index)] = value + 50
    print('Sau 1 tháng nuôi được ngần này', sheep_list)