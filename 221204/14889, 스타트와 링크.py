# 해당 코드는 pypy3로 해야 시간초과 안나온다
def next_p(a):
    i = len(a) - 1
    while i>0 and a[i-1]>=a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[i-1] >= a[j]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

import sys
N = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
b = [0 if i<N/2 else 1 for i in range(N)]
ans = sys.maxsize
while True:
    first = []
    second = []
    for i in range(N):
        if b[i] == 0:
            first.append(i)
        else:
            second.append(i)
    one = two = 0
    for i in range(N//2):
        for j in range(N//2):
            if i == j:
                continue
            one += a[first[i]][first[j]]
            two += a[second[i]][second[j]]
    diff = abs(one - two)
    if ans > diff:
        ans = diff
    if not next_p(b):
        break
print(ans)