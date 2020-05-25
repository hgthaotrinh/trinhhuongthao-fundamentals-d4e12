bac_first_number = int(input('Điền số con vi khuẩn đầu tiên: '))
minutes = int(input('Số phút bạn muốn đợi: '))
so_lan = int(minutes//2)
for i in range(so_lan):
    bac_total_number = bac_first_number * (2**(so_lan))
print('Sau',minutes, 'phút bạn sẽ có', bac_total_number, 'con vi khuẩn')