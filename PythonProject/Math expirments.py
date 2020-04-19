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
