def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

def solution(a, b):
    b //= gcd(a, b)
    while b%2 == 0:
        b //= 2
    while b%5 == 0:
        b //= 5
    return 1 if b==1 else 2

import sys

a, b = map(int, sys.stdin.readline().split())
print(solution(a, b))
