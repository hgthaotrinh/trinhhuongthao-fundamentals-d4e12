dictionary_code = {
    'cea': 'chào em, anh đứng đây từ chiều',
    'mm': 'mãi mãi bên nhau bạn nhé', 
    'odc': 'ở đây chúng tôi không làm như vậy',
    'ck': 'cà khịa',
    'kfc': 'tao sẽ đèo cả nhà mày ra KFC'
}

code_input = str(input('Điền từ bạn muốn tra vào đây: '))
if code_input in dictionary_code:
    print('nghĩa:', dictionary_code[code_input])
    print('******************')
    for key in dictionary_code:
        print(key, end='      ')
else:
    decision = str(input('Bạn có muốn đóng góp không? (y/n) '))
    if decision in ['y', 'Y']:
        new_meaning = str(input("Nghĩa của từ bạn vừa điền vào là gì: "))
        dictionary_code[code_input] = str(new_meaning)
        print('******************')
        for key in dictionary_code:
            print(key, end='      ')
    else:
        print('Bai bạn nhé!')

print()