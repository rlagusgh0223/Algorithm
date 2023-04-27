import sys
n = int(sys.stdin.readline())
lst = list(sys.stdin.readline().rstrip())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
now = 0
x = y = minx = miny = maxx = maxy = 0
ground = [[x, y]]
for i in range(n):
    if lst[i] == 'R':
        now = (now+1) % 4
    elif lst[i] == 'L':
        now = (now-1) % 4
    else:
        x, y = x+dx[now], y+dy[now]
        ground.append([x, y])

sort_x = sorted(ground, key=lambda x:x[0])
sort_y = sorted(ground, key=lambda x:x[1])
minx, maxx = sort_x[0][0], sort_x[-1][0]
miny, maxy = sort_y[0][1], sort_y[-1][1]

maze = [['#' for _ in range(miny, maxy+1)] for _ in range(minx, maxx+1)]

# 음수가 나올 경우 가장 작은 음수만큼 그래프를 이동시킨다
# 음수가 없으면 최솟값은 시작점인 0이므로 아무 영향이 없다
for i in range(len(ground)):
    ground[i][0], ground[i][1] = ground[i][0]-minx, ground[i][1]-miny
for x, y in ground:
    maze[x][y] = '.'
for i in maze:
    print(''.join(i))