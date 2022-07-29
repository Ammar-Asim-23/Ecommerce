from Cart import ShoppingCart
class Person:
    def __init__(self,name,password,email,address,id=0):
        self.name=name
        self.password=password
        self.email=email
        self.address=address
        self.id=id
        self.cart=ShoppingCart()
        
class User(Person):
    def __init__(self, name, password, email, address,id=0):
        super().__init__(name, password, email, address) 
        self.id=id
        self.cart=ShoppingCart()
        self.generate_id() 
        with open('user.txt','a') as hd:
            hd.write(f'\n{self.name}_{self.password}_{self.email}_{self.address}_{self.id}')
           
    
    def generate_id(self):
                id_1= User.get_user_list()[-1][-1]
                self.id=str(int(id_1)+1)
    @classmethod
    def get_user_list(cls):
        with open('user.txt') as hd:
            raw=hd.read()
            data=raw.split('\n')
            final=[]
            for i in data:
                final.append(i.split('_'))
            return final    
class Admin(Person):
    def __init__(self):
        super().__init__('admin','admin1234','admin1234@gmail.com','NED University CIS Department')
        self.id=1
       






