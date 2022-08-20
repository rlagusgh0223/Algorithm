from collections import deque

visit = [[0 for col in range(10)] for row in range(10)]    # 바이러스의 이동 칸을 표시하기 위한 배열
visit2 = [[0 for col in range(10)] for row in range(10)]     # 백트래킹 알고리즘에서 선택한 빈칸을 표시하기 위한 배열
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS():
    global answer

    for x in range(n):
        for y in range(m):
            visit[x][y] = lab[x][y]    # visit배열에 이동할 수 있는 칸과 없는 칸을 구분
            if lab[x][y]==2:    # 해당 칸이 바이러스라면
                queue.append([x, y])    # 큐에 바이러스 위치를 넣는다

    while queue:
        x, y = queue.popleft()
        visit[x][y] = 1
        for i in range(4):
            if 0<=x+dx[i]<n and 0<=y+dy[i]<m and lab[x+dx[i]][y+dy[i]]==0 and visit[x+dx[i]][y+dy[i]]==0:
                queue.append([x+dx[i], y+dy[i]])
                visit[x+dx[i]][y+dy[i]] = 1

    cnt = 0
    for x in range(n):    # n*m 크기의 범위 탐색
        for y in range(m):
            if lab[x][y] == 0 and visit[x][y] == 0:    # 연구실이 빈칸이고 벽이 없다면ㄴ cnt값을 1 증가시킨다
                cnt += 1
    answer = max(answer, cnt)    # answer에 최댓값을 저장한다

def back_Tracking(select):    # 함수의 인자로 빈칸을 선택한 횟수를 받는다
    if select == 3:
        BFS()
        return
    for x in range(n):
        for y in range(m):
            if not lab[x][y] and not visit2[x][y]:    # 연구소가 빈칸이고, 해당 칸을 선택하지 않았다면
                visit2[x][y] = 1    # 해당칸을 선택했다고 표시하고
                lab[x][y] = 1    # 빈칸을 벽으로 만든다
                back_Tracking(select+1)    # 백트래킹 함수에 선택횟수+1인자를 주어 실행
                lab[x][y] = 0    # 백트래킹 함수가 끝난 뒤 벽을 다시 만들고
                visit2[x][y] = 0    # 빈칸을 해제한다

queue = deque()
answer = 0
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]                
back_Tracking(0)
print(answer)