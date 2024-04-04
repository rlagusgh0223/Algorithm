def solution(dirs):
    answer = 0
    x, y = 0, 0
    dir = {'U':(0, 1), 'D':(0, -1), 'R':(1, 0), 'L':(-1, 0)}
    visit = []

    for d in dirs:
        nx, ny = x+dir[d][0], y+dir[d][1]
        if -5<=nx<=5 and -5<=ny<=5:
            if (x, y, nx, ny) not in visit:
                # 출발점과 도착점의 위치가 달라도 길은 같기 때문에
                # 출발점과 도착점의 위치를 바꿔서 visit에 넣어준다
                visit.append((x, y, nx, ny))
                visit.append((nx, ny, x, y))
                answer += 1
            x, y = nx, ny
    return answer

import sys

print(solution(sys.stdin.readline().strip()))
