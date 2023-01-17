import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
up = [1] * N
down = [1] * N
for i in range(1, N):
    if lst[i-1] <= lst[i]:
        up[i] = up[i-1]+1
    if lst[i-1] >= lst[i]:
        down[i] = down[i-1]+1
print(max(max(up), max(down)))