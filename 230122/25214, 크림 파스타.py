import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
lst = [0] * N
mini = A[0]
for now in range(1, N):
    if mini > A[now]:
        mini = A[now]
    lst[now] = max(lst[now-1], A[now]-mini)
print(*lst, sep=' ')