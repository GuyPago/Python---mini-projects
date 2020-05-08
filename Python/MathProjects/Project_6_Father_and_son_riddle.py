## QUESTION:
# The ages of father and son add up to 55, and the father's age is the digits of
# the son's age reversed. How old is the father?

father = [i for i in range(1,101)]
son = father.copy()


for i in father:
    for v in son:
        if (i + v == 55) and (i == int(str(v)[::-1])) and (i > v):
            print('Father:', i, 'Son:' ,v)
