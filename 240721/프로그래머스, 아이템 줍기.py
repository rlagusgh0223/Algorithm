from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    # 정확한 길이의 계산을 위해 좌표를 2배 늘려준다
    cx, cy, ix, iy = characterX*2, characterY*2, itemX*2, itemY*2
    # 다각형의 경계선을 표시하기 위한 리스트
    # 각 값은 50이하인데 2를 곱할 예정이므로 100까지 입력 가능한 리스트를 만든다
    graph = [[-1]*101 for _ in range(101)]
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x:x*2, r)
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                # 사각형 내부일 경우 0으로 표시
                if x1<x<x2 and y1<y<y2:
                    graph[x][y] = 0
                # 사각형의 경계선이고
                # 다른 다각형이 접근한 적이 없다면 1로 경계선 표시
                elif graph[x][y] == -1:
                    graph[x][y] = 1
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    q.append((cx, cy))
    visit = [[0]*101 for _ in range(101)]
    visit[cx][cy] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # 목적지에 최초로 도달한게 가장 짧은 거리이므로 바로 리턴한다
            # 이전 좌표에서 1 더한게 현재 좌표까지의 거리이므로 1 더하고
            # 정확한 계산을 위해 2 곱했던걸 다시 나눠줘서 원래 값으로 만든다
            if nx==ix and ny==iy:
                return (visit[x][y]+1) // 2
            if 0<=nx<101 and 0<=ny<101:
                # 경계선에 있지만 아직 방문하지 않은 경우 방문한걸로 하고 q에 입력한다
                if graph[nx][ny]==1 and visit[nx][ny]==0:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))

import sys

rectangle = list(sys.stdin.readline().strip().split("],["))
rectangle = [list(map(int, r.split(","))) for r in rectangle]
characterX, characterY, itemX, itemY = map(int, sys.stdin.readline().split())
print(solution(rectangle, characterX, characterY, itemX, itemY))