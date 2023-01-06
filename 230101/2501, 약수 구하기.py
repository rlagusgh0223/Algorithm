import sys
N, K = map(int, sys.stdin.readline().split())
lst = [0] * N
now = 0
for i in range(1, N+1):
    if N%i == 0:
        lst[now] = i
        now += 1
print(lst[K-1])