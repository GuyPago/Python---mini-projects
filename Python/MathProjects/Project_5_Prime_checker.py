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
def is_prime(x):
    if (x > 1):
        for i in range(2,x):
            if (x%i == 0):
                return False
        return True
#prime_check(77655577)
#prime_check(1446111)


# Print specific primes range:

def prime_range(start=1,end=10):
    while (start < end):
        if is_prime(start):
            yield start
        start+=1
for i in prime_range(10000,11000):
    print(i)

# Print all primes :
def all_primes():
    n = 1000000
    while True:
        if is_prime(n):
            yield n
        n+=1
for i in all_primes():
    print(i)
