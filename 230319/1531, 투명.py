import sys
N, M = map(int, sys.stdin.readline().split())
mosaic = [[0]*101 for _ in range(101)]
ans = 0
for _ in range(N):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    # 면적을 구하는 거니까 상하반전됐다고 가정하고 간단하게 구한다
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            mosaic[i][j] += 1
            # M보다 많이 덧붙인 처음 한 경우만 계산한다
            # 만약 이후에 종이를 덧붙일 경우 계산하지 않는다
            if mosaic[i][j] == M+1:
                ans += 1
print(ans)