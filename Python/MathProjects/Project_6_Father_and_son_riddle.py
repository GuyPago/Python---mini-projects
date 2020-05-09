## QUESTION:
# The ages of father and son add up to 55, and the father's age is the digits of
# the son's age reversed. How old is the father?     # Solution made by GuyPago.

from tqdm import tqdm



# Solution:
father = [i for i in range(1,56)]
son = father.copy()

for i in father:
    for v in son:
        if (i + v == 55) and (i == int(str(v)[::-1])) and (i > v):
            print('Father: {} | Son: {}'.format(i,v))
            flag = 1



# General solution function:
def quest(sum=55):
    father = [i for i in range(1,sum+1)]
    son = father.copy()
    flag = 0
    answers = []
    if (sum > 9999):
        for i in tqdm(father):
            for v in son:
                if (i + v == sum) and (i == int(str(v)[::-1])) and (i > v):
                    answers+=[[i,v]]
                    flag = 1
        if (flag ==1):
                    for c,i in enumerate(answers,1):
                        print(c,'. ',i,sep='')

    else:
        for i in father:
            for v in son:
                if (i + v == sum) and (i == int(str(v)[::-1])) and (i > v):
                    print('Father: {} | Son: {}'.format(i,v))
                    flag = 1
    if (flag == 0):
        print('No possible answers')
    print('\n')


def try_sum():
    while True:
        try:
            quest(int(input('Enter sum:\n')) or 0)
        except ValueError:
            print('Error, not a number !\n')


# Another solution by generator function
def quest_2(sum=5555):
    father = [i for i in range(1,sum+1)]
    son = father.copy()

    for i in father:
        for v in son:
            if (i + v == sum) and (i == int(str(v)[::-1])) and (i > v):
                yield i,v

def try_sum2():
    while True:
        try:
            for c,i in enumerate(quest_2(int(input('Enter sum:\n') or 0)),1):
                print(c,'. ',i,sep='')
        except (ValueError,TypeError):
            print('Error, not a number !')
        print('\n')
#try_sum()
try_sum2()

for c,i in enumerate(quest_2(),1):
    print(c,'. ',i,sep='')
