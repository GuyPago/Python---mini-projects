
nums = [1,2,3,4,5,6,7,8,9,10]

nums
nums = list(filter(lambda x: x%2 == 0,nums))
nums = list(map(lambda x: x**x,nums))
nums = [i for i in nums if i%2 ==0]

def is_prime(x):
    flag = 1
    if (x > 1):
        for i in range(2,x):
            if (x%i == 0):
                return False
            else:
                flag = 0

        if flag == 0:
            return True
    else:
        return False
is_prime(11)

def all_primes():
    n = 1000000
    while True:
        if is_prime(n):
            yield n
        n+=1
all_primes()
a = all_primes()
next(a)
for i in all_primes():
    print(i)

    עטינים = [i for i in range(1,9)]


    for עטין in עטינים:
        print(עטין)
