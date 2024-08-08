import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        x = heapq.heappop(scoville)
        if x >= K:
            return answer
        y = heapq.heappop(scoville)
        answer += 1
        heapq.heappush(scoville, x + 2*y)
    return -1 if scoville[0] < K else answer



# import heapq


# def solution(scoville, K):
#     answer = 0
#     heapq.heapify(scoville)  # scoville을 heap으로 변환
#     x = heapq.heappop(scoville)  # scovile에서 가장 작은 값 빼서 x에 입력
#     while x < K:
#         y = heapq.heappop(scoville)  # scoville에서 두번째로 작은 값 빼서 입력
#         heapq.heappush(scoville, x+(y*2))
#         answer += 1
#         x = heapq.heappop(scoville)  # 연산 후 scoville에서 가장 작은 값 빼서 x에 입력
#         if len(scoville)==0 and x<K:  # 더 이상 섞을 음식이 없는데 K보다 작을 경우 값이 나올 수 없으므로 -1 리턴
#             return -1
#     return answer

import sys

scoville = list(map(int, sys.stdin.readline().split(", ")))
K = int(sys.stdin.readline())
print(solution(scoville, K))