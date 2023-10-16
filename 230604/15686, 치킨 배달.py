# N은 50, M은 13이 최대 이므로 왠만해선 시간이 부족할 일은 없을 것 같다
# 치킨집을 모두 입력받아서 각각의 치킨집에서 집마다의 거리를 리스트로 만들고,
# 그 거리 리스트들의 최솟값을 더한다
def DFS(chicken, x, y):  # 치킨집 위치가 저장된 리스트, 이전에 치킨집의 x좌표, y+1좌표(또는 시작 좌표)
    if len(chicken) == M:  # M개의 치킨집에 대하여
        global ans
        h = copy.deepcopy(house)  # 각 집의 거리를 확인하기 위한 리스트 복사(원본을 유지해야 다음 M개의 치킨집에도 검사 가능)
        # M개의 치킨집들과 비교하여 집에서 가장 가까운 치킨집 거리 저장
        for x, y in chicken:
            cnt = 0  # [0, 0]부터 시작한 집 번호
            for i in range(N):
                for j in range(N):
                    if road[i][j] == 1:
                        h[cnt] = min(h[cnt], abs(i-x)+abs(j-y))
                        cnt += 1
        ans = min(ans, sum(h))  # 지금까지의 최소거리의 합과 현재 치킨집일때 최소거리의 합 중 더 작은 값 입력
        return
    for i in range(x, N):
        if i > x:  # 행이 같다면 열은 이전에 입력된 치킨집 다음부터 시작하고, 행이 다르면 열은 0부터 시작한다
            y = 0
        for j in range(y, N):
            if road[i][j]==2: 
                chicken.append([i, j])
                DFS(chicken, i, j+1)
                chicken.pop()  # DFS를 나왔다는건 M개의 치킨집 검사를 마쳤다는 뜻이므로 마지막에 입력한 치킨집을 빼준다

import sys, copy
N, M = map(int, sys.stdin.readline().split())
road = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
chicken = []  # 치킨집의 위치를 기록할 리스트
cnt = 0  # 집의 수
ans = 1e9  # 최소거리
for i in range(N):  # 집의 수 확인
    cnt += road[i].count(1)
house = [1e9] * cnt  # 집 마다 최소거리를 입력하기 위한 리스트
DFS(chicken, 0, 0)  # 최소 거리 구하는 DFS
print(ans)