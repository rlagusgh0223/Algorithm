def solution(n, k):
    k -= n//10
    return n*12000 + k*2000

import sys

n, k = map(int, sys.stdin.readline().split())
print(solution(n, k))