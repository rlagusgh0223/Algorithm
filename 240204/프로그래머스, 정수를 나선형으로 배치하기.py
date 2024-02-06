def solution(n):
    answer = [[0]*n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y, d = 0, -1, 0
    cnt = 1
    while cnt <= n*n:
        nx, ny = x+dx[d], y+dy[d]
        if 0<=nx<n and 0<=ny<n and answer[nx][ny]==0:
            answer[nx][ny] = cnt
            cnt += 1
            x, y = nx, ny
        else:
            d = (d+1) % 4
    return answer

import sys
n = int(sys.stdin.readline())
print(solution(n))