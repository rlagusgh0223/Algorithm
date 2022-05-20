from collections import deque

visit = [[0 for col in range(10)] for row in range(10)]    # 이후에 BFS알고리즘에서 바이러스의 이동 칸을 표시하기 위한 배열
visit2 = [[0 for col in range(10)] for row in range(10)]    # 이후에 백트래킹 알고리즘에서 선택한 빈칸을 표시하기 위한 배열
dx = [0, 0, 1, -1]    # 상하좌우로 이동하기 위한 배열
dy = [1, -1, 0, 0]

def bfs():
    global answer

    for x in range(n):    # 연구소의 크기 탐색
        for y in range(m):
            visit[x][y] = lab[x][y]    # visit 배열에 이동할 수 있는 칸과 없는 칸을 구분
            if lab[x][y] == 2:    # 해당 칸이 바이러스라면 큐에 바이러스 위치를 넣는다
                queue.append([x, y])

    while queue:    # 큐가 비어있기 전끄지 무한 반복
        x, y = queue.popleft()    # 큐의 전단 위치를 꺼낸다
        visit[x][y] = 1    # 바이러스들의 위치(x,y)를 방문했다면 1로 설정해두어 다음에 이동할 수 없게 해둔다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0 and visit[nx][ny] == 0:    # 이동할 수 있는 값이고, 연구실이 빈칸이고 방문하지 않았다면
                queue.append([nx, ny])    # 큐에 이동할 칸의 위치를 넣어주고
                visit[nx][ny] = 1    # 이동할 칸은 방문했음을 표시한다

    cnt = 0    # 백트랙킹에 의해 실행된 각각의 bfs마다 안전구역을 저장하기 위한 cnt변수 생성
    for x in range(n):
        for y in range(m):
            if lab[x][y] == 0 and visit[x][y] == 0:    # 연구실이 빈칸이고 벽이 없다면
                cnt += 1    # cnt 값 1 증가
    answer = max(answer, cnt)    # 안전구역의 최댓값 저장

def back_Tracking(select):    # 함수의 인자로 빈칸을 선택한 횟수를 받는다
    if select == 3:    # 빈 칸을 3개 선택했다면 bfs함수를 실행한 후 return
        bfs()
        return
    for x in range(n):    # 연구소의 크기 n*m을 탐색
        for y in range(m):
            if not lab[x][y] and not visit2[x][y]:    # 연구소가 빈칸이고 not lab[x][y], 해당 칸을 선택하지 않았다면 not visit2[x][y]
                visit2[x][y] = 1    # 백트래킹으로 1개를 선택하기 전에 visit2[x][y]=1을 선택해, 해당칸[x,y]은 선택했음을 표시하고
                lab[x][y] = 1    # 빈칸을 벽으로 만든다
                back_Tracking(select + 1)    # 그 후 백트래킹 함수에 선택횟수+1인자를 주어 실행
                visit2[x][y] = 0    # 백트래킹 함수가 끝난 뒤 선택한 빈칸을 해제하고
                lab[x][y] = 0    # 벽을 다시 빈칸으로 만든다

queue = deque()    # 큐 자료구조를 사용한다
answer = 0    # 최댓값 저장용 변수를 0으로 초기화
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
back_Tracking(0)    # 백트래킹 함수 실행 인자. 빈칸을 선택한 회수 0을 넘겨준다
print(answer)