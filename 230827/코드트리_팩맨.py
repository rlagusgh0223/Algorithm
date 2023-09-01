from collections import deque
import sys
m, t = map(int, sys.stdin.readline().split())
r, c = map(int, sys.stdin.readline().split())
q = deque()
egg = [[0]*4 for _ in range(4)]
egg[r-1][c-1] = -1
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
for _ in range(m):
    r, c, d = map(int, sys.stdin.readline().split())
    q.append((r-1, c-1, d))
while q:
    r, c, d = q.popleft()

    # 몬스터 복제
    egg[r][c] = d

    # 몬스터 이동
    nxt = 0
    for k in range(8):
        I = (d+dx[nxt]) % 8
        J = (d+dy[nxt]) % 8
        nxt += 1
        if 0<=I<4 and 0<=J<4 and egg[I][J] != -1:
            egg[I][J], egg[r][c] = egg[r][c], egg[I][J]
            print(I, J)
            # q.append((I, J, egg[I][J]))
            break
    # for k in range(4):
    #     print(egg[k])
    # print()
for i in range(4):
    print(egg[i])