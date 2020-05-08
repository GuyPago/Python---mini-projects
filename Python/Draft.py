

father = [i for i in range(1,101)]
son = father.copy()


for i in father:
    for v in son:
        if (i + v == 55) and (i == int(str(v)[::-1])) and (i > v):
            print('Father:', i, 'Son:' ,v)
