import sys
H, W = map(int, sys.stdin.readline().split())
sky = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
check = [[-1]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if sky[i][j] == 'c':
            check[i][j] = 0
        if check[i][j]==-1 and check[i][j-1]>=0:
            check[i][j] = check[i][j-1] + 1
for i in range(H):
    print(*check[i])