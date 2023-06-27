from math import gcd
import sys
n = int(sys.stdin.readline())
if n == 2:
    a, b = map(int, sys.stdin.readline().split())
    GCD = gcd(a, b)
elif n == 3:
    a, b, c = map(int, sys.stdin.readline().split())
    GCD = gcd(gcd(a, b), c)
lst = set()
for i in range(1, int(GCD**0.5)+1):
    if GCD % i == 0:
        lst.add(i)
        lst.add(GCD//i)
for now in sorted(lst):
    print(now)