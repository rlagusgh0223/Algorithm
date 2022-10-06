import sys
N, M = map(int, sys.stdin.readline().split())
S = []
cnt = 0
for i in range(N):
    S.append(sys.stdin.readline().rstrip())
for i in range(M):
    now = sys.stdin.readline().rstrip()
    if now in S:
        cnt += 1
print(cnt)