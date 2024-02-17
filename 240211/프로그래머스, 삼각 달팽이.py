def solution(n):
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)]
    x, y = -1, 0
    now = 0
    for i in range(n):  # 나아가는 칸수(4,3,2,1 순서로 나간다)
        for j in range(i, n):  # 방향(%=0이면 아래, %=1이면 오른쪽, %=2면 위)
            if i%3 == 0:
                x += 1
            elif i%3 == 1:
                y += 1
            else:
                x, y = x-1, y-1
            now += 1
            answer[x][y] = now
    return sum(answer, [])  # 이차원 배열을 1차원 배열로 만들어서 리턴

import sys

print(solution(int(sys.stdin.readline())))
