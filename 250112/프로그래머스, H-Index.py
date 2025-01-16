# H-Index : i+1개의 논문이 각각 i+1번 이상 인용된 경우
def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        # i는 인덱스 이므로 논문의 개수를 셀 땐 i+1의 개수로 봐야한다
        # ex) [0] 논문은 1개의 논문이다
        if citations[i] < i+1:
            return i
    # 모든 논문이 최소 i+1번 이상 인용된 경우
    return len(citations)


import sys

print(solution(list(map(int, sys.stdin.readline().split(", ")))))
