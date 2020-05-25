inventory = {
'gold' : 500,
'pouch' : ['flint' , 'twine' , 'gemstone' ] ,
'backpack' : ['xylophone' , 'dagger' , 'bedroll' , 'bread loaf' ]
}

## Add a key to inventory called 'pocket' .
inventory['pocket'] = ['seashell' , 'strangeberry' ,'lint']

## Delete 'dagger'
backpack = inventory['backpack']
delete_backpack = backpack.pop(1)

## Add 50
gold = [inventory['gold']]
gold.append(50)


print(inventory)