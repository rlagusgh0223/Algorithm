from collections import Counter


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

import sys

p = list(sys.stdin.readline().strip().split('", "'))
c = list(sys.stdin.readline().strip().split('", "'))
print(solution(p, c))