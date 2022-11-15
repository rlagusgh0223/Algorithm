# c++, java는 d[i-1]같은거 할때마다 %=mod를 해야하지만
# 파이썬은 그렇게 하면 시간초과 난다
import sys

mod = 1000000009
d = [0] * 1000001
d[0] = 1

for i in range(1, 1000001):
    if i-1 >= 0:
        d[i] += d[i-1]
    if i-2 >= 0:
        d[i] += d[i-2]
    if i-3 >= 0:
        d[i] += d[i-3]
    d[i] %= mod

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(d[n])