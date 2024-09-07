from math import ceil


def solution(fees, records):
    answer = []
    inTime = [-1] * 10000
    sumTime = [0] * 10000

    for record in records:
        time, num, type = record.split()
        a, b = time.split(":")
        time = int(a)*60 + int(b)
        num = int(num)

        if type == 'IN':
            inTime[num] = time
        else:
            sumTime[num] += time - inTime[num]
            inTime[num] = -1

    lastTime = 23*60 + 59
    for i in range(10000):
        if inTime[i] > -1:
            sumTime[i] += lastTime - inTime[i]
        if sumTime[i] > 0:
            answer.append(fees[1] + max(ceil((sumTime[i]-fees[0])/fees[2])*fees[3], 0))
    return answer

import sys

fees = list(map(int, sys.stdin.readline().split(", ")))
records = list(sys.stdin.readline().strip().split('", "'))
print(solution(fees, records))