from collections import deque


def solution(land):
    answer = 0
    cnt = [[] for _ in range(len(land[0]))]  # 각 위치에서 시추관을 넣었을때 발견할 석유량을 저장하는 리스트
    q = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 석유방을 발견하면 그 방의 석유량을 계산하고
    # 각 위치에서 시추했을때 발견할 석유량을 추가한다
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1:
                visit = set()  # 현재 석유를 발견할 수 있는 시추 위치를 저장할 set(중복방지)
                ck = 1  # 석유량을 저장할 변수
                land[i][j] = -1
                q.append((i, j))
                visit.add(j)
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0<=nx<len(land) and 0<=ny<len(land[0]) and land[nx][ny]==1:
                            ck += 1
                            land[nx][ny] = ck
                            q.append((nx, ny))
                            visit.add(ny)
                for v in visit:
                    cnt[v].append(ck)

    # 각 위치에서 시추한 석유량 중 가장 많은 값을 입력한다
    for c in cnt:
        answer = max(answer, sum(c))
    return answer

import sys

land = list(sys.stdin.readline().strip().split("], ["))
land = [list(map(int, l.split(", "))) for l in land]
print(solution(land))