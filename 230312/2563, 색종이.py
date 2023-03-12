import sys
N = int(sys.stdin.readline())
paper = [[0]*100 for _ in range(100)]
ans = 0
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    x, y = x-1, y-1
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1
for i in range(100):
    ans += paper[i].count(1)
print(ans)