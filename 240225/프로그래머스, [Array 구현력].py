from math import ceil


def solution(fees, records):
    answer = []
    inTime = [-1] * 10000
    sumTime = [0] * 10000
    for record in records:
        a, b, c = record.split()
        h, m = map(int, a.split(":"))
        a = h*60 + m
        b = int(b)
        if c == 'IN':
            inTime[b] = a
        else:
            sumTime[b] += (a - inTime[b])
            inTime[b] = -1

    for i in range(10000):
        if inTime[i] != -1:
            sumTime[i] += ((23*60+59) - inTime[i])

        if sumTime[i] != 0:
            # ceil은 math의 함수로, 소수점이 있으면 무조건 반올림 해준다
            # 그러므로 //로 나누면 안된다
            # 기본시간보다 적게 있었으면 ceil 후 값이 0보다 작으므로
            # max를 이용해 0보다 작은 값이 없게 해 요금이 깎이지 않게 한다
            answer.append(fees[1] + max(ceil((sumTime[i] - fees[0])/fees[2]), 0)*fees[3] )
    return answer

import sys

fees = list(map(int, sys.stdin.readline().split(", ")))
records = list(sys.stdin.readline().strip().split('", "'))
print(solution(fees, records))