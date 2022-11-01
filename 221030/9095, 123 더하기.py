def go(sum, n):
    if sum > n:
        return 0
    elif sum == n:
        return 1
    now = 0
    for i in range(1, 4):
        now += go(sum+i, n)
    return now

import sys
T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    print(go(0, n))