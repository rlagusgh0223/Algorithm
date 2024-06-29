from collections import deque


def solution(s, e):
    dx = [1, -1, 5]
    q = deque()
    q.append(s)
    # check를 해서 중복된 값을 계산하지 않는 김에
    # 해당 위치까지 가는 최소 거리를 입력했다
    check = [-1] * 10001
    check[s] = 0
    while q:
        x = q.popleft()
        for d in dx:
            nx = x + d
            if nx == e:
                return check[x] + 1
            # 1<=nx<=10000 조건 없으면 에러 나온다
            if 1<=nx<=10000 and check[nx] == -1:
                check[nx] = check[x] + 1
                q.append(nx)


import sys

s, e = map(int, sys.stdin.readline().split())
print(solution(s, e))