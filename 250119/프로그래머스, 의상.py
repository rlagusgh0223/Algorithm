from collections import defaultdict


def solution(clothes):
    answer = 1
    cloth = defaultdict(list)
    for c in clothes:
        cloth[c[1]].append(c[0])
    for c in cloth:
        answer *= (len(cloth[c])+1)
    return answer - 1



import sys

clothes = list(sys.stdin.readline().strip().split('"], ["'))
clothes = [list(c.split('", "')) for c in clothes]
print(solution(clothes))