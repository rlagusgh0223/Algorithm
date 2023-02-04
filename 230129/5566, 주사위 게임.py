import sys
N, M = map(int, sys.stdin.readline().split())
lst = [int(sys.stdin.readline()) for _ in range(N)]
ck = [int(sys.stdin.readline()) for _ in range(M)]
now = 0
for i in range(M):
    now += ck[i]
    if now >= N-1:
        print(i+1)
        break
    now += lst[now]
    if now >= N-1:
        print(i+1)
        break