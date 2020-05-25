numbers = [1, 2, 1, 1, 4, 5, 6, 3, 4, 3]

## Use count function
# number_input = int(input('Write your number: '))
# number_count = numbers.count(number_input)
# print('Your number', number_input, 'appears', number_count, 'time(s)')


## No use of count function
number_input = int(input('Write your number: '))
number_count = 0
for i in numbers:
    if number_input == numbers[i]:
        count = 1
    else:
        count = 0
    number_count += count
print('Your number', number_input, 'appears', number_count, 'time(s)')

