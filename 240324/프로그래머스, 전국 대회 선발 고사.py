def solution(rank, attendance):
    answer = []
    cnt = 1
    while len(answer) < 3:
        now = rank.index(cnt)
        if attendance[now]:
            answer.append(now)
        cnt += 1
    return answer[0]*10000 + answer[1]*100 + answer[2]


import sys

rank = list(map(int, sys.stdin.readline().split(", ")))
attendance = list(sys.stdin.readline().strip().split(", "))
print(solution(rank, attendance))