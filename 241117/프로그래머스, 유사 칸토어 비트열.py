def count(n, k):
    if n == 0:
        return 1 if k>0 else 0
    
    div = 5 ** (n-1)
    count_one = 4 ** (n-1)
    now = (k-1) // div

    if now == 2:
        return count_one * now
    elif now < 2:
        return count_one*now + count(n-1, k - (now*div))
    else:
        return count_one*(now-1) + count(n-1, k - (now*div))

def solution(n, l, r):
    return count(n, r) - count(n, l-1)

import sys

n, l, r = map(int, sys.stdin.readline().split())
print(solution(n, l, r))