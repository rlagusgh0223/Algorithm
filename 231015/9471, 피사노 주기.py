def check(M):
    ans = 1
    mod1, mod2 = 1, 2
    while True:
        if mod1%M == mod2%M == 1:
            return ans
        ans += 1
        mod1, mod2 = mod2, (mod1+mod2)%M

import sys
P = int(sys.stdin.readline())
for i in range(1, P+1):
    N, M = map(int, sys.stdin.readline().split())
    print(i, check(M))