def solution(triangle):
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]

import sys

triangle = list(sys.stdin.readline().strip().split("], ["))
triangle = [list(map(int, t.split(", "))) for t in triangle]
print(solution(triangle))