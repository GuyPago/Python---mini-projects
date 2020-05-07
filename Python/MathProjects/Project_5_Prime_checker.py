# Check if number is prime:
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
prime_check(1446111)




# Print all primes :

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

def all_primes():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n+=1

for i in all_primes():
    print(i)
