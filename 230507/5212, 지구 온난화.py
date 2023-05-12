# 지도 바깥의 부분은 모두 바다다
import sys
R, C = map(int, sys.stdin.readline().split())
ground = [['.']*(C+2)] + [['.']+list(sys.stdin.readline().rstrip())+['.'] for _ in range(R)] + [['.']*(C+2)]  # 지도 테두리 부분 바다인것 지도에 반영
check = [[0]*(C+2) for _ in range(R+2)]  # 지도에서 지금은 육지인 곳 표시할 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 육지가 있는곳이 사이드에 있는 지도를 출력하기 위한 좌표
maxx = maxy = 0
minx = R+2
miny = C+2
for x in range(1, R+1):
    for y in range(1, C+1):
        if ground[x][y] == 'X':  # 지도에서 지금 육지인 부분이라면
            check[x][y] = 1  # 체크 리스트에 표시
            cnt = 0  # 주변 바다의 수를 계산하기 위한 변수
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if ground[nx][ny]=='.' and check[nx][ny]==0:  # 주변이 바다이고 육지였다가 바다가 된게 아니라면
                    cnt += 1  # 바다의 수를 더한다
            if cnt >= 3:  # 주변에 바다가 3군데 이상 붙어있으면 바다가 된다
                ground[x][y] = '.'  # 육지를 바다로 바꾼다
            else:
                minx = min(minx, x)
                miny = min(miny, y)
                maxx = max(maxx, x)
                maxy = max(maxy, y)
for i in range(minx, maxx+1):
    for j in range(miny, maxy+1):
        print(ground[i][j], end='')
    print()