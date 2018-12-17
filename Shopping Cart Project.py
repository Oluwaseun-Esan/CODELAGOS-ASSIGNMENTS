Cart = {}

print('SHOPPING CART PROGRAM')

print ("""
Shopping Cart Options: The cart will have the following options:
................................................................
1 : Add items
2 : Remove items
3 : View the Cart
0 : Exit the program """)
print ('')

option = int(input('Select an option: '))

while option !=0:
    if option == 1:
        item = input('Enter an item: ')
        if item in Cart:
            print('Item already in Cart')
            quantity = int(input('Enter a quantity: '))
            Cart[item] = Cart[item]+quantity    # Cart[item] += quantity  : To add more items to the cart
        else:
            quantity = int(input('Enter a quantity: '))
            Cart[item] = quantity
            
    elif option == 2:
        item = input('Enter an item: ')
        if item in Cart:
            print('Item still available in the Cart')
            quantity = int(input('Enter a quantity to remove: '))
            Cart[item] = Cart[item]-quantity
        else:
            Cart[item] = 0

    elif option == 3:
        for item in Cart:
            print (item, ':' , Cart[item])
            
    elif option !=0:
        print ('You didn\'t enter a valid option.\n\nPlease Enter a valid option.')

    option = int(input('\n\nEnter an option: '))

else:
    print ('Shopping Cart Is Closed')
