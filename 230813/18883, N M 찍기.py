import sys
N, M = map(int, sys.stdin.readline().split())
for now in range(1, N*M +1):
    if now%M == 0:
        print(now)
    else:
        print(now, end = ' ')