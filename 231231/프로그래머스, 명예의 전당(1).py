# 다른 사람의 풀이
def solution(k, score):
    answer = []
    check = []
    for s in score:
        check.append(s)
        if len(check) > k:
            check.remove(min(check))
        answer.append(min(check))
    return answer


import sys
k = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split(", ")))
print(solution(k, score))


def solutions(k, score):
    answer = []
    minScore = []
    for s in score:
        if len(minScore) < k:
            minScore.append(s)
        else:
            if min(minScore) < s:
                minScore.sort()
                minScore[0] = s
        answer.append(min(minScore))
    return answer