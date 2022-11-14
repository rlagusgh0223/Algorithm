def go(day):
    if day == N+1:
        return 0
    if day > N+1:
        return -sys.maxsize
    if d[day] != -1:
        return d[day]
    t1 = go(day+1)
    t2 = P[day] + go(T[day]+day)
    d[day] = max(t1, t2)
    return d[day]

import sys
N = int(sys.stdin.readline())
T = [0] * (N+1)
P = [0] * (N+1)
d = [-1] * (N+1)
for i in range(1, N+1):
    T[i], P[i] = map(int, sys.stdin.readline().split())
print(go(1))