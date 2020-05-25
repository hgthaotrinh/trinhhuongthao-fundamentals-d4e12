prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stocks = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for key in prices: 
    price = prices[key]
    stock = stocks[key]
    print(key)
    print('price:', price) 
    print('stock:', stock)
    print()

total = 0
for key in prices: 
    total += prices[key] * stocks[key]
print('total revenue: $', total)


#check:
banana = 4 * 6
apple = 2 * 0 
orange = 1.5 * 32
pear = 3 * 15
revenue = banana + apple + orange + pear
print('total check', revenue)