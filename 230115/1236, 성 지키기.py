import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(N)]
r, c = 0, 0
for now in lst:
    if now.count('X') == 0:
        r += 1
for j in range(M):
    ck = True
    for i in range(N):
        if lst[i][j] == 'X':
            ck = False
    if ck:
        c += 1
print(max(r, c))