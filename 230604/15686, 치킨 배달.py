# N은 50, M은 13이 최대 이므로 왠만해선 시간이 부족할 일은 없을 것 같다
# 치킨집을 모두 입력받아서 각각의 치킨집에서 집마다의 거리를 리스트로 만들고,
# 그 거리 리스트들의 최솟값을 더한다
def DFS(chicken, x, y):
    if len(chicken) == M:
        global ans
        h = copy.deepcopy(house)
        for x, y in chicken:
            cnt = 0
            for i in range(N):
                for j in range(N):
                    if road[i][j] == 1:
                        h[cnt] = min(h[cnt], abs(i-x)+abs(j-y))
                        cnt += 1
        ans = min(ans, sum(h))
    for i in range(x, N):
        if i == x:
            for j in range(y, N):
                if road[i][j]==2: 
                    chicken.append([i, j])
                    DFS(chicken, i, j+1)
                    chicken.pop()
        else:
            for j in range(N):
                if road[i][j]==2: 
                    chicken.append([i, j])
                    DFS(chicken, i, j+1)
                    chicken.pop()

import sys, copy
N, M = map(int, sys.stdin.readline().split())
road = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
chicken = []  # 치킨집의 위치를 기록할 리스트
house = []  # 집 마다 최소거리를 입력하기 위한 리스트
ans = 1e9  # 최소거리
for i in range(N):
    for j in range(N):
        if road[i][j] == 1:
            house.append(1e9)

DFS(chicken, 0, 0)
print(ans)