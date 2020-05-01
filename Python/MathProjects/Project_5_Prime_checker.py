
def prime_check(n):
    flag = 1
    for i in range(2,n):
        if (n % i == 0):
            print(n,'is not a prime number.\n'+str(i),'x',int(n/i),'is',n)
            flag = 0
            break
    if flag == 1:
        print(n,'is a prime number')


prime_check(77655577)
