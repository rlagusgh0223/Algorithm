import sys
N, M = map(int, sys.stdin.readline().split())
bread = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
for i in range(N):
    bread[i] = bread[i][::-1]
for i in range(N):
    print(*bread[i], sep='')