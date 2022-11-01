def go(day, sum):
    global ans
    if day == N:
        ans = max(ans, sum)
        return
    if day > N:
        return
    go(day+1, sum)
    go(day+T[day], sum+P[day])

import sys
N = int(sys.stdin.readline())
T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, sys.stdin.readline().split())
ans = 0
go(0, 0)
print(ans)