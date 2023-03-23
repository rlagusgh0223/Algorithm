# 단순히 모든 칸을 방문하는걸로 끝이 아니라
# 나이트의 경로로 이동하며
# 마지막칸에서 나이트의 경로로 시작칸으로 이동 가능한지 확인해야 한다
import sys
check = [[0]*6 for _ in range(6)]
visit = [[0, 0] for _ in range(36)]
a = ['A', 'B', 'C', 'D', 'E', 'F']
for i in range(36):
    now = sys.stdin.readline().rstrip()
    x = a.index(now[0])
    y = int(now[1]) - 1
    visit[i][0], visit[i][1] = x, y
    if i == 0:
        check[x][y] = 1
for i in range(1, 36):
    X, Y, x, y = visit[i-1][0], visit[i-1][1], visit[i][0], visit[i][1]
    if ((abs(X-x)==2 and abs(Y-y)==1) or (abs(X-x)==1 and abs(Y-y)==2)) and check[x][y] == 0:
        check[x][y] = 1
    else:
        print("Invalid")
        exit()
sx, sy, ex, ey = visit[0][0], visit[0][1], visit[-1][0], visit[-1][1]
if (abs(sx-ex)==2 and abs(sy-ey)==1) or (abs(sx-ex)==1 and abs(sy-ey)==2):
    print("Valid")
else:
    print("Invalid")