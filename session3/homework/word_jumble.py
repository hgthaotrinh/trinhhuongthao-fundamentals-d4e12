from random import shuffle, choice, randint          #hoặc lệnh randint                
word = 'champion'
list_word = list(word)                      #phân tách riêng rẽ từng phần tử
# another_list_word = word.split(',')         #phân tách phần tử dựa vào ký hiệu được gán
print(list_word)

shuffle(list_word)
# temp = list_word[0]
# list_word[0] = list_word[1]
# list_word[1] = temp
for char in list_word:
    print(char, end=' ')



#nếu dùng lệnh import random, phải ghi là random.shuffle() thì sẽ biết được lệnh đấy lấy từ thư viện nào
#còn dùng lệnh from random import shuffle thì không cần ghi --> không biết lấy từ thư viện nào, và không sử dụng được thư viện khác có cùng câu lệnh | nhưng có lợi ích là chỉ import đúng cái mình cần