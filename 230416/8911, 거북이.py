import sys
T = int(sys.stdin.readline())
# 시계방향으로 방향전환 할 수 있게 리스트 생성
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(T):
    lst = list(sys.stdin.readline().rstrip())
    max_x = max_y = min_x = min_y = x = y = direction = 0
    for now in lst:
        if now == 'F':
            x += dx[direction]
            y += dy[direction]
        elif now == 'B':
            x -= dx[direction]
            y -= dy[direction]
        elif now == 'L':
            direction = (direction-1) % 4
        elif now == 'R':
            direction = (direction+1) % 4
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        min_y = min(min_y, y)
    print((max_x-min_x) * (max_y-min_y))