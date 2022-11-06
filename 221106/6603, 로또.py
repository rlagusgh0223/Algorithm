# 순열로도 가능하고 재귀로도 가능하다
# 둘 다 시간복잡도는 같지만, 재귀를 이용하는걸 추천한다
def next_per(a):
    i = len(a) - 1
    while i>0 and a[i-1] >= a[i]:
        i -= 1
    while i <= 0:
        return False
    j = len(a) - 1
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

import sys
while True:
    k, *a = list(map(int, sys.stdin.readline().split()))
    if k == 0:
        break
    ans = []
    d = [0]*(k-6) + [1]*6
    while True:
        cur = [a[i] for i in range(k) if d[i]==1]
        ans.append(cur)
        if not next_per(d):
            break
    ans.sort()
    for v in ans:
        print(' '.join(map(str, v)))
    print()