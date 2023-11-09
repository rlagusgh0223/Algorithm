# 모범답안
def solutions(progresses, speeds):
    answer = []
    for p, s in zip(progresses, speeds):
        if len(answer)==0 or answer[-1][0] < -((p-100)//s):
            answer.append([-((p-100)//s), 1])  # 완성까지 걸리는 날, 몇개의 작업이 한번에 되는지
        else:
            answer[-1][1] += 1
    return [a[1] for a in answer]


def solution(progresses, speeds):
    answer = []
    day = [0]
    for i in range(len(speeds)):
        d = 0
        while 100-progresses[i] > speeds[i]*d:
            d += 1
        day.append(max(day[-1], d))
    cnt = 1
    day.append(0)
    for i in range(1, len(day)-1):
        if day[i] == day[i+1]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
    return answer

import sys
progresses = list(map(int, sys.stdin.readline().strip().split(', ')))
speeds = list(map(int, sys.stdin.readline().strip().split(', ')))
print(solutions(progresses, speeds))