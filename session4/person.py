person = ['Đức', 96, 'Sơn La', 1, False]            #khó biết thông tin đại diện cho gì, vì mỗi phần tử là 1 định dạng khác nhau
dictionary_person = {
    'name': 'Đức',                                  #key : value, không giới hạn số cặp, bất kỳ kiểu dữ liệu, chứa được cả list, chứa được dictionary khác
    'yob': 96, 
    'hometown': 'Sơn La',
}

## READ
if 'yb' in dictionary_person:                       #kiểm tra key có nằm trong dict không --> dùng để check
    print(dictionary_person['yb'])
else:
    print('ngu')

## CREAT + UPDATE
dictionary_person['relationship'] = False           #2 câu lệnh giống nhau vì mỗi key là unique, nếu key đó đã tồn tại rồi thì sẽ tự động update
dictionary_person['name'] = 'not Đức'

## DELETE
del dictionary_person['name']
print(dictionary_person)

## READ
for key in dictionary_person:
    print(key, dictionary_person[key])