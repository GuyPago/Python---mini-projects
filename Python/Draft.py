


def factorial(n):
    assert n>=0, 'Value must be positive'
    assert round(n)==n, 'Value must be integer'
    if (n==0) or (n==1):
        return 1
    else:
        return n*factorial(n-1)

factorial(-1)
