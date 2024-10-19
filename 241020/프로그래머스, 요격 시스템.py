def solution(targets):
    answer = 0
    targets.sort(key = lambda x:x[1])
    before = 0
    for start, end in targets:
        if before <= start:
            answer += 1
            before = end
    return answer

import sys

targets = list(sys.stdin.readline().strip().split("],["))
targets = [list(map(int, t.split(","))) for t in targets]
print(solution(targets))