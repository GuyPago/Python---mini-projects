import time

def yulia():
    x = 1
    dot = "."
    print("loading",end='')
    while (x < 12):
        print(dot,end='')
        x += 1
        time.sleep(0.3)


yulia()

list = ['nir','guy','yes']
list * (-1)

list.append('guy2')
print(list)

list.insert(2,'hazze4')
print(list)
print(list.index('bes'))
