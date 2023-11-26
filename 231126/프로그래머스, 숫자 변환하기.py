from collections import deque
def solution(x, y, n):
    if x == y:
        return 0
    q = deque()
    q.append(x)
    # y까지의 수 중 몇번의 연산을 통해 온건지 입력할 리스트
    ck = [0] * (y+1)
    while q:
        x = q.popleft()
        for i in range(3):
            if i == 0:
                nx = x+n
            elif i == 1:
                nx = x*2
            else:
                nx = x*3
            # y를 초과한 값이거나 이미 점검한 값이면 의미 없으므로 continue
            # 이미 점검한 값 또 점검하면 시간초과 나온다
            if nx>y or ck[nx]:
                continue
            # y가 맞으면 기존에 받은 값에서 연산을 한번 더 한것이므로 그 값 리턴
            if nx == y:
                return ck[x]+1
            q.append(nx)
            ck[nx] = ck[x]+1
    return -1


import sys
x, y, n = map(int, sys.stdin.readline().split())
print(solution(x, y, n))