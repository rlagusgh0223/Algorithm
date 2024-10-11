# 미완성
def solution(plans):
    answer = []
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(":"))
        plans[i][1] = h*60+m
        plans[i][2] = int(plans[i][2])
    plans.sort(key = lambda x:x[1])

    answer.append(plans[0][0])
    time = plans[0][1] + plans[0][2]
    i = 1
    stack = []

    while i<len(plans):
        if plans[i][1] >= time:
            answer.append(plans[i][0])
            time = plans[i][1] + plans[i][2]
        else:
            rtime = time - plans[i][1]
            plans[i][2] -= rtime
            stack.append(plans[i])
        i += 1
    while stack:
        last = stack.pop()
        answer.append(last[0])
    return answer



import sys

plans = list(sys.stdin.readline().strip().split('"], ["'))
plans = [list(p.split('", "')) for p in plans]
print(solution(plans))