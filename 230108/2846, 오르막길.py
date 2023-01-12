import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
ck = [0] * N
start = lst[0]
for i in range(1, N):
    if lst[i-1] >= lst[i]:
        start = lst[i]
    ck[i] = lst[i]-start
print(max(ck))