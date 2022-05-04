# 모범답안
# import heapq, sys
# N = int(sys.stdin.readline())

# card = list(int(sys.stdin.readline()) for _ in range(N))
# heapq.heapify(card)    # n개의 카드를 힙으로 변환
# answer = 0

# while len(card) != 1:
#     first = heapq.heappop(card)
#     second = heapq.heappop(card)
#     sum = first + second
#     answer += sum
#     heapq.heappush(card, sum)

# print(answer)
#############################################
# 문제를 해결하기 위해 가장 작은 값과 그 다음 작은값을 더하고
# 그 값을 다시 힙에 넣은 후 
# 첫번재 연산을 반복
# 우선순위 큐를 사용한다
import sys, heapq

N = int(sys.stdin.readline())
card = []
result = 0
for i in range(N):    # 입력받는 값 우선수위 큐를 위해 heapq로 저장
    x = int(sys.stdin.readline())
    heapq.heappush(card, x)

while len(card) > 1:    # 비교할 자료가 2개 이상 남아있다면 계속 진행하기 위해 반복문을 사용한다
    x = heapq.heappop(card)    # 가장 작은 값 입력
    y = heapq.heappop(card)    # 그 다음 작은 값 입력
    sum = x + y    # 현재 힙의 값 중 가장 작은 값과 그 다음 작은 값 더한다
    result += sum    # 그 값을 이 전까지의 값과 더한다
    heapq.heappush(card, sum)    # 힙에는 다시 가장 작은 값과 그 다음 작은 값 더한값을 입력한다

print(result)    # 마지막으로 하나 남은 값은 계산을 마친 값이므로 출력