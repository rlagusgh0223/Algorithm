from collections import Counter


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]


# 아래 코드는 시간초과 나온다
#  def solution(participant, completion):
#     for c in completion:
#         del participant[participant.index(c)]
#     return participant[0]

import sys

p = list(sys.stdin.readline().strip().split('", "'))
c = list(sys.stdin.readline().strip().split('", "'))
print(solution(p, c))