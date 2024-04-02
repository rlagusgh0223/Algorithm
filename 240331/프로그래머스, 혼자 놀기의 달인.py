def solution(cards):
    answer = []
    visit = [False] * (len(cards) + 1)
    for v in cards:
        if not visit[v]:
            tmp = []
            while v not in tmp:
                tmp.append(v)
                v = cards[v-1]
                visit[v] = True
            answer.append(len(tmp))
    if answer[0] == len(cards):
        return 0
    else:
        answer.sort(reverse=True)
    return answer[0] * answer[1]

import sys

cards = list(map(int, sys.stdin.readline().split(",")))
print(solution(cards))