def solution(distance, rocks, n):
    start, end, answer = 0, distance, 0
    rocks = sorted(rocks+[distance])
    while start <= end:
        mid = (start+end) // 2
        before, min_dis, remove = 0, distance+1, 0
        for rock in rocks:
            dis = rock - before
            if dis < mid:
                remove += 1
            else:
                min_dis = min(dis, min_dis)
                before = rock
        if remove > n:
            end = mid - 1
        else:
            start = mid + 1
            answer = min_dis
    return answer

import sys

d = int(sys.stdin.readline())
rocks = list(map(int, sys.stdin.readline().split(", ")))
n = int(sys.stdin.readline())
print(solution(d, rocks, n))