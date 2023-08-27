from collections import deque
import sys
m, t = map(int, sys.stdin.readline().split())
r, c = map(int, sys.stdin.readline().split())
ground = [[0]*4 for _ in range(4)]
q = deque()
egg = [[0]*4 for _ in range(4)]
ground[r-1][c-1] = -1
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
for _ in range(m):
    r, c, d = map(int, sys.stdin.readline().split())
    ground[r-1][c-1] = d
    q.append((r-1, c-1, d))
while q:
    r, c, d = q.popleft()

    # 몬스터 복제
    egg[r][c] = d

# 몬스터 이동
for i in range(4):
    for j in range(4):
        if ground[i][j] > 0:
            nxt = 0
            for k in range(8):
                I = (ground[i][j]+nxt) % 8
                J = (ground[i][j]+nxt) % 8
                nxt += 1
                if 0<=I<4 and 0<=J<4 and ground[I][J]==0:
                    ground[I][J], ground[i][j] = ground[i][j], ground[I][J]
                    break
            for k in range(r):
                print(ground[k])
            print()
print()
for i in range(r):
    print(egg[i])