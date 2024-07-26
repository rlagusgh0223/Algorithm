def solution(command):
    # 초기 상태는 [0, 1]을 향하게 둔다고 주어졌으므로
    # 거기를 기준으로 오른쪽으로 90도,
    # 왼쪽으로 90도 회전할 수 있는 좌표를 입력한다
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = y = d = 0
    for c in command:
        # R, L은 이동은 하지 않고 방향만 전환하므로 d만 바꾼다
        if c == 'R':
            d = (d+1) % 4
        elif c == 'L':
            d = (d-1) % 4
        # 각 방향으로 앞으로 한칸, 뒤로 한칸이므로 더하고 뺀다
        elif c == 'G':
            x, y= x+dx[d], y+dy[d]
        else:
            # -1 // 4 = -1
            # -1 / 4 = -0.25 에서 소수 부분을 버리고
            # 가장 가까운 정수로 내림하면 -1이 된다

            # a%b는 a - (a // b) * b와 동일하다
            # -1 % 4  = -1 - (-1//4) * 4
            #         = -1 - (-1) * 4
            #         = -1 - (-4)
            #         = 3
            x, y = x-dx[d], y-dy[d]
    return [x, y]

import sys

print(solution(sys.stdin.readline().strip()))
