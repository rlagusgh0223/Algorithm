def gcd(n1, n2):
    while n1%n2 > 0:
        n1, n2 = n2, n1%n2
    return n2

def solution(numer1, denom1, numer2, denom2):
    n = numer1*denom2 + numer2*denom1  # 분자
    d = denom1*denom2  # 분모
    g = gcd(n, d)  # 분자와 분모 간의 최대공약수
    return [n//g, d//g]

import sys

n1, d1, n2, d2 = map(int, sys.stdin.readline().split())
print(solution(n1, d1, n2, d2))