from functions import  update_dict ,dict_filter
class ShoppingHistory:
    def __init__(self):
        import pandas as pd
        try:
            self.__history = pd.read_csv('history.csv')
        except ValueError:
            self.__history = pd.DataFrame()

    def update_history(self, cart):
        import pandas as pd
        dict = dict_filter(self.__history.to_dict())
        new = update_dict(dict, cart)
        self.__history = pd.DataFrame(new)

        self.__history.to_csv('history.csv')

    def check_history(self):
        print(self.__history)

    def check_by_order(self,orderno):
        print(self.__history.iloc[[orderno]])    
        
    def check_by_name(self,name):
        print(self.__history.loc[self.__history['User'] == name])
