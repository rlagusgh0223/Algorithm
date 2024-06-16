# H-Index
# 연구자의 논문 중 H번 이상 인용된 논문이 H편 있는 경우
# H-지수는 H다
def solution(citations):
    # 내림차순 정렬
    # ex) [6, 5, 3, 1, 0]
    citations.sort(reverse=True)
    # 논문의 인용횟수 비교
    for i in range(len(citations)):
        # 1번째 논문 : 6회 인용(6 < 0+1)
        # 2번째 논문 : 5회 인용(5 < 1+1)
        # 3번째 논문 : 3회 인용(3 < 2+1)
        # 4번째 논문 : 1회 인용(1 < 3+1)
        # H는 3이 된다
        if citations[i] < i+1:
            return i
    return len(citations)

import sys

print(solution(list(map(int, sys.stdin.readline().split(", ")))))
