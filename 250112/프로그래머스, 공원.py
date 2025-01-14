def solution(mats, park):
    mats.sort(reverse=True)
    r, c = len(park), len(park[0])

    def can(size, x, y):
        if x+size>r or y+size>c:
            return False
        for i in range(x, x+size):
            for j in range(y, y+size):
                if park[i][j] != '-1':
                    return False
        return True

    for mat in mats:
        for i in range(r):
            for j in range(c):
                if can(mat, i, j):
                    return mat
    return -1

import sys

mats = list(map(int, sys.stdin.readline().split(",")))
park = list(sys.stdin.readline().strip().split('"], ["'))
park = [list(p.split('", "')) for p in park]
print(solution(mats, park))