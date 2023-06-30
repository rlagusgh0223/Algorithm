# pypy3로 제출해야 된다
import sys
N, C = map(int, sys.stdin.readline().split())
bomb = [0] * (C+1)
ans = 0
for i in range(N):
    n = int(sys.stdin.readline())
    for j in range(n, C+1, n):
        if bomb[j] == 0:
            bomb[j] = 1
            ans += 1
print(ans)