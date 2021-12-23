from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = deque()
cnt = 0

endFlag = True

while endFlag:                      # 입력이 잘못될 경우 계속 반복
    N = int(sys.stdin.readline())   # 복도의 크기 입력
    graph = ['X'] * N               # 복도의 내용 입력할 리스트
    t = 0                           # 선생님, 학생, 엄폐물 여부 입력할 변수
    s = 0
    x = 0

    if 3 <= N <= 6:                 # 복도 크기 범위 넘어가는지 확인
        for i in range(N):          # 선생님, 학생, 엄폐물 입력
            graph[i] = list(sys.stdin.readline().split())
        for i in range(N):          # 선생님, 학생, 빈 공간 계산 및 선생님 위치 큐에 입력
            for j in range(N):
                if graph[i][j] == 'T':
                    T.append([i,j])
                    t += 1
                elif graph[i][j] == 'S':
                    s += 1
                elif graph[i][j] == 'X':
                    x += 1
        if t <= 5 and s <= 30 and x >=3:    # 입력 가능한 숫자 만큼만 입력해야 계산 진행
            endFlag = False
        else:
            print("입력수 오류")
    else:
        print("잘못된 입력")

EndFlag = True
for i in range(len(T)):     # T 바로 옆에 S가 있으면 벽을 세워도 엄폐가 안되므로 그냥 끝
    x, y = T[i]
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 'S':
                print('-1')
                EndFlag = False
                break
    if not EndFlag:
        break

while T and EndFlag:        # 선생과 바로 붙어있지 않으면 선생으로부터 근처를 확인해가면 학생 앞에 엄폐물 설치
    x, y = T.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 'X':
                graph[nx][ny] = cnt
                T.append([nx,ny])
            elif graph[nx][ny] == 'S':
                graph[x][y] = 'O'
                cnt += 1

if cnt == 3 and EndFlag:
    print('YES')
else:
    print('NO')

for i in range(N):
    print(graph[i])