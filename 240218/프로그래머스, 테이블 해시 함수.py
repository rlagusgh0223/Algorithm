def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x:[x[col-1], -x[0]])
    for i in range(row_begin, row_end+1):
        total = 0
        for j in data[i-1]:
            total += (j%i)
        answer ^= total
    return answer

import sys
data = list(sys.stdin.readline().strip().split("],["))
data = [list(map(int, d.split(","))) for d in data]
c, rb, re = map(int, sys.stdin.readline().split())
print(solution(data, c, rb, re))