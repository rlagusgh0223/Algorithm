import sys
N = int(sys.stdin.readline())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
value = [[0]*N for _ in range(N)]
value[0][0] = 1
for i in range(N):
    for j in range(N):
        if i==N-1 and j==N-1:  # 이 조건문이 없다면 마지막이 0이므로 [i+0][j], [i][j+0]이 되어서 자기 자신도 더하게 된다
            print(value[i][j])
            break
        now = ground[i][j]
        if i+now < N:
            value[i+now][j] += value[i][j]
        if j+now < N:
            value[i][j+now] += value[i][j]