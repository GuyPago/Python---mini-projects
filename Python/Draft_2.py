import numpy as np


class family:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age

    def __le__(self, other):
        return self == other or self < other


dad = family('Ram', 56)
mom = family('Tal', 49)
brother_1 = family('Betanir', 22)

lst = ['aba', 'ima', 'betanir', 'guy', 'yulia', 'nookey', 'sol']
print(lst)


def load_tsv_to_dict(path):
    dic = {}
    with open(path, 'r') as f:
        for line in f:
            if line[0] != '#':
                token = line.rstrip().split('\t')
                print(token)
                dic[token[1]] = token[0]
    return dic

def find_best_seller(products):
    dic = {}
    for key in products:
        dic[products[key]] = dic.get(products[key], 0) +1
    return max(dic, key=dic.get)



dic = {'1001': 'Dyson V11 Torque', '2349': 'Xiaomi Not Pro', '3124': 'ESET NOD32 Antivirus', '6786': 'Ninja Shaker',
     '0304': 'ESET NOD32 Antivirus'}

dic2 = {1:2, 4:5, 5:3, 7:3}

print(max(dic2))
dic2.pop(7)
print(max(dic2))

a = np.array([1,3,4,1,2,3,4,2])
print(np.sum(a==1))