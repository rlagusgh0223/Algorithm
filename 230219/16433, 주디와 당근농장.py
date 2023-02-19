# 이렇게 구하는게 BFS보다 훨씬 빠르고 메모리도 적게 든다
import sys
N, R, C = map(int, sys.stdin.readline().split())
R, C = R-1, C-1
ground = [['.']*N for _ in range(N)]
ground[R][C] = 'v'
for row in range(N):
    if (R+C)%2 == 0:  # 행과 열 둘 다 홀수이거나 짝수일때
        if row%2 == 0:  # 당근들도 행과 열 둘 다 홀수이거나 짝수인 곳에 심는다
            for col in range(0, N, 2):
                ground[row][col] = 'v'
        else:
            for col in range(1, N, 2):
                ground[row][col] = 'v'
    else:  # 행과 열이 홀짝이거나 짝홀이면
        if row%2 == 0:  # 당근들도 홀짝이나 짝홀인 곳에 심는다
            for col in range(1, N, 2):
                ground[row][col] = 'v'
        else:
            for col in range(0, N, 2):
                ground[row][col] = 'v'
for now in ground:
    print(*now, sep='')