import sys
input = sys.stdin.readline
N, M = map(int, input().split())
t = [list(input().rstrip()) for _ in range(N)]
for i in range(1, N):
    ck = False
    for j in range(1, M+1):
        if t[i][M-j:] == t[i-1][:j]:
            ck = True
            break
        if t[i][:j] == t[i-1][M-j:]:
            ck = True
            break
    if not ck:
        print(0)
        exit()
print(1)