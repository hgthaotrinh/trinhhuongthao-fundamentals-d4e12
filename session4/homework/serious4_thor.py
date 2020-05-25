month = 3
n1 = 1
n2 = 2

while True: 
    if month == 0:
        print ('month', month, ': pair(s) of rabbits', n1)
    elif month == 1: 
        print ('month', month, ': pair(s) of rabbits', n2)
    else:
        for i in range(2, month):
            month = i + 1
            n1 = n2
            n2 = n1 + n2 
            print ('month', month, ':', n2, 'pair(s) of rabbits')


