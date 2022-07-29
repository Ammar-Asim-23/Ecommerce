from user import Person, User, Admin
from shopping_history import ShoppingHistory
from Items import Items

print('Welcome to Tears of Students Bakery ')
while True:
    choice = input(
        '''What would you like to do:
        1.create new id
        2.login
        3.admin functions
        4.quit
        '''
    )
    if choice == '1':
        print('You have chosen to create new id')
        name = input('Enter your name: ')
        password = input('Enter your password: ')
        email = input('Enter your email address: ')
        address = input('Enter your address: ')
        a = User(name, password, email, address)
        a.generate_id()

    elif choice == '2':
        print('You have chosen login')
        name = input('Enter your username: ')
        password = input('Enter your password: ')
        list = User.get_user_list()
        a = False

        for i in list:
            if name == i[0] and password == i[1]:
                current_user = Person(i[0], i[1], i[2], i[3], i[4])
                a = True

        if a:
            print('Login Succesfull')
            print(f'Welcome {current_user.name}')
            choice_1 = input('''What would you like to do:
             1.Buy items
             2.Check history
             3.Quit
             ''')
            if choice_1 == '1':
                current_user.cart.add_to_class(current_user.name)
            elif choice_1 == '2':
                s = ShoppingHistory()
                s.check_by_name(current_user.name)
            elif choice_1 == '3':
                a = False
                break
            else:
                print('Please enter a correct choice')

        else:
            print('Username or Password is Incorrect')

    elif choice == '3':
        print('You have chosen to login as admin')
        admin = Admin()
        password = input('Please enter the password: ')
        if password == admin.password:
            print('Welcome Back')
            a = True
            while a == True:
                choice_1 = input('''What would you like to do:
                1.Check History
                2.Check User Data
                3.Stock Update
                4.Quit
                ''')
                if choice_1 == '1':
                    s = ShoppingHistory()
                    choice_2 = input('''How would you like to check:
                    1.Check complete history
                    2.Check by name
                    3.Check by order number
                    ''')
                    if choice_2 == '1':
                        s.check_history()
                    elif choice_2 == '2':
                        name = input('Enter the user name whose history you want to check:')
                        s.check_by_name(name)
                    elif choice_2 == '3':
                        order = int(input('Enter the order number'))
                        s.check_by_order(order)
                elif choice_1 == '2':
                    print(User.get_user_list())
                elif choice_1 == '3':
                    a = Items()
                    a.stock_update()

                elif choice_1 == '4':
                    a = False
                    break
                else:
                    print('Please enter a correct choice')
        else:
            print('Sorry Wrong Password')
    elif choice == '4':
        break
