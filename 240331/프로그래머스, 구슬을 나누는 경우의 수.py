def solution(balls, share):
    x= [1, 1] + [0] * (balls)
    for i in range(2, len(x)):
        x[i] = i * x[i-1]
    
    answer = x[balls] // (x[balls-share] * x[share])
    return answer

import sys

x, y = map(int, sys.stdin.readline().split())
print(solution(x, y))