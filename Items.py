
class Items:
    def __init__(self,stock_amount=100):
        with open('stock.txt') as hd:
            raw=hd.read()
            j=raw.split(',')
            s=[]
            for i in j:
                s.append(int(i))
            self.items_dict =  {
            'Cakes':[s[0],1200], 'Cupcakes':[s[1],120], 'Brownies':[s[2],150],'Sundaes':[s[3],300],'Cookies':[s[4],140],
            'Bread':[s[5],110], 'Samosas':[s[6],40], 'Rolls':[s[7],50], 'Chips':[s[8],80], 'Nimco':[s[9],130]
            }

    def stock_update(self):
        item = input('Enter the item do you want to add \n1 Cakes, \n2 Cupcakes, \n3 Brownies, \n4 Sundaes , \n5 Cookies, \n6 Bread \n7 Samosas \n8 Rolls \n9 Chips \n10 Nimco ')
        if item == '1':
            n = int(input('How many Cakes do you want to add?'))
            if n<=100:
                self.items_dict['Cakes'][0]+=n
                print(self.items_dict)
            else:
                print('This exceeds our stores limit.')

        elif item == '2':
            n = int(input('How many Cupcakes do you want to add?'))
            if n<=100:
                self.items_dict['Cupcakes'][0]+=n
            else:
                print('This exceeds our stores limit.')

        elif item == '3':
            n = int(input('How many Brownies do you want to add?'))
            if n<=100:
                self.items_dict['Brownies'][0]+=n
            else:
                print('This exceeds our stores limit.')

        elif item == '4':
            n = int(input('How many Sundaes do you want to add?'))
            if n<=100:
                self.items_dict['Sundaes'][0]+=n
            else:
                print('This exceeds our stores limit.')

        elif item == '5':
            n = int(input('How many cookies do you want to add?'))
            if n<=100:
                self.items_dict['Cookies'][0]+=n
            else:
                print('This exceeds our stores limit.')

        elif item == '6':
            n = int(input('How many bread loaves do you want to add?'))
            if n<=100:
                self.items_dict['Bread'][0]+=n

        elif item == '7':
            n = int(input('How many Samosas do you want to add?'))
            if n<=100:
                self.items_dict['Samosas'][0]+=n
            else:
                print('This exceeds our stores limit.')

        elif item == '8':
            n = int(input('How many Rolls do you want to add?'))
            if n<=100:
                self.items_dict['Rolls'][0]+=n
            else:
                print('This exceeds our stores limit.')

        elif item == '9':
            n = int(input('How many Chips packets do you want to add?'))
            if n<=100:
                self.items_dict['Chips'][0]+=n
            else:
                print('This exceeds our stores limit.')

        elif item == '10':
            n = int(input('How many Nimco packets do you want to add?'))
            if n<=100:
                self.items_dict['Nimco'][0]+=n
            else:
                print('This exceeds our stores limit.')
        with open('stock.txt','w') as hd:
            k=[x[0] for x in self.items_dict.values()]
            for i in range(len(k)-1):
                hd.write(f'{k[i]},')
            hd.write(f'{k[-1]}')    
