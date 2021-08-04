import numpy as np


def is_contain_zero(m):
    return np.any(m == 0)


def all_are_even(m):
    return np.all(m%2 == 0)
    
stores = np.array ( ['amazon', 'barnes and noble', ' costco ', 'dunkin donuts', ' errocca', 'foot locker ', 'groceries', 'hoodies', 'idigital ', 'jeans'])
shoppers = np.array ( ['avi ', 'benny', 'charlie ', 'dan', 'eli ', 'fred ', 'gal', 'harry', 'ilan ', 'john'])
data = np.array( [ [ 13 , 87 , 94 , 20 , 14 , 98 , 47 , 75 , 73 , 12],
[14 , 33 , 36 , 70 , 53 , 22 , 55 , 67 , 73 , 43],
[58 , 15 , 27 , 63 , 9 , 54 , 77 , 61 , 7 , 71],
[76 , 55 , 15 , 23 , 3 , 62 , 19 , 89 , 16 , 68],
[39 , 63 , 94 , 9 , 10 , 2 , 12 , 93 , 24 , 12],
[15 , 0 , 47 , 35 , 69 , 100 , 75 , 44 , 84 , 80],
[61 , 92 , 71 , 67 , 90 , 47 , 16 , 96 , 92 , 96],
[67 , 42 , 60 , 75 , 48 , 68 , 30 , 97 , 36 , 39],
[57 , 81 , 23 , 76 , 58 , 24 , 51 , 71 , 45 , 38],
[14 , 74 , 45 , 53 , 53 , 48 , 88 , 48 , 16 , 42] ])


print(np.sum(data, axis=0))
print(np.sum(data, axis=1))
print(np.max(np.sum(data,axis=0)))
store = np.argmax(np.sum(data, axis=0))
print(stores[store])
cheapest_idx = np.argmin(np.sum(data, axis=1))
print(f'Cheapest customer is {shoppers[cheapest_idx]}!')

print(np.any(np.sum(data,axis=0)==0))
print(np.any(np.min(data,axis=0)>0))

print(np.sum(np.average(data, axis=1)>50))
print(np.sum(np.any(data>90, axis=1)))
print(np.sum(data[data<10]))

print(shoppers[np.any(data>90, axis=1)])