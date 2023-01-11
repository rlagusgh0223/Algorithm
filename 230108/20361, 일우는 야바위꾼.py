import sys
N, X, K = map(int, sys.stdin.readline().split())
lst = [0] * (N+1)
lst[X] = 1
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    lst[x], lst[y] = lst[y], lst[x]
print(lst.index(1))