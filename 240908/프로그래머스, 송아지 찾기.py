from collections import deque


def solution(s, e):
    dx = [1, -1, 5]
    check = [-1] * 10001
    q = deque()
    q.append(s)
    check[s] = 0
    while q:
        x = q.popleft()
        for i in range(3):
            nx = x+dx[i]
            if nx == e:
                return check[x]+1
            if 1<=nx<=10000 and check[nx]==-1:
                check[nx] = check[x]+1
                q.append(nx)

import sys

s, e = map(int, sys.stdin.readline().split())
print(solution(s, e))