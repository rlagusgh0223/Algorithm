import sys
n, m = map(int, sys.stdin.readline().split())
bing = [list(sys.stdin.readline().split()) for _ in range(n)]
go = [[0]*n for _ in range(m)]
bnum, gnum = [], []
for i in range(n):
    bmax = 0
    for j in range(m):
        go[j][i] = bing[i][j]
        bmax += bing[i][j].count('9')
    bnum.append(bmax)
for i in range(m):
    gmax = 0
    for j in range(n):
        gmax += go[i][j].count('9')
    gnum.append(gmax)
print(sum(bnum) - max(max(bnum), max(gnum)))