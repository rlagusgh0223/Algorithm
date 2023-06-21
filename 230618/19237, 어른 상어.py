import sys
n, m, k = map(int, sys.stdin.readline().split())

# 모든 상어의 위치와 방향 정보를 포함하는 2차원 리스트
# array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 모든 상어의 현재 방향 정보
directions = list(map(int, sys.stdin.readline().split()))

# 각 위치마다 [특정 냄새의 상어 번호, 특정 냄새의 남은 시간]을 저장하는 2차원 리스트
# smell = [[[0, 0] for _ in range(n)] for _ in range(n)]
smell = [[[0, 0]]*n for _ in range(n)]

# 각 상어의 회전 방향 우선순위 정보
priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):  # 각 상어의 m번동안 회전방향을 입력해야 되는데 1줄에 넣기에는 많아서 밖으로 뺐다
        priorities[i].append(list(map(int, sys.stdin.readline().split())))

# 특정 위치에서 이동 가능한 4가지 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 모든 냄새 정보를 업데이트
def update_smell():
    # 각 위치를 하나씩 확인하며
    for i in range(n):
        for j in range(n):
            # 냄새가 존재하는 경우, 시간을 1만큼 감소시키기
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 상어가 존재하는 해당 위치의 냄새를 k로 설정
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]

# 모든 상어를 이동시키는 함수
def move():
    # 이동 결과를 담기 위한 임시 결과 테이블 초기화
    new_array = [[0]*n for _ in range(n)]
    # 각 위치를 하나씩 확인하며
    for x in range(n):
        for y in range(n):
            # 상어가 존재하는 경우
            if array[x][y] != 0:
                direction = directions[array[x][y]-1]  # 현재 상어의 방향
                found = False
                # 일단 냄새가 존재하지 않는 곳이 있는지 확인
                for index in priorities[array[x][y]-1][direction-1]:  # priorities[현재 상어 번호(array에 입력된 x는 x번 상어를 의미)][상어 방향(1,2,3,4가 각각 상,하,좌,우)] => 현재 상어에서 갈 수 있는 방향 4개를 우선순위대로 index에 입력한다
                    nx = x + dx[index-1]
                    ny = y + dy[index-1]
                    if 0<=nx<n and 0<=ny<n:
                        if smell[nx][ny][1] == 0:  # 냄새가 존재하지 않는 곳이면
                            # 해당 상어의 방향 이동시키기
                            directions[array[x][y]-1] = index
                            # 상어 이동시키기(만약 이미 다른 상어가 있다면 번호가 낮은 상어가 들어가도록 할것)
                            if new_array[nx][ny] == 0:
                                new_array[nx][ny] = array[x][y]
                            else:
                                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])
                            found = True
                            break
                if found:
                    continue
                # 주변에 모두 냄새가 남아 있다면, 자신의 냄새가 있는 곳으로 이동
                for index in priorities[array[x][y]-1][direction-1]:
                    nx = x + dx[index-1]
                    ny = y + dy[index-1]
                    if 0<=nx<n and 0<=ny<n:
                        if smell[nx][ny][0] == array[x][y]:  # 자신의 냄새가 있는 곳이면
                            # 해당 상어의 방향 이동시키기
                            directions[array[x][y]-1] = index
                            # 상어 이동시키기(만약 이미 다른 상어가 있다면 번호가 낮은 상어가 들어가도록 할것)
                            new_array[nx][ny] = array[x][y]
                            break
    return new_array

time = 0
while True:
    update_smell()  # 모든 위치의 냄새를 업데이트
    new_array = move()  # 모든 상어를 이동시키기
    array = new_array  # 맵 업데이트
    time += 1  # 시간 증가

    # 1번 상어만 남았는지 체크
    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False
    if check:
        print(time)
        break

    # 1000초가 지날때까지 끝나지 않았다면
    if time >= 1000:
        print(-1)
        break