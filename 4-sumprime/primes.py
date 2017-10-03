#!/usr/bin/env python3

# Finding the first n primes:

def isprime(n=2, primes=None):
    """Retuns true if @n is prime relative to all integers
       in @primes, otherwise false."""
    for p in primes:
        if not n % p:
            return False
    return True

def nextprime(current_max=2, primes=None):
    """Given a current max prime candidate, current_max, and a set of
    primes less than current_max, finds the next prime number higher
    than or equal to current_max.
    
    Returns a tuple of the next prime, and a set of primes including the
    recently found prime."""

    if primes is None:
        primes = {2}

    candidate = current_max+1

    if isprime(candidate, primes):
        primes.add(candidate)
        return (candidate, primes)
    else:
        return nextprime(candidate, primes)

def firstnprimes(n):
    """Returns a set of the first n prime numbers. Eg:

    >>> firstnprimes(10)
    {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
    """

    cur,primes = nextprime()

    while len(primes) < n:
        cur,primes = nextprime(cur,primes)

    return primes

def sumnprimes(n):
    """Returns the sum of the first n primes.

    >>> sumnprimes(3)
    10
    >>> sumnprimes(1000)
    3682913
    """
    return sum(firstnprimes(n))

if __name__ == "__main__":
    print(sumnprimes(1000))
