#!/usr/bin/env python3

# To run tests:
# python3 -m doctest digstat.py [-v]

def powmod(b,e,m):
    if e == 0:
        return 1

    if e % 2 == 0:
        t = powmod(b, e/2, m)
        return t * t % m
    
    else:
        return b*powmod(b, e-1, m) % m

def genstats(a, n):
    """Print out statistics for last digits in the
       sequence a^1, a^2 … a^(n-1), a^n. Eg:

       >>> genstats(2, 5)
       0: 0, 1: 0, 2: 2, 3: 0, 4: 1, 5: 0, 6: 1, 7: 0, 8: 1, 9: 0
       >>> genstats(3, 2)
       0: 0, 1: 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 1
       >>> genstats(4, 1)
       0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0
       >>> genstats(5, 400)
       0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 400, 6: 0, 7: 0, 8: 0, 9: 0
       >>> genstats(6, 10)
       0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 10, 7: 0, 8: 0, 9: 0
       >>> genstats(7, 100)
       0: 0, 1: 25, 2: 0, 3: 25, 4: 0, 5: 0, 6: 0, 7: 25, 8: 0, 9: 25
       >>> genstats(8, 9121)
       0: 0, 1: 0, 2: 2280, 3: 0, 4: 2280, 5: 0, 6: 2280, 7: 0, 8: 2281, 9: 0
       >>> genstats(9, 12)
       0: 0, 1: 6, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 6
       >>> genstats(3, 100000)
       0: 0, 1: 25000, 2: 0, 3: 25000, 4: 0, 5: 0, 6: 0, 7: 25000, 8: 0, 9: 25000
       >>> genstats(9, 1000000)
       0: 0, 1: 500000, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 500000
       """

    digits = { 0: 0, \
               1: 0, \
               2: 0, \
               3: 0, \
               4: 0, \
               5: 0, \
               6: 0, \
               7: 0, \
               8: 0, \
               9: 0 }
    # For 2, the pattern is 2,4,8,6,2,4 …:
    # >>> for i in range(1,5+1): print(2**i, end=" ")
    # 2 4 8 16 32
    if a == 2:
        digits[2] = (n-1)//4+1 
        if n >= 2: # only any 4s if n is 2 or greater (2^2 = 4) 
            digits[4] = (n-2)//4+1
        if n >= 3: # only any 8s if n is 3 or greater (2^3 = 8) 
            digits[8] = (n-3)//4+1 
        if n >= 4: # only any 6s if n is 4 or greater (2^4 = 16) 
            digits[6] = (n-4)//4+1 

    # For 3, it is: 3,9,7,1,3,9 …: 
    # >>> for i in range(1,10+1): print(3**i, end=" ")
    # 3 9 27 81 243 729 2187 6561 19683 59049 
    elif a == 3:
        digits[3] = (n-1)//4+1 
        digits[9] = (n-2)//4+1
        digits[7] = (n-3)//4+1 
        digits[1] = (n-4)//4+1 

    # For 4, the pattern is:
    # 4,16,64,256 … or 4,6,4,6 … 
    elif a == 4:
        digits[4] = n/2 + n % 2 # Round up
        digits[6] = n/2 # Round down

    elif a == 5 or a == 6:
        #5*5 ends in 5, multiplied by 5 ends in 5 … ditto for 6.
        digits[a] = n
    
    # For 7: 7, 49, 343, 2401, 16807, 117649, 823543, 5764801 … 
    # 7, 9, 3, 1, 7, 9, 3, 1 … 
    elif a == 7:
        digits[7] = (n-1)//4+1 
        digits[9] = (n-2)//4+1
        digits[3] = (n-3)//4+1 
        digits[1] = (n-4)//4+1 

    # 8: 8, 64, 512, 4096, 32768, 262144, 2097152, 16777216 … 
    # 8,4,2,6,8 … 
    elif a == 8:
        digits[8] = (n-1)//4+1 
        digits[4] = (n-2)//4+1
        digits[2] = (n-3)//4+1 
        digits[6] = (n-4)//4+1 

    elif a == 9:
        #similar pattern for 9 (1,9,1,9 … )
        digits[1] = n/2 # Round down
        digits[9] = n/2 + n % 2 # Round up

 

    else:
        for i in range(1,n+1):
            d = powmod(a,i,10)
            digits[d] = digits[d]+1

    print_digits(digits)

def print_digits(digits):
    for k, v in digits.items():
        if (k < 9):
            print("%d: %d" % (k,v), end=", ")
        else:
            print("%d: %d" % (k,v))

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        fn = "-"
    else:
        fn = sys.argv[1]

    if fn == "-":
        file = sys.stdin
    else:
        file = open(fn)

    with file:
        for line in file:
            a,n = [int(x) for x in line.split()]
            genstats(a,n)
