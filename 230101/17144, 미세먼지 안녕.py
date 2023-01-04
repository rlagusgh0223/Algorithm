import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 맵의 크기(R X C)와 T초 정보 입력
r, c, t = map(int, input().split())
arr = []  # 전체 맵의 상태(미세먼지)
# 공기청정기의 위 칸(up_position), 아래 칸(down_position)
up_position = None
down_position = None
for i in range(r):
    arr.append(list(map(int, input().split())))
    for j in range(c):
        if arr[i][j] == -1:  # 공기청정기인 경우
            up_position = (i-1, j)
            down_position = (i, j)

# 공기청정기의 위 칸 처리하기(U -> R -> D -> L 순서로 처리)
def up(arr, x, y, direction):
    if direction == 'U':
        nx, ny = x-1, y  # 위쪽 끝까지 도달한 경우
        if nx == -1:
            direction = 'R'
    if direction == 'R':
        nx, ny = x, y+1  # 오른쪽 끝까지 도달한 경우
        if ny == c:
            direction = 'D'
    if direction == 'D':
        nx, ny = x+1, y   # 아래쪽 끝까지 도달한 경우
        if nx == up_position[0] + 1:
            direction = 'L'
    if direction == 'L':
        nx, ny = x, y-1
    # 공기청정기로 돌아올 때까지
    if (nx, ny) !=up_position:
        # (nx, ny) 위치에 잇는 미세먼지를 (x, y) 위치로 이동
        arr[x][y] = arr[nx][ny]
        up(arr, nx, ny, direction)

# 공기청정기의 아래 칸 처리하기(D -> R -> U -> L 순서로 처리)
def down(arr, x, y, direction):
    if direction == 'D':
        nx, ny = x+1, y  # 아래쪽 끝까지 도달한 경우
        if nx == r:
            direction = 'R'
    if direction == 'R':
        nx, ny = x, y+1  # 오른쪽 끝까지 도달한 경우
        if ny == c:
            direction = 'U'
    if direction == 'U':
        nx, ny = x-1, y  # 위쪽 끝까지 도달한 경우
        if nx == down_position[0] - 1:
            direction = 'L'
    if direction == 'L':
        nx, ny = x, y-1
    # 공기청정기로 돌아올 때까지
    if (nx, ny) != down_position:
        # (nx, ny) 위치에 잇는 미세먼지를 (x, y) 위치로 이동
        arr[x][y] = arr[nx][ny]
        down(arr, nx, ny, direction)

# 공기청정기 순환 함수
def cycle():
    global arr
    x, y = up_position
    up(arr, x-1, y, 'U')  # U -> R -> D -> L 순서대로 처리
    arr[x][y+1] = 0  # 바로 오른쪽 칸은 0
    x, y = down_position
    down(arr, x+1, y, 'D')  # D -> R -> U -> L 순서대로 처리
    arr[x][y+1] = 0  # 바로 오른쪽 칸은 0

# T초만큼 반복
for _ in range(t):
    result = [[0]*c for _ in range(r)]  # 한 번 확산한 뒤의 결과 배열
    for x in range(r):  # 각 위치에 대하여 미세먼지 확산
        for y in range(c):
            if arr[x][y] == -1:  # 공기청정기가 있는 경우 무시
                result[x][y] = -1
                continue
            diffuse = arr[x][y] // 5  # 상, 하, 좌, 우 위치로 arr[x][y] // 5 만큼식 확산
            summary = 0
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx<0 or ny<0 or nx>=r or ny>=c:  # 범위를 벗어나는 경우 무시
                    continue
                if arr[nx][ny] == -1:  # 공기청정기가 있는 경우 무시
                    continue
                summary += diffuse  # 확산된 양
                result[nx][ny] += diffuse
            result[x][y] += arr[x][y] - summary  # 확산되지 않고, 남아있는 미세먼지
    arr = result  # 확산 완료
    cycle()  # 공기청정기 가동

answer = 0
for row in arr:
    answer += sum(row)
print(answer + 2)  # 공기 청정기로 2 감소한 것 되돌리기