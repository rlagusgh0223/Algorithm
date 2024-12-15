# 문제에서 하라는대로 한 풀이
# def solution(wallet, bill):
#     answer = 0
#     wmax, wmin, bmax, bmin = max(wallet), min(wallet), max(bill), min(bill)
#     while bmin>wmin or bmax>wmax:
#         if bill[0] > bill[1]:
#             bill[0] //= 2
#         else:
#             bill[1] //= 2
#         bmax, bmin = max(bill), min(bill)
#         answer += 1
#     return answer

# 시간 차이는 없지만 코드가 더 간결해서 짜봤다
def solution(wallet, bill):
    answer = 0
    wallet[0], wallet[1], bill[0], bill[1] = max(wallet), min(wallet), max(bill), min(bill)
    while bill[1]>wallet[1] or bill[0]>wallet[0]:
        bill[0] //= 2
        bill[0], bill[1] = max(bill), min(bill)
        answer += 1
    return answer

import sys

w = list(map(int, sys.stdin.readline().split(", ")))
b = list(map(int, sys.stdin.readline().split(", ")))
print(solution(w, b))