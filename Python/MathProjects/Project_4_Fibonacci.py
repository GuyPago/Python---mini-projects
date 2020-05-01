

def fibonacci(n):
    a1 = 0
    a2 = 1
    i = 0
    print('fibonacci serie up to',str(n)+':\n')
    print(a1, end=', ')
    while  (i < n):
        an = a1 + a2
        print(an, end=', ')
        a1 = a2
        a2 = an
        i+=1
