def gcd(x, y):
    if y==0:
        return x
    else:
        return gcd(y, x%y)

import sys
x, y = map(int, sys.stdin.readline().split())
g = gcd(x, y)
print(g)
print(x*y//g)