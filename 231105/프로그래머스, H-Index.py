# H-index
# 내림차순된 정렬에서 n번째(1부터 시작한다) 인덱스 값이 최초로 n을 넘지 않을때
# n-1이 H-Index값이 된다
def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i
    # 인용된 수가 모두 n보다 크다면 문자열 길이를 출력한다
    # [5, 5, 5, 5] 이면 위의 식으로는 답이 안나온다
    return len(citations)

import sys
citations = list(map(int, sys.stdin.readline().split(',')))
print(solution(citations))