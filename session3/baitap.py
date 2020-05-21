city = ['Tokyo', 'Denver', 'Berlin', 'Toronto']
# command = ['C', 'R', 'U', 'D']
# meaning = ['create', 'read', 'update', 'delete']



# running = True
# while running:
#     action = input("Enter the action you want to do: ")
#     if action == "C":
#         request = input("Enter destination you'd like to add: ")
#         city.append(request)
#     elif action == "U": 
#         old_value = input("Name of city you'd like to change: ")
#         value = input("Name of the new destination: ")
#         index = city.index(old_value)
#         city[index] = value
#     elif action == "D":
#         delete_value = input("Name of city you'd like to delete: ")
#         index = city.index(delete_value)
#         city.pop(index)
#     elif action == "R":
#         for index, value in enumerate(city):
#             print (index + 1, value)
#     else:
#         print("Select another command please")
#         running = False


# if action != 'R':
#     for index, value in enumerate(city):
#         print (index + 1, value)
# else:
#     print()


#CREATE
# request = input("Enter destination you'd like to add: ")
# city.append("New York")

#UPDATE
# old_value = input("Name of city you'd like to change: ")
# value = input("Name of the new destination: ")
# index = city.index(old_value)
# city[index] = value

#DELETE
# delete_value = input("Name of city you'd like to delete: ")
# index = city.index(delete_value)
# city.pop(index)

#READ
# for index, value in enumerate(city):
#     print (index + 1, value)




### CHỮA BÀI ###
stores = ['cá sấu', 'khủng long', 'phi thuyền']         #cho ra ngoài để không bị đè các kết quả Create ở dưới

while True:

    choices = input('what do you want to do (c r u d) ')
    
    if choices == 'c':
        new_item = input('what u want to add: ')
        stores.append(new_item)
        print(*stores)
    elif choices == 'r':
        print(*stores)
    elif choices == 'd':
        for index, value in enumerate(stores):
            print(index + 1, value)
        delete_index = int(input('enter position you want to delete: '))
        stores.pop(delete_index - 1)
        print(*stores)
    elif choices == 'u':
        for index, value in enumerate(stores):
            print(index + 1, value)
        update_index = int(input('enter position you want to make change: '))
        update_value = input('enter new value: ')
        stores[update_index - 1] = update_value
        print(*stores)
    else:
        break