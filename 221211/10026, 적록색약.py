def can(blind, u, v):
    if u == v:
        return True
    if blind:
        if u=='R' and v=='G':
            return True
        if u=='G' and v=='R':
            return True
    return False

def go(a, blind):
    check = [[False]*n for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if check[i][j]:
                continue
            check[i][j] = True
            ans += 1
            q = deque()
            q.append((i, j))
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x+dx[k] ,y+dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if check[nx][ny]:
                            continue
                        if can(blind, a[nx][ny], a[x][y]):
                            check[nx][ny] = True
                            q.append((nx, ny))
    return ans

from collections import deque
n = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
a = [input() for _ in range(n)]
print(str(go(a, False)) + ' ' + str(go(a, True)))