import time


def dots(dot=3,t=0.5):
    for i in range(dot):
        print('.',end='',flush=True)
        time.sleep(t)



dots()
