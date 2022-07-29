import Items
from shopping_history import ShoppingHistory


class ShoppingCart():
    def add_to_class(self, user):
        self.user = user
        items = Items.Items()
        self.lists = []
        self.total = 0
        self.list2 = []
        self.items_history_dict = {
            'User': [self.user], 'Cakes': [0, 1200], 'Cupcakes': [0, 120], 'Brownies': [0, 150], 'Sundaes': [0, 300], 'Cookies': [0, 140],
            'Bread': [0, 110], 'Samosas': [0, 40], 'Rolls': [0, 50], 'Chips': [0, 80], 'Nimco': [0, 130]
        }
        while True:
            choices = input(
                ' \n1 Cakes \n2 Cupcakes \n3 Brownies \n4 Sundaes  \n5 Cookies \n6 Bread \n7 Samosas \n8 Rolls \n9 Chips \n10 Nimco \nEnter the item you want to buy')
            choice_list = choices.split(',')
            for i in range(len(choice_list)):
                if choice_list[i] == '1':
                    n = int(input('How many Cakes do you want to buy?'))
                    if n < 100:
                        items.items_dict['Cakes'][0] - n
                        self.total += n * items.items_dict['Cakes'][1]
                        self.items_history_dict['Cakes'][0] += n
                    else:
                        print(
                            'THE QUANTITY EXCEEDS OUR CURRENT STOCK\nSORRY FOR THE INCONVINENCE')
                elif choice_list[i] == '2':
                    n = int(input('How many Cupcakes do you want to buy?'))
                    if n < 100:
                        items.items_dict['Cupcakes'][0] - n
                        self.total += n * items.items_dict['Cupcakes'][1]
                        self.items_history_dict['Cupcakes'][0] += n
                    else:
                        print(
                            'THE QUANTITY EXCEEDS OUR CURRENT STOCK\nSORRY FOR THE INCONVINENCE')

                elif choice_list[i] == '3':
                    n = int(input('How many brownies do you want to buy?'))
                    if n < 100:
                        items.items_dict['Brownies'][0] - n
                        self.total += n * items.items_dict['Brownies'][1]
                        self.items_history_dict['Brownies'][0] += n
                    else:
                        print(
                            'THE QUANTITY EXCEEDS OUR CURRENT STOCK\nSORRY FOR THE INCONVINENCE')
                elif choice_list[i] == '4':
                    n = int(input('How many Sundae do you want to buy?'))
                    if n < 100:
                        items.items_dict['Sundaes'][0] - n
                        self.total += n * items.items_dict['Sundaes'][1]
                        self.items_history_dict['Sundaes'][0] += n
                    else:
                        print(
                            'THE QUANTITY EXCEEDS OUR CURRENT STOCK\nSORRY FOR THE INCONVINENCE')
                elif choice_list[i] == '5':
                    n = int(input('How many Cookies do you want to buy?'))
                    if n < 100:
                        items.items_dict['Cookies'][0] - n
                        self.total += n * items.items_dict['Cookies'][1]
                        self.items_history_dict['Cookies'][0] += n
                    else:
                        print(
                            'THE QUANTITY EXCEEDS OUR CURRENT STOCK\nSORRY FOR THE INCONVINENCE')
                elif choice_list[i] == '6':
                    n = int(input('How many Bread loaf do you want to buy?'))
                    if n < 100:
                        items.items_dict['Bread'][0] - n
                        self.total += n * items.items_dict['Bread'][1]
                        self.items_history_dict['Bread'][0] += n
                    else:
                        print(
                            'THE QUANTITY EXCEEDS OUR CURRENT STOCK\nSORRY FOR THE INCONVINENCE')
                elif choice_list[i] == '7':
                    n = int(input('How many Samosas do you want to buy?'))
                    if n < 100:
                        items.items_dict['Samosas'][0] - n
                        self.total += n * items.items_dict['Samosas'][1]
                        self.items_history_dict['Samosas'][0] += n
                    else:
                        print(
                            'THE QUANTITY EXCEEDS OUR CURRENT STOCK\nSORRY FOR THE INCONVINENCE')
                elif choice_list[i] == '8':
                    n = int(input('How many Rolls do you want to buy?'))
                    if n < 100:
                        items.items_dict['Rolls'][0] - n
                        self.total += n * items.items_dict['Rolls'][1]
                        self.items_history_dict['Rolls'][0] += n
                    else:
                        print(
                            'THE QUANTITY EXCEEDS OUR CURRENT STOCK\nSORRY FOR THE INCONVINENCE')
                elif choice_list[i] == '9':
                    n = int(input('How many Chips do you want to buy?'))
                    if n < 100:
                        items.items_dict['Chips'][0] - n
                        self.total += n * items.items_dict['Chips'][1]
                        self.items_history_dict['Chips'][0] += n
                    else:
                        print(
                            'THE QUANTITY EXCEEDS OUR CURRENT STOCK\nSORRY FOR THE INCONVINENCE')
                elif choice_list[i] == '10':
                    n = int(input('How many Nimco do you want to buy?'))
                    if n < 100:
                        items.items_dict['Nimco'][0] - n
                        self.total += n * items.items_dict['Nimco'][1]
                        self.items_history_dict['Nimco'][0] += n
                    else:
                        print(
                            'THE QUANTITY EXCEEDS OUR CURRENT STOCK\nSORRY FOR THE INCONVINENCE')
            print('*' * 20 + '\nYOUR TOTAL BILL IS ' + str(self.total))

            check_out = input(
                'Enter Y if you wanna check out else enter N to continue')
            if check_out == 'Y':
                print('You final order is:')
                print(self.items_history_dict)
                s = ShoppingHistory()
                s.update_history(self.items_history_dict)
                break
            else:
                continue

