# defaultdict() : 딕셔너리 값이 없으면 지정한 형태에 맞춰 초기값 세팅하는 딕셔너리
from collections import defaultdict
# ceil() : 괄호 안의 값의 소수점 올림한 정수로 만듦
from math import ceil


def solution(fees, records):
    answer = []
    records = [list(r.split()) for r in records]
    check, value = defaultdict(int), defaultdict(int)
    for record in records:
        h, m = map(int, record[0].split(":"))
        time = h*60 + m
        if record[2] == 'IN':
            check[record[1]] = time
        elif record[2] == 'OUT':
            value[record[1]] += time - check[record[1]]
            del check[record[1]]
    if len(check) > 0:
        for ck in check.keys():
            value[ck] += (23*60 + 59) - check[ck]

    value = dict(sorted(value.items()))
    for val in value.values():
        if val <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + ceil( (val-fees[0])/fees[2] ) * fees[3])
    return answer

import sys

# 기본시간(분), 기본요금(원), 단위시간(분), 단위요금(원)
fees = list(map(int, sys.stdin.readline().split(", ")))
records = list(sys.stdin.readline().strip().split('", "'))
print(solution(fees, records))