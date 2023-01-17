import sys
N, P = map(int, sys.stdin.readline().split())
start = N
lst = [0] * P
while True:
    N = (N*start) % P
    if lst[N] == 2:
        break
    lst[N] += 1
print(lst.count(2))