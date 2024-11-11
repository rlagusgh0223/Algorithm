def solution(dot):
    x, y = dot[0], dot[1]
    if x>0 and y>0:
        return 1
    elif x<0 and y>0:
        return 2
    elif x<0 and y<0:
        return 3
    # 0은 원소가 아니라고 문제에서 나왔으므로 나머지는 4사분면 뿐이다
    else:
        return 4

import sys

d = list(map(int, sys.stdin.readline().split(", ")))
print(solution(d))