from collections import deque


def solution(s, e):
    q = deque()
    q.append(s)
    dx = [1, -1, 5]
    check = [-1] * 10001
    check[s] = 0
    while q:
        x = q.popleft()
        for i in range(3):
            nx = x + dx[i]
            if nx == e:
                return check[x] + 1
            if 1<=nx<=10000 and check[nx]==-1:
                q.append(nx)
                check[nx] = check[x] + 1

import sys

s, e = map(int, sys.stdin.readline().split())
print(solution(s, e))