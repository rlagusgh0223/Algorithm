import sys
N, K = map(int, sys.stdin.readline().split())
lst = []
for i in range(1, K+1):
    now = str(N*i)
    lst.append(int(now[::-1]))
print(max(lst))