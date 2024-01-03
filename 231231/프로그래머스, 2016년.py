def solution(a, b):
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    # a, b를 1, 1을 넣었을때 FRI가 나오도록 요일을 배치했다
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    return day[(sum(month[:a-1]) + b) % 7]

import sys
a, b = map(int, sys.stdin.readline().split())
print(solution(a, b))