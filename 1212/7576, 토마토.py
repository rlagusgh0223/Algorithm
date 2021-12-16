from collections import deque
import sys
M, N = map(int, sys.stdin.readline().split())               #가로, 세로 범위 입력
box = [0] * N                                               #박스 안에 토마토 상태 입력
for i in range(N):
    box[i] = list(map(int, sys.stdin.readline().split()))

visited = [[0 for _ in range(M)] for _ in range(N)]         #확인한건지 안 한건지 확인할 리스트 작성
dx = [-1, 1, 0, 0]                                          #상, 하, 좌, 우를 확인하기 위한 리스트
dy = [0, 0, -1, 1]

q = deque()                 #큐 선언
    
for i in range(N):                      #1이 있는 위치를 먼저 큐에 입력하고 while문을 돌려야 1이 2개 이상 있을때 동시에 최종일수를 구할 수 있다
    for j in range(M):
        if box[i][j] == 1:              #익은 토마토가 있다면 큐에 좌표 입력(시간초과 때문에 따로 해봐야 겠다)
            q.append([i, j])
            visited[i][j] = 1           #이게 없으면 출발점을 0으로 하게 되는데, 0이 있으면 익지 않은게 하나 있는걸로 인식되니까 1로 수정
        elif box[i][j] == -1:           #box가 -1이면 아예 접근을 못하는데 visited는 0으로 체크를 안한걸로 되니까 visited를 -1로 수정
            visited[i][j] = -1

while q:                    #큐가 있는 한 반복
    x, y = q.popleft()      #큐에 가장 먼저 입력한 값 출력하여 x, y 좌표로 입력
    for i in range(4):      #상, 하, 좌, 우 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:                     #다음 좌표가 토마토 박스 안에 있다면
            if box[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1         #다음 위치에 수 체크
                q.append([nx, ny])                          #다음 좌표 큐에 입력하여 계속 진행하게 한다

ans = visited[0][0]                         #ans 초기값으로 아무거나 준다. 어차피 다른 값이랑 비교하는거니까
endFlag = True                              #하나라도 익지 않는 경우가 있을때
for i in range(N):
    for j in range(M):
        if visited[i][j] != 0:              #익었거나(1) 벽(-1)이라면 이미 나온 결과값 중 가장 큰 값, 즉 마지막으로 익은날 ans에 저장
            ans = max(visited[i][j], ans)
        else:
            print('-1')                     #하나라도 익게 하지 못한다면 어차피 결과는 -1이니까 바로 종료
            endFlag = False
            break
    if not endFlag:
        break

if endFlag:             #모두 익은 상태라면 최댓값-1(시작위치부터 카운트했기 때문에 하루 빼줘야 한다.)
    print(ans-1)