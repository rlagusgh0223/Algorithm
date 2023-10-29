def solution(brown, yellow):
    # yellow가 하나는 있어야 되므로 yellow를 감싸기 위해선 위, 아래 3칸씩은 있어야 된다
    for i in range(3, brown//2):
        for j in range(3, brown//2):
            if i*j == brown+yellow and (i-2)*(j-2)==yellow:
                return [j, i]

import sys
brown, yellow = map(int, sys.stdin.readline().split())
print(solution(brown, yellow))