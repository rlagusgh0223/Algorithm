def solution(distance, rocks, n):
    answer, start, end = 0, 0, distance
    rocks = sorted(rocks+[distance])
    while start <= end:
        mid = (start+end) // 2
        now, min_dis, remove = 0, distance+1, 0
        for rock in rocks:
            dis = rock - now
            if dis < mid:
                remove += 1
            else:
                min_dis = min(dis, min_dis)
                now = rock
        if remove > n:
            end = mid - 1
        else:
            start = mid + 1
            answer = min_dis
    return answer

import sys

distance = int(sys.stdin.readline())
rocks = list(map(int, sys.stdin.readline().split(", ")))
n = int(sys.stdin.readline())
print(solution(distance, rocks, n))