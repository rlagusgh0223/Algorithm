from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 그래프는 -1, 다각형 안은 0, 다각형의 테두리는 1로 표시한다
    # 단, 입력받은 좌표대로 하면 연결되지 않고 인접한 테두리를 연결된걸로 인식할 수 있으므로
    # 2를 곱해 연결된 테두리만 연결될 수 있도록 한다
    # 좌표는 1부터 50까지 주어지지만 그래프는 0~50까지 있으므로
    # 2를 곱해서 모두 표시하려면 0~101이 있어야 한다
    graph = [[-1]*102 for _ in range(102)]
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x:x*2, r)
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if x1<x<x2 and y1<y<y2:
                    graph[x][y] = 0
                elif graph[x][y] == -1:
                    graph[x][y] = 1
    # 모든 좌표에 2를 곱해서 위의 그래프에 맞게 입력할 수 있게 한다
    cX, cY, iX, iY = characterX*2, characterY*2, itemX*2, itemY*2
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # BFS를 이용해 가장 짧은 테두리 경로 확인
    q = deque()
    q.append((cX, cY))
    visit = [[-1]*102 for _ in range(102)]
    visit[cX][cY] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx==iX and ny==iY:
                answer = (visit[nx][ny]+1) // 2
            if 0<=nx<102 and 0<=ny<102:
                if graph[nx][ny]==1 and visit[nx][ny]==-1:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))
    return answer



import sys
rectangle = list(sys.stdin.readline().strip().split("],["))
rectangle = [list(map(int, r.split(","))) for r in rectangle]
characterX, characterY, itemX, itemY = map(int, sys.stdin.readline().split())
print(solution(rectangle, characterX, characterY, itemX, itemY))