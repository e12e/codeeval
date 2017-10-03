#!/usr/bin/env python3.4
"""
Simple doctest:

>>> fizzbuzz("sample.txt")
1 2 F 4 B F 7 8 F B
1 F 3 F 5 F B F 9 F 11 F 13 FB 15
"""

def fizzbuzz(filename):
    with open(filename) as file:
        for line in file:
            print(*fizzline(*[int(x) for x in line.split()]))

"""Takes 3 numbers, x, y and, and prints out a list from
1...n inclusive with numbers that divide by x replaced by
F, and numbers that divide by y with B, and numbers that
divide by x and y by FB.

Eg:

>>> fizzline(3, 5, 10)
1 2 F 4 B F 7 8 F B
"""
def fizzline(x, y, n):
    ret = []
    for i in range(1,n+1):
        if not i % x:
            if not i % y:
                ret.append('FB')
            else:
                ret.append('F')
        elif not i % y:
                ret.append('B')
        else:
            ret.append(i)
    return ret

def usage():
    print("""fizzbuzz:
    Test:
       python3 -m doctest -v fizzbuzz.py

    Run:
        python3 fizzbuzz.py sample.txt
        """)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        usage()
    else:
        fizzbuzz(sys.argv[1])
