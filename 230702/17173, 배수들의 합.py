import sys
N, M = map(int, sys.stdin.readline().split())
K = list(map(int, sys.stdin.readline().split()))
lst = [0] * (N+1)
for now in K:
    cnt = 1
    while cnt*now <= N:
        lst[cnt*now] = cnt*now
        cnt += 1
print(sum(lst))