def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage += (usage * change[i]) / 100
        total_usage += usage
        if total_usage > storage:
            return i
    
    return -1

import sys

s, u = map(int, sys.stdin.readline().split())
change = list(map(int, sys.stdin.readline().split(", ")))
print(solution(s, u, change))