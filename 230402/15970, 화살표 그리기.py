import sys
N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = [0] * N
for i in range(N):
    X, Y = lst[i][0], lst[i][1]
    minX = sys.maxsize
    for j in range(N):
        if i == j:
            continue
        x, y = lst[j][0], lst[j][1]
        if Y==y and abs(X-x) < minX:
            minX = abs(X-x)
    ans[i] = minX
print(sum(ans))