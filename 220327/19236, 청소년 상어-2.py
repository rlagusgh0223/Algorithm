import sys, copy

# 4 x 4 크기의 정사각형에 존재하는 각 물고기의 번호(없으면 -1)와 방향 값을 담는 테이블
array = [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, sys.stdin.readline().split()))
    # 매 줄마다 4마리의 물고기를 하나씩 확인하며
    for j in range(4):
        # 각 위치마다 [물고기의 번호, 방향]을 저장
        # 각 줄마다 물고기 번호, 방향 총 8개의 정보가 주어졌으므로 array에는 2개를 한 리스트에 넣는다.
        # [0, 1], [2, 3], [4, 5], [6, 7] 번째 값들이 각각 들어간다
        # 방향은 8가지 방향인데 리스트는 0부터 7까지로 사용하니까 리스트를 이용해서 나온 값에서 1을 빼준다
        array[i][j] = [data[j * 2], data[j * 2 + 1] - 1]
        # print(array)
        # j = 0 -> data[0*2], data[0*2+1]-1  => data[0], data[1]-1
        # j = 1 -> data[1*2], data[1*2+1]-1  => data[2], data[3]-1
        # j = 2 -> data[2*2], data[2*2+1]-1  => data[4], data[5]-1
        # j = 3 -> data[3*2], data[3*2+1]-1  => data[6], data[7]-1

# 8가지 방향에 대한 정의
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 현재 위치에서 왼쪽으로 회전된 결과 반환
def turn_left(direction):
    # 왼쪽으로 45도 회전은 0~7 중 1이 더해진 값
    return (direction+1) % 8

result = 0    # 최종 결과

# 현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:    # array의 i, j는 좌표이며 array에는 0에 번호가, 1에 방향이 있다. index는 찾고있는 특정한 번호의 물고기
                return (i, j)    # 찾고 있는 물고기가 array에 있다면 좌표 리턴
    return None    # 없으면 없다고 리턴

# 모든 물고기를 회전 및 이동시키는 함수
def move_all_fishes(array, now_x, now_y):
    # 1번부터 16번까지의 물고기를 차례대로 (낮은 번호부터) 확인
    for i in range(1, 17):
        # 해당 물고기의 위치 찾기
        position = find_fish(array, i)
        if position != None:    # 이번 번호의 물고기가 있어서 좌표를 받았다면
            x, y = position[0], position[1]    # x, y에 해당 물고기의 좌표 입력
            direction = array[x][y][1]    # 해당 물고기의 방향 입력
            # 해당 물고기의 방향을 왼쪽으로 계속 회전시키며 이동이 가능한지 확인
            for j in range(8):    # 만약 이동이 불가능 하다면 이동 가능한 방향을 찾기 위해 8가지 방향(0 ~ 7) 확인
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 해당 방향으로 이동이 가능하다면 이동시키기
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction    # array에 변경된 방향 입력
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]    # 해당 방향의 물고기와 현재 물고기 변경
                        break    # 동작하면 이제 종료
                direction = turn_left(direction)    # turn_left함수를 이용해 8방향 다 돌린다

# 상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환
def get_possible_positions(array, now_x, now_y):
    positions = []    # 먹을 수 있는 물고기의 위치 리스트
    direction = array[now_x][now_y][1]    # 현재 입력받은 좌표의 물고기의 방향
    # 현재의 방향으로 계속 이동시키기
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        # 범위를 벗어나지 않는지 확인하며
        if 0 <= now_x < 4 and 0 <= now_y < 4:
            # 물고기가 존재하는 경우
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))    # 먹을 수 있는 물고기 리스트에 현재 물고기의 좌표 입력
    return positions

# 모든 경우를 탐색하기 위한 DFS 함수
def DFS(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)    # 리스트를 통째로 복사

    total += array[now_x][now_y][0]    # 현재 위치의 물고기 먹기
    array[now_x][now_y][0] = -1    # 물고기를 먹었으므로 번호 값을 -1로 변환

    move_all_fishes(array, now_x, now_y)    # 전체 물고기 이동시키기

    # 이제 다시 상어가 이동할 차례이므로, 이동 가능한 위치 찾기
    positions = get_possible_positions(array, now_x, now_y)
    # 이동할 수 있는 위치가 하나도 없다면 종료
    if len(positions) == 0:
        result = max(result, total)    # 최댓값 저장
        return
    # 모든 이동할 수 있는 위치로 재귀적으로 수행
    for next_x, next_y in positions:
        DFS(array, next_x, next_y, total)

# 청소년 상어의 시작 위치(0, 0)에서부터 재귀적으로 모든 경우 탐색
DFS(array, 0, 0, 0)
print(result)