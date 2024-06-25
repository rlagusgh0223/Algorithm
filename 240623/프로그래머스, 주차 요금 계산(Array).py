from math import ceil


def solution(fees, records):
    answer = []
    # 입력시간을 저장하기 위한 리스트
    # 0시에 입력할 수 있으므로 초기에 -1을 줘야된다
    # 차량번호는 0000 ~ 9999이므로 10000개의 리스트면
    # 모든 차량을 저장할 수 있다
    inTime = [-1] * 10000
    # 해당 차량이 주차장에 있었던 총 시간을 저장할 리스트
    sumTime = [0] * 10000

    # 주차장에 들어오고 나온 차량들의 시간 계산
    # 모든 시간은 분으로 계산한다
    # 들어온 차량은 들어온 시간을 입력하고,
    # 나간 차량은 -1로 다시 초기화시킨다
    for record in records:
        a, b, c = record.split()
        h, m = map(int, a.split(":"))
        a = h*60 + m
        b = int(b)
        if c == 'IN':
            inTime[b] = a
        else:
            sumTime[b] += a - inTime[b]
            inTime[b] = -1
    
    last = 23*60 + 59  # 23:59까지 나가지 않은 차의 시간을 계산하기 위한 변수
    for i in range(10000):
        # 아직 나가지 않은 차량은 23:59에 나간걸로 계산하고
        # sumTime에 입력한다
        if inTime[i] != -1:
            sumTime[i] += last - inTime[i]
        # sumTime에 값이 들어왔다면(주차장에 주차한 적이 있다면)
        # 요금 계산 후 answer에 입력한다
        # 0000부터 차 번호순으로 계산하고 있으므로
        # 별도로 정렬할 필요 없다
        if sumTime[i] != 0:
            # ceil을 이용해서 소수점 자리 있으면 자릿수 올려준다
            # max를 이용해서 기본시간보다 적게 주차한 경우 음수가 나오는데
            # 0으로 계산하게 해준다
            answer.append(fees[1] + max(ceil((sumTime[i]-fees[0]) / fees[2]), 0) * fees[3])

    return answer

import sys

fees = list(map(int, sys.stdin.readline().split(", ")))
records = list(sys.stdin.readline().strip().split('", "'))
print(solution(fees, records))