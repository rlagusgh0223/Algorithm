def solution(n):
    answer = []
    def hanoi(start, end, middle, n):
        if n == 1:
            answer.append([start, end])
        else:
            # n-1개의 원판을 출발 기둥에서 중간 기둥으로 이동
            hanoi(start, middle, end, n-1)
            # n번째 원판을 출발 기둥에서 도착 기둥으로 이동
            hanoi(start, end, middle, 1)
            # n-1개의 원판을 중간 기둥에서 도착 기둥으로 이동
            hanoi(middle, end, start, n-1)
    hanoi(1, 3, 2, n)
    return answer

import sys
print(solution(int(sys.stdin.readline())))
