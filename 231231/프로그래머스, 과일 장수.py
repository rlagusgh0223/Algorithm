def solutions(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        if i+m <= len(score):
            now = list(score[i:i+m])
            answer += min(now) * m
    return answer


import sys
k, m = map(int, sys.stdin.readline().split())
score = list(map(int, sys.stdin.readline().split(", ")))
print(solution(k, m, score))