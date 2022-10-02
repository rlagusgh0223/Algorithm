import sys
N, M = map(int, sys.stdin.readline().split())
pkm = {}
for i in range(N):
    now = sys.stdin.readline().rstrip()
    pkm[now] = i+1
    pkm[str(i+1)] = now

for i in range(M):
    now = sys.stdin.readline().rstrip()
    if pkm[now]:
        print(pkm[now])