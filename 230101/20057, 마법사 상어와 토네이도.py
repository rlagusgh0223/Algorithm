# 지속적인 공부 필요
def move():
    global x, y, direction, turned, moved, target
    if moved == target:  # 충분히 이동했다면 회전 수행
        moved = 0
        turned += 1
        direction = (direction+1) % 4
    if turned == 2:  # 2번 회전했다면, 이동할 칸 수 증가
        turned = 0
        target += 1
    # 다음 위치로 이동
    x = x + dx[direction]
    y = y + dy[direction]
    moved += 1

# 방향별 모래 비율
left = [
    (-2, 0, 0.02), (-1, -1, 0.10), (-1, 0, 0.07),
    (-1, 1, 0.01), (0, -2, 0.05), (1, -1, 0.10),
    (1, 0, 0.07), (1, 1, 0.01), (2, 0, 0.02)
]
down = [(-y, x, val) for x, y, val in left]
right = [(x, -y, val) for x, y, val in left]
up = [(y, x, val) for x, y, val in left]
ratio = [left, down, right, up]

import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
x = n//2
y = n//2
direction = 0  # 방향(서, 남, 동, 북)
turned = 0  # 회전한 횟수
moved = 0  # 현재 방향으로 이동한 수
target = 1  # 이동할 칸 수
result = 0  # 맵을 벗어나는 모래의 양
cnt = 1  # 총 이동 횟수

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

while cnt < n*n:
    move()  # 한 칸 이동
    remain = arr[x][y]  # 남은 모래의 양
    for i in range(9):  # 각 9개의 위치로 모래 옮기기
        nx, ny, percentage = ratio[direction][i]
        nx += x
        ny += y
        current = int(arr[x][y] * percentage)  # 옮길 모래 양
        # 맵을 벗어나는 경우
        if nx<0 or nx>=n or ny<0 or ny>=n:
            result += current
        else:
            arr[nx][ny] += current
        remain -= current
    # 남은 모래 옮기기
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 맵을 벗어나는 경우
    if nx<0 or nx>=n or ny<0 or ny>=n:
        result += remain
    else:
        arr[nx][ny] += remain
    arr[x][y] = 0
    cnt += 1
print(result)