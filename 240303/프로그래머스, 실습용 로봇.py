def solution(command):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y, d = 0, 0, 0
    for c in command:
        if c == 'R':
            d = (d+1) % 4
        elif c == 'L':
            # -1//4 = -1
            # -1%4 = 3
            # -1을 4로 나누면 -1이 몫으로 들어가고
            # -1에서 -4를 빼므로 3이 남는다
            d = (d-1) % 4
        elif c == 'G':
            x, y = x+dx[d], y+dy[d]
        else:
            x, y = x-dx[d], y-dy[d]
    return [x, y]

import sys

print(solution(sys.stdin.readline().strip()))
