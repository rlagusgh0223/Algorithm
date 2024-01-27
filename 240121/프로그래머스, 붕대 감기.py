def solution(bandage, health, attacks):
    answer = health
    time = 0
    cnt = 0
    ck = 0
    while time < attacks[-1][0]:
        time += 1
        if time == attacks[ck][0]:
            cnt = 0
            answer -= attacks[ck][1]
            ck += 1
        else:
            cnt += 1
            answer += bandage[1]
            if cnt == bandage[0]:
                cnt = 0
                answer += bandage[2]
            answer = min(answer, health)
        if answer <= 0:
            return -1
    return answer

import sys
b = list(map(int, sys.stdin.readline().split(", ")))
h = int(sys.stdin.readline())
a = list(sys.stdin.readline().split("], ["))
a = [list(map(int, now.split(", "))) for now in a]
print(solution(b, h, a))