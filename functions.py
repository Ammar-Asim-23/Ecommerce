
class Dict(dict):
    def __add__(self,other):
        '''
        appends values of same keys together
        '''
        if self != False:    
            d1 = self.items()
            d2 = other.items()
            res = []
            for a, b in d1:
                for i, j in d2:
                    if a == i:
                        k = b + j
                        res.append((a, k))
            result = dict()
            for i, j in res:
                result[i] = j
            return result


def sub_dict(dict_1, dict_2):
    '''
    gets difference of values of same keys
    '''
    d1 = dict_1.items()
    d2 = dict_2.items()
    res = []

    for a, b in d1:
        for i, j in d2:
            if a == i:
                k = b - j
                res.append((a, k))
    result = dict()
    for i, j in res:
        result[i] = j
    return result


def dict_split_list(dict_):
    '''
    splits the dictionary based on the number of elements 
    in values and puts them as elements of a list.
    '''
        
    list_1 = []
    list_2 = []
    for i in dict_.values():
        try:
            if type(i) == list:
                list_1.append(i[0])
                list_2.append(i[-1])
            else:
                raise TypeError    
        except TypeError:
            list_1.append(i)
            list_2.append(i)

    key = list(dict_.keys())
    d1 = Dict()
    d2 = Dict()
    for i in range(len(key)):
        d1[key[i]] = [list_1[i]]
        d2[key[i]] = [list_2[i]]
    return [d1, d2]


def dict_filter(d):
    new=Dict()
    a=d.keys()
    k=[x for x in d.values()]
    k=k[1:]
    b=[]
    for i in k:
        b.append(list(i.values()))   
    c=[]
    for i in a:
        if i != 'Unnamed: 0':    
            c.append(i)
    for i in range(len(c)):
        new[c[i]]=b[i] 
    return new  

def update_dict(dict_1, dict_2):
    '''
    used to give sum of the values of same position
    '''
    l1=dict_split_list(dict_2)


    return dict_1 + l1[0]  
