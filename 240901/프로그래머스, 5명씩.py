def solution(names):
    return [names[i] for i in range(0, len(names), 5)]

import sys

print(solution(list(sys.stdin.readline().strip().split('", "'))))
