def solution(date1, date2):
    d1, d2 = 0, 0
    for i in range(3):
        d1 = d1*100 + date1[i]
        d2 = d2*100 + date2[i]
    return 1 if d1<d2 else 0

import sys

d1 = list(map(int, sys.stdin.readline().split(", ")))
d2 = list(map(int, sys.stdin.readline().split(", ")))
print(solution(d1, d2))