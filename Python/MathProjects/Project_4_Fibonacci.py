# fibonacci serie up to 'n'

def fibonacci(n):
    a1,a2 = 0,1
    i = 0
    print('fibonacci serie up to',str(n)+':\n')
    print(a1, end=', ')
    while  (i < n):
        an = a1 + a2
        print(an, end=', ')
        a1 = a2
        a2 = an
        i+=1
