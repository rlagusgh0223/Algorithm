# 원리는 내 코드와 같지만 더 짧은 코드이기에 남긴다
def solution(score):
    answer = sorted([sum(s) for s in score], reverse=True)
    return [answer.index(sum(i))+1 for i in score]

# def solution(score):
#     answer = []
#     res = [0] * len(score)
#     for i in range(len(score)):
#         res[i] = sum(score[i]) / 2
#     check = list(sorted(res, reverse=True))
#     for r in res:
#         answer.append(check.index(r) + 1)
#     return answer

import sys

score = list(sys.stdin.readline().strip().split("], ["))
score = [list(map(int, s.split(", "))) for s in score]
print(solution(score))